from textual import events
from textual.reactive import reactive
from textual.widget import Widget
from .grid import Grid

class Game(Widget):

    key = reactive("key")

    def __init__(self):
        super().__init__()
        self.grid = Grid()

    def render(self) -> str:
        return f"{self.key}"
    
    def ReadInput(self, event: events.Key) -> None:
        if event.key == "j" and self.grid.SpaceIsFree():
            self.grid.MoveForward()
        if event.key == "h":
            self.grid.TurnLeft()
        if event.key == "l":
            self.grid.TurnRight()

        self.key = self.grid.RenderMap()