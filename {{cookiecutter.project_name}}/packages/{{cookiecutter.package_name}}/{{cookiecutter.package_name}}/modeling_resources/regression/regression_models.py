import os
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

from {{cookiecutter.package_name}}.regression.regression_resources import RegressionResourceRetainer
from {{cookiecutter.package_name}}.config.logging_config import ProcessLogger
from {{cookiecutter.package_name}}.config import config

 

class BinaryLogisticRegression(RegressionResourceRetainer):
    def __init__(self, dataframe, dependent_variable, independent_variables):
        super().__init__(dataframe, dependent_variable, independent_variables)
        self.model = None
        
    def fit_model(self):
        endogenous = self.dataframe[self.dependent_variable]
        exogenous = sm.add_constant(
            self.dataframe[self.independent_variables], prepend=False
        )

        self.model = sm.GLM(endogenous, exogenous, family=sm.families.Binomial()).fit()
        self.model_results = self.model.summary()