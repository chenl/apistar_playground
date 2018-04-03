from apistar import http, Route


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


routes = [
    Route('show_request', 'GET', show_request),
    Route('show_query_params', 'GET', show_query_params),
    Route('show_user_agent', 'GET', show_user_agent),
]
