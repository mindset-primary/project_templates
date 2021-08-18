from typing import List
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import mutual_info_classif
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import chi2
from sklearn.feature_selection import f_classif
from kmodes.kmodes import KModes

from {{cookiecutter.package_name}}.modeling_resources.regression.regression_models import BinaryLogisticRegression

from {{cookiecutter.package_name}}.processing.data_management import export_artifact_excel
from {{cookiecutter.package_name}}.config.logging_config import ProcessLogger
from {{cookiecutter.package_name}}.config import config

ProcessLogger = ProcessLogger(__name__)


##
## ANALYZER CLASS TEMPLATE
##

class PreprocessorName(BaseEstimator, TransformerMixin):
    ''' Placeholder description for analyzing unit. '''
    def __init__(self):
        return None

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame, y: pd.Series = None):
        X = X.copy()
        # YOUR CODE HERE.

        return X

########################################################
#                                                      #
#                   DIMENSIONALITY REDUCTION           #
#                                                      #
########################################################



#######################################################
##                  FULTER METHODS                   ##
#######################################################  
##
##
##
##
##
##



#######################################################
##                  WRAPPER METHODS                  ##
#######################################################  
##
##
##
##
##
##



#######################################################
##                  EMBEDDED METHODS                 ##
#######################################################  
##
##
##
##
##
##





#######################################################
##                  MISC. METHODS                    ##
#######################################################  
##
##
##
##
##
##

class LogisticRegressor(BaseEstimator, TransformerMixin):
    ''' Placeholder description for analyzing unit. '''
    def __init__(self, dependent_variable, independent_variables, export=False):
        self.dependent_variable = dependent_variable
        self.independent_variables = independent_variables
        self.export = export

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame, y: pd.Series = None):
        X = X.copy()
        # YOUR CODE HERE.

        if self.export==False:
            logreg = BinaryLogisticRegression(X, self.dependent_variable, self.independent_variables)
            logreg.fit_model()
        else:
            logreg = BinaryLogisticRegression(X, self.dependent_variable, self.independent_variables)
            logreg.fit_model()
            logreg.save_model()
            logreg.export_model_results()

        ProcessLogger.processLogger.info(f" Logistic model fitted: {logreg.model!=False}")

        return X