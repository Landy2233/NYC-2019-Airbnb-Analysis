# dash_app.py

import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load cleaned data
df = pd.read_csv('cleaned_airbnb_data.csv')

# Create Dash app
app = dash.Dash(__name__)

# Dropdown options
boroughs = df['neighbourhood_group'].unique()

# Layout
app.layout = html.Div([
    html.H1("NYC Airbnb 2019 Price Explorer", style={'textAlign': 'center'}),

    dcc.Dropdown(
        id='borough',
        options=[{'label': b, 'value': b} for b in boroughs],
        value='Manhattan',
        style={'width': '50%'}
    ),

    dcc.Graph(id='price-boxplot'),

    html.Div(id='summary-stats', style={'padding': '20px'})
])

# Callback for graph and stats
@app.callback(
    [dash.dependencies.Output('price-boxplot', 'figure'),
     dash.dependencies.Output('summary-stats', 'children')],
    [dash.dependencies.Input('borough', 'value')]
)
def update_dashboard(selected_borough):
    filtered_df = df[df['neighbourhood_group'] == selected_borough]

    fig = px.box(filtered_df, x='room_type', y='price',
                 title=f"Price by Room Type in {selected_borough}",
                 color='room_type')

    avg_price = round(filtered_df['price'].mean(), 2)
    total_listings = filtered_df.shape[0]

    summary = f"Average Price: ${avg_price} | Total Listings: {total_listings}"

    return fig, summary

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
