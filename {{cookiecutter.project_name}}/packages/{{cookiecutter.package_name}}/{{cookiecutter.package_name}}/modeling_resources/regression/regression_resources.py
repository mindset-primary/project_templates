import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

import os  

from {{cookiecutter.package_name}}.config.logging_config import ProcessLogger
from {{cookiecutter.package_name}}.config import config


class RegressionResourceRetainer:
    def __init__(self, dataframe, dependent_variable, independent_variables):
        
        # Input resources
        self.dependent_variable = dependent_variable
        self.independent_variables = independent_variables
        self.dataframe = dataframe[[self.dependent_variable] + self.independent_variables]
        
        # Output resources
        self.model_results = None
        
    def save_model(self):
        '''
        Serializes model and stores as .PKL file.
        '''
        if self.model!=None:
            self.model.save(f"{config.OUTPUT_DIR}/regression_output/{self.dependent_variable}.pkl")
            
        else:
            print("No fitted model to save.")

        return None
    
    def export_model_results(self):
        '''
        This method requires that you have installed LaTeX on your computer.
        Download and install from: https://miktex.org/download
        Outputs: model_results as .xlsx and latex as .pdf
        '''
        writer = pd.ExcelWriter(
            f"{config.OUTPUT_DIR}/regression_output/{self.dependent_variable}.xlsx", engine="xlsxwriter"
        )
        results_as_html = self.model_results.tables[0].as_html()
        first = pd.read_html(results_as_html, index_col=0)[0]

        results_as_html = self.model_results.tables[1].as_html()
        second = pd.read_html(results_as_html, header=0, index_col=0)[0]

        first.to_excel(writer)
        second.to_excel(writer, startrow=12)

        writer.save()

        beginningtex = """\\documentclass{report}
        \\usepackage{booktabs}
        \\begin{document}"""
        endtex = r"\end{document}"

        f = open(f"{config.OUTPUT_DIR}/regression_output/{self.dependent_variable}.tex", "w")
        f.write(beginningtex)
        f.write(self.model_results.as_latex())
        f.write(endtex)
        f.close()
        
        #os.system(f"pdflatex {config.OUTPUT_DIR}/regression_output/{self.dependent_variable}.tex")
        os.system(f"pdflatex -output-directory {config.OUTPUT_DIR}/regression_output/ {config.OUTPUT_DIR}/regression_output/{self.dependent_variable}.tex")
        os.remove(f"{config.OUTPUT_DIR}/regression_output/{self.dependent_variable}.aux")
        os.remove(f"{config.OUTPUT_DIR}/regression_output/{self.dependent_variable}.tex")
        os.remove(f"{config.OUTPUT_DIR}/regression_output/{self.dependent_variable}.log")