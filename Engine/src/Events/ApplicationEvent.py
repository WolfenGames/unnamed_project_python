from Engine.src.gl_imports import *
from Engine.src.Events.Event import UPEvent, EventCategory, EventClassCategory, EVENT_CLASS_TYPE, EventType


class WindowResizeEvent(UPEvent):
    def __init__(self, width, height) -> None:
        super().__init__()
        self.m_width = width
        self.m_height = height

    def GetWidth(self):
        return self.m_width

    def GetHeight(self):
        return self.m_height

    def __str__(self) -> str:
        return f"WindowResizeEvent: {self.m_width}, {self.m_height}"


class WindowClosedEvent(UPEvent):
    def __init__(self) -> None:
        super().__init__()
        self.m_EventClassType = EVENT_CLASS_TYPE(EventType.WindowClose)
        self.m_EventClassCategory = EventClassCategory(EventCategory.EventCategoryApplication)

    def GetEventClassType(self):
        return self.m_EventClassType

    def GetEventClassCategory(self):
        return self.m_EventClassCategory


class AppTickEvent(UPEvent):
    def __init__(self) -> None:
        super().__init__()
        self.m_EventClassType = EVENT_CLASS_TYPE(EventType.AppUpdate)
        self.m_EventClassCategory = EventClassCategory(EventCategory.EventCategoryApplication)

    def GetEventClassType(self):
        return self.m_EventClassType

    def GetEventClassCategory(self):
        return self.m_EventClassCategory


class AppRenderEvent(UPEvent):
    def __init__(self) -> None:
        super().__init__()
        self.m_EventClassType = EVENT_CLASS_TYPE(EventType.AppRender)
        self.m_EventClassCategory = EventClassCategory(EventCategory.EventCategoryApplication)

    def GetEventClassType(self):
        return self.m_EventClassType

    def GetEventClassCategory(self):
        return self.m_EventClassCategory
