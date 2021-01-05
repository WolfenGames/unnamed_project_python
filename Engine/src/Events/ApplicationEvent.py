from Engine.src.gl_imports import *
from Engine.src.Events.Event import UPEvent

class WindowResizeEvent(UPEvent):
    def __init__(self, width, height) -> None:
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
        self.m_EventClassType = UPEvent.EVENT_CLASS_TYPE(UPEvent.EventType.WindowClose)
        self.m_EventClassCategory = UPEvent.EventClassCategory(UPEvent.EventCategory.EventCategoryApplication)

    def GetEventClassType(self):
        return self.m_EventClassType

    def GetEventClassCategory(self):
        return self.m_EventClassCategory

class AppTickEvent(UPEvent):
    def __init__(self) -> None:
        super().__init__()
        self.m_EventClassType = UPEvent.EVENT_CLASS_TYPE(UPEvent.EventType.AppUpdate)
        self.m_EventClassCategory = UPEvent.EventClassCategory(UPEvent.EventCategory.EventCategoryApplication)

    def GetEventClassType(self):
        return self.m_EventClassType

    def GetEventClassCategory(self):
        return self.m_EventClassCategory

class AppRenderEvent(UPEvent):
    def __init__(self) -> None:
        super().__init__()
        self.m_EventClassType = UPEvent.EVENT_CLASS_TYPE(UPEvent.EventType.AppRender)
        self.m_EventClassCategory = UPEvent.EventClassCategory(UPEvent.EventCategory.EventCategoryApplication)

    def GetEventClassType(self):
        return self.m_EventClassType

    def GetEventClassCategory(self):
        return self.m_EventClassCategory
