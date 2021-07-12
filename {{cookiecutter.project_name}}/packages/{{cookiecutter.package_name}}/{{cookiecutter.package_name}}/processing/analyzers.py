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


from {{cookiecutter.package_name}}.processing.data_management import export_artifact_excel
from {{cookiecutter.package_name}}.config.logging_config import ProcessLogger
from {{cookiecutter.package_name}}.config import config
import data_management

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


class BinaryLogisticRegression:
    '''
    Binary logistic regression (Binomial)
    
    Attributes:
        - dependent_variable: outcome variable (str) to predict
        - independent_variables (list): predictor variables
    '''
    def __init__(self, data, dependent_variable, independent_variables):
        self.dependent_variable = dependent_variable
        self.independent_variables = independent_variables
        self.data = data[
            [self.dependent_variable] + self.independent_variables
        ].replace({-1: np.NaN})

        self.model = None
        self.results = None

    def fit_model(self):
        endogenous = self.data[self.dependent_variable]
        exogenous = sm.add_constant(
            self.data[self.independent_variables], prepend=False
        )

        model = sm.GLM(endogenous, exogenous, family=sm.families.Binomial())
        results = model.fit()

        self.model = model
        self.results = results
        data_management.save_model(self.dependent_variable, self.results)

    def export_regression_results(self, file_name):
        writer = pd.ExcelWriter(
            f"./output/results/regression_output/{file_name}.xlsx", engine="xlsxwriter"
        )
        results_as_html = self.results.summary().tables[0].as_html()
        first = pd.read_html(results_as_html, index_col=0)[0]

        results_as_html = self.results.summary().tables[1].as_html()
        second = pd.read_html(results_as_html, header=0, index_col=0)[0]

        first.to_excel(writer)
        second.to_excel(writer, startrow=12)

        writer.save()

        beginningtex = """\\documentclass{report}
        \\usepackage{booktabs}
        \\begin{document}"""
        endtex = r"\end{document}"

        f = open(f"./output/results/regression_output/{file_name}.tex", "w")
        f.write(beginningtex)
        f.write(self.results.summary().as_latex())
        f.write(endtex)
        f.close()




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