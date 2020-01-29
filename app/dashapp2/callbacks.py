from datetime import datetime as dt

import pandas_datareader as pdr
from dash.dependencies import Input
from dash.dependencies import Output
from app.models import ScrappedData, SelectedData
import pandas as pd
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

    @dashapp.callback( Output(component_id='my-div', component_property='children'),
                       [Input('my_input', 'value')])
    def get_input(input_value):
        return 'You\'ve entered "{}"'.format(input_value)


def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


def get_url(app, website_url, website_name):
    with app.app_context():
        main_list = []
        try:
            # Make the request and check object type
            r = requests.get(website_url)
            # Extract HTML from Response object and print
            html = r.text
            # Create a BeautifulSoup object from the HTML
            soup = BeautifulSoup(html, "html.parser")
            # Get the text out of the soup tag p and print it
            text = soup.get_text()
            text = text.split('\n')
            for t in text:
                if len(t) > 0:
                    tlist = t.split('END')
                    main_list.append(tlist)
            create_main_list(main_list, website_name)
            # create_dframe(main_list)
            return main_list
        except:
            pass



def read_ip_info(ip):
    reader = geoip2.database.Reader('./GeoLite2-City.mmdb')
    response = reader.city(ip)
    return [response.country.name, response.subdivisions.most_specific.name,
            response.city.name,
            response.postal.code, response.location.latitude,
            response.location.longitude
            ]


def create_main_list(llist, website_name):
    main_list = []
    for val in llist:
        combine = val[1:] + read_ip_info(val[0])
        v_info = ScrappedData.query.filter_by(unique_time=combine[2],
                                              website_name=website_name).first()
        if v_info is None:
            v_in = ScrappedData(browser=combine[0],
                                time=combine[1],
                                unique_time=combine[2],
                                ip_request=val[0],
                                country=combine[3],
                                region=combine[4],
                                city=combine[5],
                                zipcode=combine[6],
                                latitude=combine[7],
                                longitude=combine[8],
                                website_name=website_name)
            db.session.add(v_in)
            db.session.commit()
        main_list.append(combine)
    df = pd.DataFrame(main_list)
    return df

# def _datafarame():
