from Engine.src.Events.ApplicationEvent import WindowClosedEvent
from Engine.src.Events.Event import EventDispatcher
from Engine.src.Platform.Windows.Windows import Window, WindowProperties
from Engine.src.gl_imports import *


class Application:

    def __init__(self) -> None:
        properties = WindowProperties()
        window = Window()
        self.m_Running = True
        self.m_Window = window.Create(properties=properties)
        self.m_Window.SetEventCallback(self.OnEvent)

    def Run(self):
        r = 0
        g = 0
        b = 0
        redFlipped = False
        greenFlipped = False
        blueFlipped = False
        while not glfw.window_should_close(self.m_Window.m_Window):
            if redFlipped:
                r += 0.00001
            else:
                r -= 0.00007

            if greenFlipped:
                g += 0.0001
            else:
                g -= 0.0002

            if blueFlipped:
                b += 0.001
            else:
                b -= 0.003

            if r >= 1:
                redFlipped = False
            if g >= 1:
                greenFlipped = False
            if b >= 1:
                blueFlipped = False
            if r <= 0:
                redFlipped = True
            if g <= 0:
                greenFlipped = True
            if b <= 0:
                blueFlipped = True
            glClearColor(r, g, b, 1)
            glClear(GL_COLOR_BUFFER_BIT)
            self.m_Window.OnUpdate()

    def OnWindowClose(self) -> bool:
        self.m_Running = False
        return True

    def OnEvent(self, event):
        print(event)
        dispatch = EventDispatcher(event)
        dispatch.Dispatch(WindowClosedEvent, self.OnWindowClose)
