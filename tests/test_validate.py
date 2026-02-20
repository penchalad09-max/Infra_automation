import sys
import os

# Add the python folder to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "python"))

import validate_webserver

def test_webserver_running():
    result = validate_webserver.check_webserver()
    assert result is True
