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
                    text = self.group_distribution_binary_outcome()[self.output_variable].values,
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
                    text = self.group_distribution_binary_outcome()[self.output_variable].values,
                    textposition="inside",
                    marker={
                        "color": self.colors[color],
                        "line": {"color": "rgb(255, 255, 255)", "width": 2},
                    },
                )
            ),
            color += 1
            
        return go.Figure(data=data, layout=self.layout)