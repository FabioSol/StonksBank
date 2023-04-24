import numpy as np
import pandas as pd
import datetime
from sklearn.utils import resample
from typing import Dict
from transformers.columnSelectorTransformer import ColumnSelectorTransformer
from transformers.woeTransformer import WOETransformer
from transformers.binningTransformer import BinningTransformer
from bins import bins
dataset = pd.read_csv('../files/credit_risk_data_v2.csv', low_memory=False)
#%%
cols_to_keep = ['loan_amnt', 'funded_amnt', 'term', 'int_rate',
       'installment', 'grade', 'sub_grade', 'emp_length', 'home_ownership',
       'annual_inc', 'verification_status', 'pymnt_plan', 'purpose',
       'addr_state', 'dti', 'delinq_2yrs', 'inq_last_6mths',
       'open_acc', 'pub_rec', 'revol_bal',
       'revol_util', 'total_acc', 'initial_list_status', 'out_prncp',
       'total_pymnt', 'total_rec_prncp',
       'total_rec_int', 'total_rec_late_fee', 'recoveries',
       'collection_recovery_fee', 'last_pymnt_amnt',
       'collections_12_mths_ex_med', 'acc_now_delinq', 'tot_coll_amt',
       'tot_cur_bal', 'total_rev_hi_lim', 'status']
#%%
column_t = ColumnSelectorTransformer(columns=cols_to_keep)
binning_t = BinningTransformer(bins=bins)
woe_t = WOETransformer(columns=cols_to_keep)
#%%
dataset_c = column_t.transform(dataset)
dataset_c.head()
#%%
# dataset_c = column_t.clean(X=dataset_c)
#%%
dataset_c = dataset_c.dropna()
#%%
x_train_c = dataset_c.drop("status", axis=1)
y_train = dataset_c["status"]
#%%
x_train_b = binning_t.transform(x_train_c)
x_train_b.head()
#%%
woe_t.fit(x_train_b, y_train)
#%%
woe_t.transform(x_train_b)