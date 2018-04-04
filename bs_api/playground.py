from typing import Iterable
from apistar import http, Include, Route, Response, reverse_url


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


user_idx = 2
users = {0: 'penny', 1: 'benny', 2: 'jenny'}


def list_users():
    """list all users"""
    return users


def create_user(name: str):
    """Create a user"""
    global user_idx, users
    user_idx += 1
    users[user_idx] = name
    return {
        'message': 'user created',
        'uid': user_idx,
        'name': name,
    }


def edit_user(user_id: int, name: str):
    """Modify a user's data"""
    global users
    old_name = users[user_id]
    users[user_id] = name
    return {
        'message': 'user modified',
        'uid': user_id,
        'old_name': old_name,
        'new_name': name,
    }


def delete_user(user_id: int):
    """Remove a user from the database..."""
    global users
    name = users.pop(user_id)
    return {
        'message': 'user deleted',
        'uid': user_id,
        'name': name,
    }


user_routes = [
    Route('/', 'GET', list_users),
    Route('/', 'POST', create_user),
    Route('/{user_id}', 'PUT', edit_user),
    Route('/{user_id}', 'DELETE', delete_user),
]


# Revese routing

players = {'penny': 42, 'benny': 99, 'jenny': 1234}


def get_score(player_name: str) -> int:
    return players[player_name]


def get_palyers() -> Iterable[str]:
    return players.keys()

# ----------------------------------------------------------------------


def get_palyer_details(player_name: str):
    score = get_score(player_name)
    return {'name': player_name, 'score': score}


def get_all_palyers():
    player_names = get_palyers()
    player_list = [
        {
            'name': player_name,
            'url': reverse_url('get_palyer_details', player_name=player_name),
        }
        for player_name in player_names
    ]
    return {'players': player_list}


players_routes = [
    Route('/', 'GET', get_all_palyers),
    Route('/{player_name}/', 'GET', get_palyer_details),
]

# ----------------------------------------------------------------------


routes = [
    Route('/show_request', 'GET', show_request),
    Route('/show_query_params', 'GET', show_query_params),
    Route('/show_user_agent', 'GET', show_user_agent),

    Route('/create_project_default', 'GET', create_project_default),
    Route('/create_project', 'GET', create_project),

    Route('/hello/{username}/', 'GET', echo_username),

    Include('/users', user_routes),

    Include('/players', players_routes),
]
