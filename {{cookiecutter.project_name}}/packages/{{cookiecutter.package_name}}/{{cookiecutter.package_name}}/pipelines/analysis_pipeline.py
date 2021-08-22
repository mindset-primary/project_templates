from sklearn.pipeline import Pipeline
from {{cookiecutter.package_name}}.config.config import config
from {{cookiecutter.package_name}}.processing import analyzers as analyze
from {{cookiecutter.package_name}}.config.logging_config import ProcessLogger

############################## ANALYSIS AND OUTPUT #########################
############################################################################

###
### DATA ANALYSIS
###


analysis_pipeline = Pipeline(
    [
        (
            "Fit logistic regression model.",
            analyze.LogisticRegressor(
                dependent_variable=config.logistic_regression_config.dependent_variable, 
                independent_variables=config.logistic_regression_config.independent_variables,
                export=True)
        ),
        (
            "Tabulate and test group differences",
            analyze.SeriesOfTabulations(
                dependent_variables=config.logistic_regression_config.dependent_variable,
                independent_variables=config.logistic_regression_config.independent_variables),
        ),
        (
            "Barchart",
            analyze.SeriesOfBinaryGraphs(
                dependent_variables=config.binary_graph_config.binary_graph_dependent_variables,
                independent_variables=config.binary_graph_config.binary_graph_independent_variables)
        ),
        (
            "Analysis pipeline Step N",
            print('Step N')
        )
    ]
)