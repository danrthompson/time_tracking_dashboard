import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html

# Load data from CSV
df = pd.read_csv("toggl_data.csv")

# Calculate total duration per category
category_durations = df.groupby("category")["duration"].sum()

# Create a bar plot for total duration per category
category_bar = go.Bar(
    x=category_durations.index,
    y=category_durations.values,
    name="Total duration per category",
)

# Calculate total duration per day of the week
day_durations = df.groupby("day_of_week")["duration"].sum()

# Create a line plot for total duration per day of the week
day_line = go.Line(
    x=day_durations.index, y=day_durations.values, name="Total duration per day of week"
)

# Create a Dash app
app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Time tracking dashboard"),
        dcc.Graph(
            id="category-graph",
            figure={
                "data": [category_bar],
                "layout": go.Layout(title="Total duration per category"),
            },
        ),
        dcc.Graph(
            id="day-graph",
            figure={
                "data": [day_line],
                "layout": go.Layout(title="Total duration per day of week"),
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
