def test_app_is_created(app_flask):
    print(app_flask.name)
    assert app_flask.name != ''