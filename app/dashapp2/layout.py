import dash_core_components as dcc
import dash_html_components as html

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

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
    dcc.Graph(id='my-graph')
], style={'width': '500'})
