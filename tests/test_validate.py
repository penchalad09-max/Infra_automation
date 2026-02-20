from python import validate_webserver

def test_webserver_running():
    # Call your validation function
    result = validate_webserver.check_webserver()
    # Assert that it returns True (or expected output)
    assert result is True
