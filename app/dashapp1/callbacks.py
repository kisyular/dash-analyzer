from datetime import datetime as dt

import pandas_datareader as pdr
import requests
from dash.dependencies import Input
from dash.dependencies import Output
from bs4 import BeautifulSoup
from app import db
from app.models import ScrappedData, SelectedData
import pandas as pd
from flask import current_app
import geoip2.database
import threading


def register_callbacks(dashapp):
    @dashapp.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
    def update_graph(selected_dropdown_value):
        df = pdr.get_data_yahoo(selected_dropdown_value, start=dt(2017, 1, 1), end=dt.now())
        return {
            'data': [{
                'x': df.index,
                'y': df.Close
            }],
            'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
        }

#
# def get_datasets():
#     """Return previews of all CSVs saved in /data directory."""
#
#     arr = ['This is an example Plot.ly Dash App.']
#     for index, csv in enumerate(data_filepath):
#         df = pd.read_csv(data_filepath[index]).head(10)
#         table_preview = dash_table.DataTable(
#             id='table_' + str(index),
#             columns=[{"name": i, "id": i} for i in df.columns],
#             data=df.to_dict("rows"),
#             sort_action="native",
#             sort_mode='single'
#         )
#         arr.append(table_preview)
#     return arr
#
#
#
# def run_test():
#     website_url = 'https://kisyula.com/gud.txt'
#     website_name = 'Rellika'
#     threading.Thread(target=get_url,
#                      args=(current_app._get_current_object(), website_url,
#                            website_name)).start()

