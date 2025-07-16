import argparse
import sys
from textual.app import App, ComposeResult
from textual import events
from textual.containers import Horizontal, Vertical
from textual.widgets import Static
from gamelogic.game import Game 

class Controls(Static): 

    DEFAULT_CSS = """
    Controls {
        border: solid red;
        content-align: left top;
        height: auto;
        padding: 5;
    }
    """
    def render(self) -> str:
        return (
            "(h) Turn Left\n"
            "(j) Move Forward\n"
            "(l) Turn Right\n"
            "(CTRL + Q) Quit\n"
        )

class App(App):
    parser = argparse.ArgumentParser(description="LAN of Monsters")
    subparser = parser.add_subparsers(dest="mode", required=True, help="Run the app as either the client or the server.")

    server_parser = subparser.add_parser("server", help="Run application as the server.")

    client_parser = subparser.add_parser("client", help="Run application as the client.")
    client_parser.add_argument("--address", required=True, help="IP address of server.")

    args = parser.parse_args()

    DEFAULT_CSS = """
    Controls {
        border: solid red;
        content-align: left top;
        height: auto;
        padding: 5;
    }
    """
    def render(self) -> str:
        return (
            "(h) Turn Left\n"
            "(j) Move Forward\n"
            "(l) Turn Right\n"
            "(CTRL + Q) Quit\n"
        )

class App(App):
    
    def compose(self) -> ComposeResult:
        yield Vertical(Vertical(Game()), Horizontal(Vertical(Controls()), Vertical()))
    
    def compose(self) -> ComposeResult:
        yield Vertical(Vertical(Game()), Horizontal(Vertical(Controls()), Vertical()))

    def on_key(self, event: events.Key) -> None:
        self.query_one(Game).ReadInput(event)

if __name__ == "__main__":
    app = App()
    app.run()