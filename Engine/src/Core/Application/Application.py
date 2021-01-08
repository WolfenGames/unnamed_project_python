from Engine.src.Events.ApplicationEvent import WindowClosedEvent
from Engine.src.Events.Event import EventDispatcher
from Engine.src.Platform.Windows.Windows import Window, WindowProperties
from Engine.src.Singletons.Singletons import Singleton
from Engine.src.gl_imports import *

from Engine.src.Layers.LayerStack import LayerStack

class Application(metaclass=Singleton):

    def __init__(self) -> None:
        properties = WindowProperties()
        window = Window()
        self.m_Running = True
        self.m_Window = window.Create(properties=properties)


        # Basic Layer System, still to be changed and finalized.
        # This is in no way, shape or form a working LayerStack
        self.layerstack = LayerStack()
        self.layerstack.AddLayer(name="Window - Layer")
        self.layerstack.AddOverlay(name="Test Overlay", status=False)
        self.layerstack.AddLayer(name="User Interface", status=False)

        print(f"\nCurrent number of Layers - {len(self.layerstack.layers)}")
        self.layerstack.Debug_info()

    def Get(self):
        return self

    def Run(self):
        r = 0
        g = 0
        b = 0
        redFlipped = False
        greenFlipped = False
        blueFlipped = False
        while not window_should_close(self.m_Window.m_Window):
            if redFlipped:
                r += 0.100001
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

            if r >= 0.9:
                redFlipped = False
            if g >= 0.9:
                greenFlipped = False
            if b >= 0.9:
                blueFlipped = False
            if r <= 0.1:
                redFlipped = True
            if g <= 0.1:
                greenFlipped = True
            if b <= 0.1:
                blueFlipped = True

            glClearColor(r, g, b, 1)
            glClear(GL_COLOR_BUFFER_BIT)
            self.m_Window.OnUpdate()

    def OnWindowClose(self) -> bool:
        self.m_Running = False
        return True

    def OnEvent(self, event):
        dispatch = EventDispatcher(event)
        dispatch.Dispatch(WindowClosedEvent, self.OnWindowClose)
        # pass
