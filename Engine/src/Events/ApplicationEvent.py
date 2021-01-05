from Engine.src.gl_imports import *
from Engine.src.Events import Event

class WindowResizeEvent(Event):
    def __init__(self, width, height) -> None:
        super.__init__()
        self.m_width = width
        self.m_height = height

    def GetWidth(self):
        return self.m_width

    def GetHeight(self):
        return self.m_height

    def __str__(self) -> str:
        return f"WindowResizeEvent: {self.m_width}, {self.m_height}"

class WindowClosedEvent(Event):
    def __init__(self) -> None:
        super().__init__()
        self.m_EventClassType = Event.EVENT_CLASS_TYPE(Event.EventType.WindowClose)
        self.m_EventClassCategory = Event.EventClassCategory(Event.EventCategory.EventCategoryApplication)

    def GetEventClassType(self):
        return self.m_EventClassType

    def GetEventClassCategory(self):
        return self.m_EventClassCategory

class AppTickEvent(Event):
    def __init__(self) -> None:
        super().__init__()
        self.m_EventClassType = Event.EVENT_CLASS_TYPE(Event.EventType.AppUpdate)
        self.m_EventClassCategory = Event.EventClassCategory(Event.EventCategory.EventCategoryApplication)

    def GetEventClassType(self):
        return self.m_EventClassType

    def GetEventClassCategory(self):
        return self.m_EventClassCategory

class AppRenderEvent(Event):
    def __init__(self) -> None:
        super().__init__()
        self.m_EventClassType = Event.EVENT_CLASS_TYPE(Event.EventType.AppRender)
        self.m_EventClassCategory = Event.EventClassCategory(Event.EventCategory.EventCategoryApplication)

    def GetEventClassType(self):
        return self.m_EventClassType

    def GetEventClassCategory(self):
        return self.m_EventClassCategory
