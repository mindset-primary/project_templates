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
from {{cookiecutter.package_name}}.modeling_resources.tabulation.tabulation import tabulate_and_test
from {{cookiecutter.package_name}}.graphs.graphs import BarCharter

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

class SeriesOfTabulations(BaseEstimator, TransformerMixin):
    def __init__(self, dependent_variables=None, independent_variables=None):
        if not isinstance(dependent_variables, list):
            self.dependent_variables = [dependent_variables]
        else:
            self.dependent_variables = dependent_variables
        if not isinstance(independent_variables, list):
            self.independent_variables = [independent_variables]
        else:
            self.independent_variables = independent_variables

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame):

        X = X.copy()

        for dependent_variable in self.dependent_variables:
            for independent_variable in self.independent_variables:
                tabulate_and_test(
                    X, dependent_variable, independent_variable
                ).tab_test()

        return X

class SeriesOfBinaryGraphs(BaseEstimator, TransformerMixin):
    def __init__(self, dependent_variables=None, independent_variables=None):
        if not isinstance(dependent_variables, list):
            self.dependent_variables = [dependent_variables]
        else:
            self.dependent_variables = dependent_variables
        if not isinstance(independent_variables, list):
            self.independent_variables = [independent_variables]
        else:
            self.independent_variables = independent_variables

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame):

        X = X.copy()


        for variable in self.dependent_variables:
            for group_variable in self.independent_variables:
                test_graph = BarCharter(X, 'q23_1', 'q8', labels = {1: 'Male', 2: 'Female'}, stat_annotation='binary')
                test_graph.grouped_single_binary_chart().write_image(f"{config.OUTPUT_DIR}/graphical_output/{variable}_{group_variable}.png")

        return X

class SeriesOfOrdinalGraphs(BaseEstimator, TransformerMixin):
    def __init__(self, dependent_variables=None, independent_variables=None):
        if not isinstance(dependent_variables, list):
            self.dependent_variables = [dependent_variables]
        else:
            self.dependent_variables = dependent_variables
        if not isinstance(independent_variables, list):
            self.independent_variables = [independent_variables]
        else:
            self.independent_variables = independent_variables

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame):

        X = X.copy()


        for variable in self.dependent_variables:
            for group_variable in self.independent_variables:
                test_graph = BarCharter(X, variable, group_variable, labels={1: 'Male', 2: 'Female'}, stat_annotation='ordinal')
                test_graph = test_graph.grouped_barchart_ordinal(x_axis_labels = {1: 'Daily', 2: 'Weekly', 3: 'Monthly', 4: 'Quarterly', 5: 'Yearly', 6: 'Less than yearly'})
                test_graph.write_image(f"{config.OUTPUT_DIR}/graphical_output/{variable}_{group_variable}.png")

        return X