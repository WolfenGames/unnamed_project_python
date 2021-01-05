from Engine.src.Events.ApplicationEvent import WindowResizeEvent
class Application():

    def Run(self):
        self.e = WindowResizeEvent(1280, 720)
        print(f"{self.e}")
