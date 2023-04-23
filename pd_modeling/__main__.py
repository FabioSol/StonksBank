import numpy as np
import pandas as pd
import datetime
from sklearn.utils import resample
from typing import Dict

df = pd.read_csv('../files/credit_risk_data_v2.csv', low_memory=False)

# Data preprocessing
df.drop(['id', 'member_id', 'open_acc_6m', 'open_il_6m', 'open_il_12m',
         'open_il_24m', 'mths_since_rcnt_il', 'total_bal_il',
         'il_util', 'open_rv_12m', 'open_rv_24m',
         'annual_inc_joint', 'dti_joint', 'verification_status_joint',
         'mths_since_last_record', 'url', 'emp_title',
         'issue_d', 'desc', 'max_bal_bc', 'all_util',
         'inq_fi', 'total_cu_tl', 'inq_last_12m',
         'mths_since_last_major_derog', 'next_pymnt_d', 'policy_code',
         'application_type', 'title', 'earliest_cr_line',
         'last_pymnt_d', 'last_credit_pull_d'], axis=1, inplace=True)

mean_mths_since_last_delinq = int(df['mths_since_last_delinq'].mean())
df['mths_since_last_delinq'].fillna(mean_mths_since_last_delinq, inplace=True)
df.dropna(inplace=True)


def clean_term(val):
    return int(val.replace(' months', ''))


df['term'] = df['term'].apply(clean_term)

# Convert to categorical or unix
df['grade'] = df['grade'].astype('category')
df['sub_grade'] = df['sub_grade'].astype('category')
df['emp_length'] = df['emp_length'].astype('category')
df['home_ownership'] = df['home_ownership'].astype('category')
df['verification_status'] = df['verification_status'].astype('category')
df['pymnt_plan'] = df['pymnt_plan'].astype('category')
df['purpose'] = df['purpose'].astype('category')
df['title'] = df['title'].astype('category')
df['zip_code'] = df['zip_code'].astype('category')
df['addr_state'] = df['addr_state'].astype('category')
df['initial_list_status'] = df['initial_list_status'].astype('category')

# Check dataset balance
status_aggregation = (
        df.groupby("status").size().to_frame().rename(columns={0: "count"}) / len(df)
)

# Undersampling
majority_class = df[df['status'] == 0]
minority_class = df[df['status'] == 1]
n_samples = len(minority_class)
undersampled_majority = resample(majority_class,
                                 replace=False,
                                 n_samples=37666)
undersampled_df = pd.concat([undersampled_majority, minority_class])

# WoE

def get_absolute_odds (
        df: pd.DataFrame,
    col: str,
    target: str = "status",
    target_mappings: Dict = {0: "good", 1: "bad"},
    absolute_values: bool = False
):
    # Configuration of the target map
    key_first, key_second = list(target_mappings.keys()) # Calculate absolute odds & assign good/bad Labels
    return (
        df.query(f" {target} == {key_first}")
        .groupby(col).size().reset_index()
        .rename (columns={0: target_mappings[key_first]})
        .set_index(col)
    ).join(
        df.query(f" {target} == {key_second}")
        .groupby(col).size().reset_index()
        .rename (columns={0: target_mappings[key_second]})
        .set_index(col)
    ).reset_index()[[col, "good", "bad"]]

def calculate_relative_odds(row: pd.Series, total_good: int, total_bad: int) -> pd.Series:
    return pd.Series(
        {
            **row.to_dict(),
            "good": row["good"] / total_good,
            "bad": row["bad"] / total_bad
        }
    )
def get_odds (
    df: pd.DataFrame,
    col: str,
    target: str = "status",
    target_mappings: Dict = {0: "good", 1: "bad"},
    absolute_values: bool = False
):
    # Configuration of the target map
    key_first, key_second = list(target_mappings.keys())
    # Calculate absolute odds & assign good/bad Labels
    odds_absolute = get_absolute_odds(df, col, target, target_mappings, absolute_values)
    if absolute_values:
        return odds_absolute
    # Calculate relative odds
    total_good = odds_absolute["good"].sum()
    total_bad = odds_absolute ["bad"].sum()
    return odds_absolute.apply(
        lambda row: calculate_relative_odds (
            row=row,
            total_good=total_good,
            total_bad=total_bad
        ),
        axis=1
    )
def calculate_woe (row: pd.Series) -> pd.Series:
    if row['bad'] != 0 and row['bad'] != 0.0:
        # print(row)
        return pd.Series (
            {
                **row.to_dict(),
                "woe": np.log(row["good"] / row["bad"]),
                "info_val": (row["good"]/row["bad"]) * np.log(row["good"] / row["bad"])
            }
        )
    else:
        print('row[bad] is zero')
        raise 'error'

def get_woe(
    df: pd.DataFrame,
    col: str,
    target: str = "status",
    target_mappings: Dict = {0: "good", 1: "bad"}
) -> pd.DataFrame:
    # if df[col]
    return get_odds(df, col, target, target_mappings, absolute_values=False)\
        .apply(lambda row: calculate_woe(row), axis=1)\
        .sort_values(by="woe", axis=0, ascending=True)