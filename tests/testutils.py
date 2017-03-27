"""Common utility classes and functions for testing."""
import os

import httplib2

import firebase


def resource_filename(filename):
    """Returns the absolute path to a test resource."""
    return os.path.join(os.path.dirname(__file__), 'data', filename)


def resource(filename):
    """Returns the contents of a test resource."""
    with open(resource_filename(filename), 'r') as file_obj:
        return file_obj.read()


def cleanup_apps():
    with firebase._apps_lock:
        app_names = list(firebase._apps.keys())
        for name in app_names:
            firebase.delete_app(name)


class HttpMock(object):
    """A mock HTTP client implementation.

    This can be used whenever an HTTP interaction needs to be mocked
    for testing purposes. For example HTTP calls to fetch public key
    certificates, and HTTP calls to retrieve access tokens can be
    mocked using this class.
    """

    def __init__(self, status, response):
        self.status = status
        self.response = response

    def request(self, *args, **kwargs):
        del args
        del kwargs
        return httplib2.Response({'status': self.status}), self.response