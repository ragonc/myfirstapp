import dash
import dash_html_components as html

app = dash.Dash()
server = app.server
app.layout = html.Div(["Hi. I am your first dash app"])

if __name__ == '__main__':
app.run_server(
