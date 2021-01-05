from Engine.src.Events.ApplicationEvent import *
class Application():
    def __init__(self) -> None:
        super().__init__()

    def Run(self):
        self.e = WindowResizeEvent(1280, 720)
        print(f"{self.e}")
        while(True):
            pass
