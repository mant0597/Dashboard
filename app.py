import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
d = pd.read_csv('C:\\Users\\maida\\Downloads\\archive (1)\\Groceries_dataset.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Grocery Purchase Analysis"),

    dcc.Graph(
        id='purchase-frequency',
        figure={
            'data': [],
            'layout': {'title': 'Purchase Frequency Over Time of Grocery'}
        }
    ),

    dcc.Dropdown(
        id='graph-type-dropdown',
        options=[
            {'label': 'Bar Chart', 'value': 'bar'},
            {'label': 'Line Chart', 'value': 'line'},
            {'label': 'Scatter Chart', 'value': 'scatter'},
            {'label': 'Pie Chart', 'value': 'pie'},
        ],
        value='bar',
        multi=False,
        style={'width': '40%'}
    ),

    dcc.Graph(
        id='purchase-items',
        figure={
            'data': [],
            'layout': {'title': 'Top Purchased Items'}
        }
    ),
])

@app.callback(
    Output('purchase-items', 'figure'),
    [Input('graph-type-dropdown', 'value')]
)
def update_bar_graph(graph_type):
    top_items = d['itemDescription'].value_counts().head(10)
    graph_title = 'Top Purchased Items'

    if graph_type == 'bar':
        fig = {
            'data': [
                {'x': top_items.index, 'y': top_items.values, 'type': 'bar', 'name': graph_title, 'color': 'blue'},
            ],
            'layout': {'title': f'{graph_title}'}
        }
    elif graph_type == 'line':
        fig = {
            'data': [
                {'x': top_items.index, 'y': top_items.values, 'type': 'line', 'name': graph_title},
            ],
            'layout': {'title': f'{graph_title}'}
        }
    elif graph_type == 'scatter':
        fig = {
            'data': [
                {'x': top_items.index, 'y': top_items.values, 'mode': 'markers', 'type': 'scatter', 'name': graph_title},
            ],
            'layout': {'title': f'{graph_title}'}
        }
    else:
        fig = {
            'data': [
                {'labels': top_items.index, 'values': top_items.values, 'type': 'pie', 'name': graph_title},
            ],
            'layout': {'title': f'{graph_title}'}
        }

    return fig

@app.callback(
    Output('purchase-frequency', 'figure'),
    [Input('graph-type-dropdown', 'value')]
)
def update_purchase_frequency(graph_type):
    purchase_counts = d['Date'].value_counts().sort_index()

    if graph_type == 'bar':
        fig = {
            'data': [
                {'x': purchase_counts.index, 'y': purchase_counts.values, 'type': 'bar', 'name': 'Purchase Frequency', 'color': 'green'},
            ],
            'layout': {'title': 'Purchase Frequency Over Time'}
        }
    elif graph_type == 'line':
        fig = {
            'data': [
                {'x': purchase_counts.index, 'y': purchase_counts.values, 'type': 'line', 'name': 'Purchase Frequency'},
            ],
            'layout': {'title': 'Purchase Frequency Over Time'}
        }
    elif graph_type == 'scatter':
        fig = {
            'data': [
                {'x': purchase_counts.index, 'y': purchase_counts.values, 'mode': 'markers', 'type': 'scatter', 'name': 'Purchase Frequency'},
            ],
            'layout': {'title': 'Purchase Frequency Over Time'}
        }
    else:
        fig = {
            'data': [
                {'labels': purchase_counts.index, 'values': purchase_counts.values, 'type': 'pie', 'name': 'Purchase Frequency'},
            ],
            'layout': {'title': 'Purchase Frequency Over Time'}
        }

    return fig
if __name__ == '__main__':
    app.run_server(debug=True)
