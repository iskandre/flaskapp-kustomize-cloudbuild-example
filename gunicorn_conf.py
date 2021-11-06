from __future__ import print_function

import json
import os

host = os.getenv("HOST", "0.0.0.0")
port = os.getenv("PORT", "8010")
bind_env = os.getenv("BIND", None)
use_loglevel = os.getenv("LOG_LEVEL", "info")
if bind_env:
    use_bind = bind_env
else:
    use_bind = "{host}:{port}".format(host=host, port=port)

# Gunicorn config variables
loglevel = use_loglevel
workers = workers_per_core = 1
bind = use_bind
keepalive = 120
errorlog = "-"

# For debugging and testing
log_data = {
    "loglevel": loglevel,
    "workers": workers,
    "bind": bind,
    # Additional, non-gunicorn variables
    "workers_per_core": workers_per_core,
    "host": host,
    "port": port,
}
print(json.dumps(log_data))