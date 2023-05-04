from dash import Dash, dcc, html
app =  Dash()
app.layout = html.Div([
    html.H1('Hola')
])

if __name__ == '__main__':
    app.run_server()