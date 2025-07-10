from textual.app import App, ComposeResult
from textual import events
from gamelogic.game import Game 

class App(App):
    def compose(self) -> ComposeResult:
        yield Game()

    def on_key(self, event: events.Key) -> None:
        self.query_one(Game).ReadInput(event)

if __name__ == "__main__":
    app = App()
    app.run()