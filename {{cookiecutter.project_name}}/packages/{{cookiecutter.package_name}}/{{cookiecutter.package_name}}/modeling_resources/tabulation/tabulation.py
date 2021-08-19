import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency, kruskal

from {{cookiecutter.package_name}}.config import config


class tabulate_and_test:
    def __init__(self, data, output_var, group_var):
        self.data = data
        self.output_var = output_var
        self.group_var = group_var

    def tab_test(self):
        groups = {}

        for group in sorted(self.data[self.group_var].unique()):
            # REPLACING -1 with NAN: BUT SHOULD BE DONE IN PRE-PROCESSING
            groups[f"{self.output_var}_{self.group_var}={group}"] = (
                self.data[self.data[self.group_var] == group]
                .replace({-1: np.NaN})[self.output_var]
                .value_counts(normalize=True)
                .mul(100)
                .round(1)
                .sort_index()
            )

        count = self.data.groupby(self.group_var)[self.output_var].value_counts()
        perc = self.data.groupby(self.group_var)[self.output_var].value_counts(
            normalize=True
        )

        writer = pd.ExcelWriter(
            f"{config.OUTPUT_DIR}/tabular_output/{self.output_var}_{self.group_var}.xlsx",
            engine="xlsxwriter",
        )
        stat, p, dof, expected = chi2_contingency(
            pd.crosstab(self.data[self.group_var], self.data[self.output_var])
        )
        test = (
            pd.DataFrame([stat, p, dof])
            .T.rename(columns={0: "Stat (Chi2)", 1: "p", 2: "DoF"})
            .rename(index={0: "Pearson's Chi2 contingency"})
        )
        test.to_excel(writer)

        kruskal_test = kruskal(
            *[
                group[self.output_var].values
                for name, group in self.data.groupby(self.group_var)
            ]
        )
        kruskal_test = pd.DataFrame([kruskal_test[0], kruskal_test[1]]).T.rename(
            columns={0: "Stat (H)", 1: "p"}, index={0: "Kruskal-Wallis"}
        )
        kruskal_test.to_excel(writer, startrow=3)

        table_out = pd.concat([count, perc], axis=1)
        table_out.columns = ["count", "perc"]
        table_out.to_excel(writer, startrow=6)
        writer.save()

        return groups