from datetime import datetime as dt

import pandas_datareader as pdr
from dash.dependencies import Input
from dash.dependencies import Output
from app.models import ScrappedData, SelectedData
import pandas as pd
import geoip2.database
import threading

def register_callbacks(dashapp):
    # Gapminder dataset GAPMINDER.ORG, CC-BY LICENSE
    url = "https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv"
    df = pd.read_csv(url)
    df = df.rename(index=str, columns={"pop": "population",
                                       "lifeExp": "life_expectancy",
                                       "gdpPercap": "GDP_per_capita"})
    @dashapp.callback(Output('my-graph', 'figure'),
                      [Input('my-dropdown', 'value')])
    def update_graph(selected_dropdown_value):
        df = pdr.get_data_yahoo(selected_dropdown_value, start=dt(2017, 1, 1),
                                end=dt.now())
        return {
            'data': [{
                'x': df.index,
                'y': df.Close
            }],
            'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
        }

    @dashapp.callback(
        Output(component_id='my-div', component_property='children'),
        [Input('my_input', 'value')])
    def get_input(input_value):
        return 'You\'ve entered "{}"'.format(input_value)

    @dashapp.callback(
        Output('timeseries-graph', 'figure'),
        [Input('country-dropdown', 'value')])
    def update_graph(country_values):
        dff = df.loc[df['country'].isin(country_values)]

        return {
            'data': [go.Scatter(
                x=dff[dff['country'] == country]['year'],
                y=dff[dff['country'] == country]['GDP_per_capita'],
                text="Continent: " +
                     f"{dff[dff['country'] == country]['continent'].unique()[0]}",
                mode='lines+markers',
                name=country,
                marker={
                    'size': 15,
                    'opacity': 0.5,
                    'line': {'width': 0.5, 'color': 'white'}
                }
            ) for country in dff.country.unique()],
            'layout': go.Layout(
                title="GDP over time, by country",
                xaxis={'title': 'Year'},
                yaxis={'title': 'GDP Per Capita'},
                margin={'l': 60, 'b': 50, 't': 80, 'r': 0},
                hovermode='closest'
            )
        }


# def get_url():
#     web = SelectedData.query.order_by(SelectedData.timestamp.desc()).first()
#     website_name = 'web.website_name'
#     website_url = 'https://kisyula.com/gud.txt'
#     main_list = []
#     try:
#         # Make the request and check object type
#         r = requests.get(website_url)
#         # Extract HTML from Response object and print
#         html = r.text
#         # Create a BeautifulSoup object from the HTML
#         soup = BeautifulSoup(html, "html.parser")
#         # Get the text out of the soup tag p and print it
#         text = soup.get_text()
#         text = text.split('\n')
#         for t in text:
#             if len(t) > 0:
#                 tlist = t.split('END')
#                 combine = tlist[1:] + read_ip_info(tlist[0])
#                 main_list.append(combine)
#         df = pd.DataFrame(main_list)
#         print(df)
#         return df
#     except:
#         pass
#
#
# def read_ip_info(ip):
#     reader = geoip2.database.Reader('./GeoLite2-City.mmdb')
#     response = reader.city(ip)
#     return [response.country.name, response.subdivisions.most_specific.name,
#             response.city.name,
#             response.postal.code, response.location.latitude,
#             response.location.longitude
#             ]
