import pytest
from flask import Flask
import src.app.main as main


@pytest.fixture(scope="module")
def app_flask() -> Flask:
    '''Instância do app flask principal'''
    return main.app


