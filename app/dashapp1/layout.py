import dash_core_components as dcc
import dash_html_components as html

######################## START Paid Search Layout ########################
layout_paid_search =  html.Div([
    html.Div([
        # CC Header
        Header(),
        # Date Picker
        html.Div([
            dcc.DatePickerRange(
              id='my-date-picker-range-paid-search',
              min_date_allowed=dt(2018, 1, 1),
              max_date_allowed=df['Date'].max().to_pydatetime(),
              initial_visible_month=dt(current_year,df['Date'].max().to_pydatetime().month, 1),
              start_date=(df['Date'].max() - timedelta(6)).to_pydatetime(),
              end_date=df['Date'].max().to_pydatetime(),
            ),
            html.Div(id='output-container-date-picker-range-paid-search')
            ], className="row ", style={'marginTop': 30, 'marginBottom': 15}),
        # Header Bar
        html.Div([
          html.H6(["Paid Search"], className="gs-header gs-text-header padded",style={'marginTop': 15})
          ]),
        # Radio Button
        html.Div([
          dcc.RadioItems(
            options=[
                {'label': 'Condensed Data Table', 'value': 'Condensed'},
                {'label': 'Complete Data Table', 'value': 'Complete'},
            ], value='Condensed',
            labelStyle={'display': 'inline-block', 'width': '20%', 'margin':'auto', 'marginTop': 15, 'paddingLeft': 15},
            id='radio-button-paid-search'
            )]),
        # First Data Table
        html.Div([
            dash_table.DataTable(
                id='datatable-paid-search',
                columns=[{"name": i, "id": i, 'deletable': True} for i in dt_columns]
                + [{"name": j, "id": j, 'hidden': 'True'} for j in conditional_columns],
                editable=True,
                n_fixed_columns=2,
                style_table={'maxWidth': '1500px'},
                row_selectable="multi",
                selected_rows=[0],
                ),
            ], className=" twelve columns"),
        # Download Button
        html.Div([
          html.A(html.Button('Download Data', id='download-button'), id='download-link-paid-search-1')
          ]),
        # Second Data Table
        html.Div([
            dash_table.DataTable(
              id='datatable-paid-search-2',
              columns=[{"name": i, "id": i} for i in df_columns_calculated] +
              [{"name": k, "id": k, 'hidden': 'True'} for k in conditional_columns_calculated_calculated],
              editable=True,
              n_fixed_columns=1,
              css=[{'selector': '.dash-cell div.dash-cell-value', 'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'}],
              style_table={'maxWidth': '1500px'},
                ),
            ], className=" twelve columns"),
        # GRAPHS
        html.Div([
            html.Div([
              dcc.Graph(id='paid-search'),
              ], className=" twelve columns"
              )
            ], className="row ")
        ], className="subpage")
    ], className="page")
