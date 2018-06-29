import os
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, Event

from components import Column, Header, Row
import config
from auth import auth
from utils import StaticUrlPath

root = '/app/lib/PWitsml'
classpath = root + '/activation.jar;' + \
            root + '/javax.mail.jar;' + \
            root + '/jwitsml-1.0.jar;' + \
            root + '/jdom.jar;' + \
            root + '/axis-1.4.jar;' + \
            root + '/commons-discovery-0.5.jar;' + \
            root + '/commons-logging-1.2.jar;' + \
            root + '/wsdl4j-1.5.2.jar;' + \
            root + '/jaxrpc-api.jar;'
os.environ['CLASSPATH'] = classpath
from jnius import autoclass  # set CLASSPATH before import jnius


# Test 1: Call java.lang.String Class
String = autoclass('java.lang.String')
string_1 = String('Hello World.')

System = autoclass('java.lang.System')
System.out.println(string_1)

# Test 2: Call Capbilities Class from jwitsml(http://jwitsml.org/javadoc/index.html)
Capbilities = autoclass('org.jwitsml.Capabilities')
WitsmlVersion = autoclass('org.jwitsml.WitsmlVersion')

username = "Test"
version = WitsmlVersion.VERSION_1_3_1
clientCapabilities = Capbilities(version, username,
                                 String('abc'),
                                 String('123-456-7890'),
                                 String('WV'),
                                 String('WV'),
                                 String('WV'),
                                 String('1.0'))

version = clientCapabilities.getWitsmlVersion()
System = autoclass('java.lang.System')
System.out.println(version)


app = dash.Dash(__name__, static_folder='static')
auth(app)

server = app.server 

app.layout = html.Div([
    html.Link(href='/static/stylesheet.css', rel='stylesheet'),
    html.Div(
        style={'height': '70px',
               'borderBottom': 'thin lightgrey solid'},
        children=[
            html.H3('Pyjnius Test',
                    style={'color': '#506784',
                           'display': 'inline-block'}
                    )
        ]
    ),

    html.Div(
        style={'height': '70px',
               'borderBottom': 'thin lightgrey solid'},
        children=[
            html.H3('The jwitsml version is {}'.format(version),
                    style={'color': '#506784',
                           'display': 'inline-block'}
                    )
        ]
    )
])

if __name__ == '__main__':
    app.run_server()

