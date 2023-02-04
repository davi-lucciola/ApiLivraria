import pytest
from flask import Flask
from ..app.api import create_app


@pytest.fixture(scope="module")
def app_flask() -> Flask:
    '''Instância do app flask principal'''
    return create_app()
