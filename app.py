import dash
from dash import dcc,html
import pandas as pd
from dash.dependencies import Input, Output

data = pd.read_csv("Finalset.csv")

xdata = list(range(1, data.shape[0]))
input_columns = { "MLD" : "Flow-Rate", "IN_BOD" : "Input BOD","IN_TSS" : "Input TSS","IN_PH" : "Input PH","IN_COD" : "Input COD"}
output_columns = { "OUT_BOD" : "Output BOD","OUT_TSS" : "Output TSS","OUT_PH" : "Output PH","OUT_COD" : "Output COD","OUT_DO" : "Output DO" }
app = dash.Dash(__name__)
app.title = "Bharwarav1.0"
server = app.server
app.layout = html.Div(
    children= [
        html.Div(children="Input-Parameter", className="Input-title"),
        dcc.Dropdown(
            id="input_param",
            options = [
                {"label" : input_val , "value" : input_key }
                for input_key,input_val in input_columns.items()
            ],
            value = "MLD",
            clearable = False,
            className = "dropdown"
        ),
        html.Div(children="Output-Parameter", className="Output-title"),
        dcc.Dropdown(
            id="output_param",
            options = [
                {"label" : output_val , "value" : output_key }
                for output_key,output_val in output_columns.items()
            ],
            value = "OUT_BOD",
            clearable = False,
            className = "dropdown"
        ),
        html.Div(
            children=[
                #inputgraph
                html.Div(
                    children=dcc.Graph(id="input_graph",config={"displayModeBar":False},),
                    className="graphcard",
                ),
                #output graph
                html.Div(
                    children=dcc.Graph(id="output_graph", config={"displayModeBar":False},),
                    className="graphcard",
                )
            ]
        )
    ]
)

@app.callback([Output("input_graph","figure"), Output("output_graph", "figure")],
              [Input("input_param","value"), Input("output_param", "value")],)
def plot_graphs(input_cols, output_cols):

    input_figure = {
        "data" : [
            {
                "x" : xdata,
                "y" : data[input_cols],
                "type" : "line",
            },
        ],
        "layout" : {
            "title" : {
                "text" : input_cols + " Graph",
                "x" : 0.05,
                "xanchor" : "left",
            },
        "xaxis" : {"fixedrange":True},
        "yaxis" : {"fixedrange" : True},
        "colorway" : ["#17887"],
        },
    }
    output_figure = {
        "data" : [
            {
                "x" : xdata,
                "y" : data[output_cols],
                "type" : "line",
            },
        ],
        "layout" : {
            "title" : {
                "text" : output_cols + " Graph",
                "x" : 0.05,
                "xanchor" : "left",
            },
        "xaxis" : {"fixedrange":True},
        "yaxis" : {"fixedrange" : True},
        "colorway" : ["#17887"],
        },
    }
    return input_figure, output_figure

if __name__ == "__main__":
    app.run_server(debug = True)
