import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import psutil
from datetime import datetime
import dash_bootstrap_components as dbc
import numpy as np

# Interface name (change accordingly)
INTERFACE = 'Wi-Fi'  # e.g., 'Wi-Fi' for Windows

# Initial values
old_stats = psutil.net_io_counters(pernic=True)[INTERFACE]
old_sent = old_stats.bytes_sent
old_recv = old_stats.bytes_recv

# Initialize app with Bootstrap for styling
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = dbc.Container([ 
    dbc.Row([ 
        dbc.Col(html.H1("Wi-Fi Network Monitor", className='text-center text-primary mb-4'), width=12) 
    ]), 

    dbc.Row([ 
        dbc.Col(dcc.Graph(id='live-graph', animate=True), width=12) 
    ]), 

    dcc.Interval( 
        id='graph-update', 
        interval=500,  # 500 ms = 0.5 second for smoother updates
        n_intervals=0 
    )
], fluid=True)

# Store data
time_list = []
upload_speed_list = []
download_speed_list = []

def smooth_data(data, window_size=3):
    """ Smooth the data using a moving average filter. """
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

@app.callback( 
    Output('live-graph', 'figure'), 
    [Input('graph-update', 'n_intervals')] 
) 
def update_graph(n): 
    global old_sent, old_recv

    stats = psutil.net_io_counters(pernic=True)[INTERFACE]
    new_sent = stats.bytes_sent
    new_recv = stats.bytes_recv

    # Calculate upload/download speeds
    upload_speed = (new_sent - old_sent) * 8 / 1024  # Kbps
    download_speed = (new_recv - old_recv) * 8 / 1024  # Kbps

    old_sent, old_recv = new_sent, new_recv

    # Save to lists
    current_time = datetime.now().strftime('%H:%M:%S')
    time_list.append(current_time)
    upload_speed_list.append(upload_speed)
    download_speed_list.append(download_speed)

    # Keep only the last 30 data points (adjustable)
    time_trim = time_list[-30:]
    upload_trim = upload_speed_list[-30:]
    download_trim = download_speed_list[-30:]

    # Smooth data (apply moving average)
    smoothed_upload = smooth_data(upload_trim)
    smoothed_download = smooth_data(download_trim)

    # Adjust the x-axis range to be static for the last few seconds
    time_range = [time_trim[0], time_trim[-1]]

    # Limit the x-axis to display the last 30 seconds (time_list is trimmed to the last 30 values)
    figure = { 
        'data': [
            {'x': time_trim[1:], 'y': smoothed_upload, 'type': 'line', 'name': 'Upload (Kbps)', 'line': {'color': 'red'}},
            {'x': time_trim[1:], 'y': smoothed_download, 'type': 'line', 'name': 'Download (Kbps)', 'line': {'color': 'green'}}
        ], 
        'layout': { 
            'title': f'Live Wi-Fi Monitoring - {INTERFACE}', 
            'xaxis': { 
                'title': 'Time', 
                'range': time_range,  # Keep the x-axis static
                'tickangle': -45,  # Tilt time labels if necessary
                'showgrid': True,
                'gridcolor': '#444444',
            }, 
            'yaxis': { 
                'title': 'Speed (Kbps)', 
                'showgrid': True, 
                'gridcolor': '#444444', 
            },
            'paper_bgcolor': '#303030', 
            'plot_bgcolor': '#303030', 
            'font': {'color': 'white'}
        } 
    }

    return figure

if __name__ == '__main__': 
    app.run(debug=True)
