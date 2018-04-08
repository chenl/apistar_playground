import base64
from apistar import http, Route
from apistar.authentication import Authenticated
from apistar.interfaces import Auth


class BasicAuthentication:

    def authenticate(self, authorization: http.Header):
        """Determine the user associated with the request, using HTTP Basic
        Authentication.

        """
        if authorization is None:
            return None

        scheme, token = authorization.split()
        if scheme.lower() != 'basic':
            return None

        username, password = base64.b64decode(token).decode('utf-8').split(':')
        # TODO: put password validation code here
        return Authenticated(username)


def display_user(auth: Auth):
    return {
        'is_authenticated': auth.is_authenticated(),
        'user': auth.get_display_name(),
    }


routes = [
    Route('/display', 'GET', display_user),
]
