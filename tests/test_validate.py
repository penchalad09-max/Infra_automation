import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "python"))

import validate_webserver

def test_webserver_running():
    assert validate_webserver.check_webserver() is True
