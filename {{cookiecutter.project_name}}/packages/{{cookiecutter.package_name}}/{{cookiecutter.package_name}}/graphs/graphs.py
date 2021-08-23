import numpy as np
import pandas as pd
import plotly
import plotly.graph_objs as go

from {{cookiecutter.package_name}}.graphs.graph_resources import ChartResource

class BarCharter(ChartResource):
    def __init__(self, dataframe, output_variable, group_variable, labels, stat_annotation=None):
        super().__init__(dataframe, output_variable, group_variable, labels)
        if stat_annotation=='binary':
            #print(self.annotate_stat(binary=True))
            self.layout['xaxis']['title']['text'] = self.annotate_stat(binary=True)

    def grouped_single_binary_chart(self):
        """
        Used for graphing positive responses of grouped binary variable.
        """
        color = 0
        data = []

        if self.labels is None:
            data.append(
                go.Bar(
                    x = self.group_distribution_binary_outcome()[self.output_variable].index,
                    y = self.group_distribution_binary_outcome()[self.output_variable].values,
                    text = self.group_distribution_binary_outcome()[self.output_variable].transform(lambda x: "{:,.1%}".format(x)).values,
                    textposition="inside",
                    marker={
                        "color": self.colors[color],
                        "line": {
                            "color": "rgb(255, 255, 255)",
                            "width": 2,
                        },
                    },
                )
            ),
        else:
            data.append(
                go.Bar(
                    x =self.group_distribution_binary_outcome()[self.output_variable].rename(index=self.labels).index,
                    y = self.group_distribution_binary_outcome()[self.output_variable].values,
                    text = self.group_distribution_binary_outcome()[self.output_variable].transform(lambda x: "{:,.1%}".format(x)).values,
                    textposition="inside",
                    marker={
                        "color": self.colors[color],
                        "line": {"color": "rgb(255, 255, 255)", "width": 2},
                    },
                )
            ),
            color += 1
            
        return go.Figure(data=data, layout=self.layout)
    def grouped_barchart_ordinal(self, x_axis_labels=None):
        """
        Used for graphing positive responses of grouped ordinal variable.
        """
        color = 0
        data = []
        
        _table = self.group_distribution_ordinal_outcome()
        if self.labels is not None:
            _table = (
                self.dataframe.replace({-1: np.NaN})
                .groupby(self.group_variable)[self.output_variable]
                .value_counts(normalize=True)
                .round(4)
                .sort_index()
                .rename(index=self.labels, level=0))
            if x_axis_labels!=None:
                _table.rename(x_axis_labels, inplace=True)
            
        for group, distribution in _table.groupby(level=0):
            data.append(
                go.Bar(
                    x=distribution.index.get_level_values(1),
                    y=distribution.values,
                    text=distribution.transform(lambda x: "{:,.1%}".format(x)).values,
                    textposition="inside",
                    marker={
                        "color": self.colors[color],
                        "line": {
                            "color": "rgb(255, 255, 255)",
                            "width": 2,
                        },
                    },
                    name=group,
                )
            ),
            color += 1
        
        return go.Figure(data=data, layout=self.layout)