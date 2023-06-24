from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layout import create_layout
from src.language import __t__


def main():
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = __t__("general", "pokedex")
    app.layout = create_layout(app)
    app.run()


if __name__ == '__main__':
    main()
