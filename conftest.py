import pytest
from django.test import Client


@pytest.fixture
def django_test_client():
    return Client()
