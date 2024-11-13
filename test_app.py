from dash import Dash, html
import os
import yaml

# Create a Dash app
app = Dash(__name__)
# Load configuration and calculate thresholds
with open("config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

# Verify if data is present
data_dir = config["data"]["directory"]
data_present = (
    "Data folder is empty" if not os.listdir(data_dir) else "Data loaded successfully"
)

# Define the app layout
app.layout = html.Div(
    [html.H1("Hello, Dash!"), html.P(data_present)]  # Show if data is present or not
)

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050)
