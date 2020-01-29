import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# Gapminder dataset GAPMINDER.ORG, CC-BY LICENSE
url = "https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv"
df = pd.read_csv(url)
df = df.rename(index=str, columns={"pop": "population",
                                   "lifeExp": "life_expectancy",
                                   "gdpPercap": "GDP_per_capita"})

layout = html.Div([
    html.Div(style={'backgroundColor': colors['background']}, children=[
        html.H1(
            children='Hello Dash',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),
        html.Div(children='Dash: A web application framework for Python.',
                 style={
                     'textAlign': 'center',
                     'color': colors['text']
                 }),
        dcc.Graph(
            id='Graph1',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar',
                     'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar',
                     'name': u'Montréal'},
                ],
                'layout': {
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                    }
                }
            }
        )
    ]),
    html.H1('Stock Tickers'),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Coke', 'value': 'COKE'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='COKE'
    ),
    dcc.Graph(id='my-graph'),
    dcc.Input(
        className="form-control",
        id='my_input',
        placeholder='Enter a value...',
        type='text',
        value=''
    ),
    html.Div(id='my-div'),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': i, 'value': i} for i in df.country.unique()],
        multi=True,
        value=['Australia']
    ),

    dcc.Graph(id='timeseries-graph')
], style={'width': '500'}, className="container", )
