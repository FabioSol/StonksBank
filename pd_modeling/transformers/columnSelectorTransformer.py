from typing import List
import pandas as pd
from sklearn.utils import resample


class ColumnSelectorTransformer:
    def __init__(self, columns: List[str]):
        self.columns = columns

    def transform(self, X: pd.DataFrame, y: pd.DataFrame = None) -> pd.DataFrame:
        return X.loc[:, self.columns]

    @staticmethod
    def clean(X: pd.DataFrame, y: pd.DataFrame = None, column_mean_sampling: str = '') -> pd.DataFrame:
        if column_mean_sampling != '':
            sampled_mean = int(X[column_mean_sampling].mean())
            X[column_mean_sampling].fillna(sampled_mean, inplace=True)
        X.dropna(inplace=True)
        return X

    @staticmethod
    def undersampling(X: pd.DataFrame, y: str):
        status_aggregation = (
                X.groupby(y).size().to_frame().rename(columns={0: "count"}) / len(X)
        )
        majority_class = X[X[y] == 0]
        minority_class = X[X[y] == 1]
        n_samples = len(minority_class)
        undersampled_majority = resample(majority_class,
                                         replace=False,
                                         n_samples=n_samples)
        undersampled_df = pd.concat([undersampled_majority, minority_class])
        return undersampled_df
    def fit(self, *args, **kwargs):
        return self

    def __str__(self) -> str:
        return f"ColumnSelectorTransformer({self.columns})"

    def __repr__(self) -> str:
        return f"ColumnSelectorTransformer({self.columns})"
