import pandas as pd
import datetime

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
         'application_type'], axis=1, inplace=True)

mean_mths_since_last_delinq = int(df['mths_since_last_delinq'].mean())
df['mths_since_last_delinq'].fillna(mean_mths_since_last_delinq, inplace=True)
df.dropna(inplace=True)
def clean_term(val):
    return int(val.replace(' months', ''))
df['term'] = df['term'].apply(clean_term)
# Convert to categorical
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
df['earliest_cr_line'] = pd.to_datetime(df['earliest_cr_line'], format='%b-%y').astype(int) // 10**6 #nojala
df['initial_list_status'] = df['initial_list_status'].astype('category')
df['last_pymnt_d'] = pd.to_datetime(df['last_pymnt_d'], format='%b-%y').astype(int) // 10**6 #nojala
df['last_credit_pull_d'] = df['last_credit_pull_d'].astype('category')
df.info()
