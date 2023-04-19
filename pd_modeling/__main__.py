import pandas as pd

df = pd.read_csv('../files/credit_risk_data_v2.csv', low_memory=False)
df.info()