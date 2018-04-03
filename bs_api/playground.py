from apistar import http, Include, Route, Response


# Request

def show_request(request: http.Request):
    """Show a the content of the request object"""
    return {
        'method': request.method,
        'url': request.url,
        'headers': dict(request.headers),
    }


def show_query_params(query_params: http.QueryParams):
    """Show the content of the query parameters"""
    return {
        'params': dict(query_params),
    }


def show_user_agent(user_agent: http.Header):
    """Show the user agent"""
    return {
        'user_agent': user_agent,
    }


# Response

def create_project_default():
    """Create an object with default return code 200 OK"""
    return {'name': 'new project', 'id': 123}


def create_project():
    """Create a project with 201 CREATED status code

    By returning a Response object
    """
    data = {'name': 'new project', 'id': 123}
    headers = {'location': 'http://chen.rotemlevy.name/project/123'}
    return Response(data, status=201, headers=headers)


# URL Routing

def echo_username(username):
    """Say hello to a user"""
    return {'message': f'Welcome, {username}!'}
routes = [
    Route('show_request', 'GET', show_request),
    Route('show_query_params', 'GET', show_query_params),
    Route('show_user_agent', 'GET', show_user_agent),

    Route('create_project_default', 'GET', create_project_default),
    Route('create_project', 'GET', create_project),

    Route('hello/{username}/', 'GET', echo_username),
]
