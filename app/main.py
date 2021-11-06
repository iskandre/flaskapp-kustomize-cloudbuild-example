import os
import sys
from flask import Flask
import time

app = Flask(__name__)
@app.route('/info/', methods=['GET'])
def get_messages():
    version = "{}.{}".format(sys.version_info.major, sys.version_info.minor)
    # start_response("200 OK", [("Content-Type", "text/plain")])
    message = "Hello World1 from a default Python {} app in a Docker container, with Meinheld and Gunicorn (default)".format(
        version
    )
    if os.getenv('APP_LOCATION'):
        message = message + F" app-location:{os.getenv('APP_LOCATION')}"
    if os.getenv('ENVIRONMENT'):
        message = message + F". You are currently in {os.getenv('ENVIRONMENT')} environment."
    if os.getenv('DEPLOYED_CITY'):
        message = message + F" The app was deployed in city {os.getenv('DEPLOYED_CITY')}"
    return message

#if __name__ == '__main__':
#    host = os.getenv("HOST", "0.0.0.0")
#    port = os.getenv("PORT", "8010")
#    app.run(debug=False, port=port, host=host)