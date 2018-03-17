import dash_auth
import os
from textwrap import dedent
import urllib3

import config

########################################################################
# This file provides an interface to the `plotly_auth` library
# You do not need to edit this file
########################################################################

def auth(app):
    if 'DYNO' in os.environ:
    if config.DASH_APP_PRIVACY == 'private':
        # Checks if running inside Plotly On-Premise environment
        if 'DYNO' in os.environ:
            if config.PATH_BASED_ROUTING:
                if config.DASH_APP_NAME == 'name-of-your-dash-app':
                     raise Exception(
                        'Please enter the name of your' +
                        ' dash app inside config.py')
                app.config.requests_pathname_prefix = '/{}/'.format(
                    config.DASH_APP_NAME
                )

        if config.PATH_BASED_ROUTING:
            APP_URL = '{}/{}'.format(
                config.PLOTLY_DASH_DOMAIN.strip('/'),
                config.DASH_APP_NAME,
            )
        else:
            APP_URL = '{}://{}.{}'.format(
                config.PLOTLY_DASH_DOMAIN.split('://')[0],
                config.DASH_APP_NAME,
                config.PLOTLY_DASH_DOMAIN.split('://')[1].strip('/')
            )

        dash_auth.PlotlyAuth(
            app,
            config.DASH_APP_NAME,
            config.DASH_APP_PRIVACY,
            APP_URL
        )
