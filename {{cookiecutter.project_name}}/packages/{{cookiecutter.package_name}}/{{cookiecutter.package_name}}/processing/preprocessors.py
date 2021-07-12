from typing import List
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import mutual_info_classif
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import chi2
from sklearn.feature_selection import f_classif
from kmodes.kmodes import KModes

from {{cookiecutter.package_name}}.processing.data_management import export_artifact_excel
from {{cookiecutter.package_name}}.config.logging_config import ProcessLogger
from {{cookiecutter.package_name}}.config import config

ProcessLogger = ProcessLogger(__name__)


##
## PREPROCESSOR CLASS TEMPLATE
##

class PreprocessorName(BaseEstimator, TransformerMixin):
    ''' Placeholder description for preprocessor unit. '''
    def __init__(self):
        # YOUR CODE HERE
        return None

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        '''
        Method used for Sklearn class. May be left empty.
        '''
        return self

    def transform(self, X: pd.DataFrame, y: pd.Series = None):
        X = X.copy()
        # YOUR CODE HERE.

        return X

class ExtractSubsetVariables(BaseEstimator, TransformerMixin):
    def __init__(self, variables: List[str]):
        ''' Extracts selected variables only. '''

        if not isinstance(variables, list):
            raise ValueError("variables must be given as elements of list.")
        
        self.variables = variables

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame):
        
        X = X.copy()
        X = X[self.variables]

        return X

class ColumnRenamer(BaseEstimator, TransformerMixin):
    ''' Replaces variable names. '''

    def __init__(self, variables: dict):
        if not isinstance(variables, dict):
            raise ValueError('Variables and new names must be given as dict.')

        self.variables = variables

    def fit(self, X: pd.DataFrame, y: pd.Series=None):
        return self

    def transform(self, X: pd.DataFrame, y: pd.Series=None):
        X = X.copy()
        X.rename(columns=self.variables, inplace=True)

        return X

class CategoricalRecoder(BaseEstimator, TransformerMixin):
    ''' Recodes categorical variables into numerical. '''

    def __init__(self, variables: List[str], value_labels: dict):

        if not isinstance(variables, list):
            raise ValueError('variables must be given as elements of list.')

        self.variables = variables
        self.value_labels = value_labels

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        # Sklearn BaseEstimator w. pipeline requires this method.
        # Ignore this method unless there is a reason.
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()
        for variable in self.variables:
            X[variable] = X[variable].map(self.value_labels)

        return X


class NormalizeDateVariables(BaseEstimator, TransformerMixin):
    def __init__(self, variables: List[str]):
        ''' Extracts selected variables only. '''

        if not isinstance(variables, list):
            raise ValueError("variables must be given as elements of list.")
        
        self.variables = variables

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame):
        
        X = X.copy()

        for date_variable in self.variables:
            X[date_variable] = X[date_variable].dt.normalize()

        return X