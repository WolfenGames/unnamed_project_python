from Engine.src.Events.ApplicationEvent import WindowResizeEvent
from Engine.src.Platform.Windows.Windows import Window, WindowProperties
from Engine.src.gl_imports import *


class Application:

    def __init__(self) -> None:
        properties = WindowProperties()
        window = Window()
        self.m_Running = True
        self.m_Window = window.Create(properties=properties)

    def Run(self):
        while True:
            glClearColor(1, 0, 1, 1)
            glClear(GL_COLOR_BUFFER_BIT)
            self.m_Window.OnUpdate()

    def OnEvent(self, event):
        pass
