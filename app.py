from apistar import annotate, render_template, Include, Route
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls, static_urls
from apistar.renderers import HTMLRenderer

import bs_api.playground
from bs_api.auth import BasicAuthentication


@annotate(renderers=[HTMLRenderer()])
def hello(username: str):
    return render_template('index.html', username=username)


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


routes = [
    Route('/', 'GET', hello),
    Include('/docs', docs_urls),
    Include('/static', static_urls),
    Include('/playgound', bs_api.playground.routes),
]

settings = {
    'TEMPLATES': {
        'ROOT_DIR': 'templates',       # Include the 'templates' direcotry.
        'PACKAGE_DIRS': ['apistar'],   # Include the buildin apistar templates.
    },
    'AUTHENTICATION': [BasicAuthentication()]
}

app = App(
    routes=routes,
    commands=bs_api.playground.commands,
    settings=settings,
)


if __name__ == '__main__':
    app.main()
