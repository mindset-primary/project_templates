import numpy as np
import pandas as pd
import plotly
import plotly.graph_objs as go

from scipy.stats import chi2_contingency, kruskal

COLORS = ["#F58F86", "#8DD4DD", "#BA98BB", "#F6A3B1", "#EFF0A9", "#FBBDA6"] # MOVE THIS TO CONFIG

class ChartResource:
    '''
    ChartResource class is used as a helper class for BarCharter class.
    It processes data for use in BarCharter class by:
        - Setting standard layout / changing layout.
        - Producing correct data shape.
        - Labelling data.
        - Statistically testing for annotation in BarCharter graph object.
    '''
    
    def __init__(self, dataframe, output_variable, group_variable, labels=None):
        self.dataframe = dataframe
        self.output_variable = output_variable
        self.group_variable = group_variable
        self.labels = labels
        self.colors = COLORS
        
        self.layout = go.Layout(
            template="plotly_white",
            autosize=False,
            bargap=0.15,
            font={"family": "Raleway", "size": 15},
            height=400 * 2,
            legend={"orientation": "v", "yanchor": "top"},
            margin={
                "r": 0,
                # 't': 20,
                "b": 20,
                "l": 10,
            },
            title={
                "text": None,
                "y": 0.9,
                "x": 0.5,
                "xanchor": "center",
                "yanchor": "bottom",
            },
            showlegend=False,
            width=380 * 2,
            xaxis={
                "title": None,
                "autorange": True,
                "showline": True,
                "type": "category",
                "title": {
                    #"text": f"<i>N={str(dataframe[variable].count())} {test_annotation}</i> ",
                    "text": f"<i>N={str(self.dataframe[self.output_variable].count())}</i> ",
                    "standoff": 10,
                    "font": {"size": 12},
                },
            },
            yaxis={
                "autorange": False,
                "range": [0, 100], # for percentage use (0-100%)
                "showgrid": True,
                "showline": True,
                "title": "Percentage of responses",
                "type": "linear",
                "zeroline": True,
            },
        )
        
    def label_variables(self, variables_to_label):
        pass
        
    def group_distribution_binary_outcome(self):
        """
        Helper function for "grouped_single_binary_chart".
        Use for graphing positive outcome only.
        
        Assumes binary output_variable (ex. yes(1), or no(0))
        Creates frequency table of output_variable, grouped by group_variable.
        Keeps only positive outcome values (1).

        """
        _table = pd.DataFrame(
            self.dataframe.groupby(self.group_variable)[self.output_variable]
            .value_counts(normalize=True)
            .mul(100)
            .round(1)
        )
        table = _table[_table.index.get_level_values(1) == 1].reset_index(
            level=1, drop=True
        )

        return table
    
    def annotate_stat(self, binary=False, ordinal=False):
        if binary == True:
            '''
            Runs a Chi2 test of significance.
            Returns string including Chi2 stat and P-value.
            '''
            dataframe_ = self.dataframe.dropna(subset=[self.output_variable])
            stat, p, dof, expected = chi2_contingency(
                pd.crosstab(dataframe_[self.group_variable], self.dataframe[self.output_variable])
            )

            if p < 0.05:
                p_sig = "p<0.05 (statistically significant)"
            else:
                p_sig = "p>0.05 (not statistically significant)"

            return f"N={dataframe_[self.output_variable].count()} | [Chi^2={round(stat,4)}, {p_sig}]"
        
        elif ordinal == True:
            '''
            Runs a Kruskal-Wallis test of significance.
            Returns string including H stat and P-value.
            '''
            dataframe_ = self.dataframe.dropna(subset=[self.output_variable])
            kruskal_test = kruskal(
                *[group[self.output_variable].values for name, group in dataframe_.groupby(self.group_variable)]
            )
            p = kruskal_test[1]
            stat = kruskal_test[0]

            if p < 0.05:
                p_sig = "p<0.05 (statistically significant)"
            else:
                p_sig = "p>0.05 (not statistically significant)"

            return f"N={dataframe_[self.output_variable].count()} | H={round(stat,4)}, {p_sig}"
        
        else:
            print('No statistical test specified. Returning N (count)')
            dataframe_ = self.dataframe.dropna(subset=[self.output_variable])
            return f"N={dataframe_[self.output_variable].count()}"

            