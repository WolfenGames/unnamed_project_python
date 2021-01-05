from Engine.src.Events import Event
from Engine.src.Core.MouseCodes import *

class MouseMovedEvent(Event):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.m_MouseX = x
        self.m_MouseY = y
        self.m_EventClassType = Event.EVENT_CLASS_TYPE( Event.EventType.MouseMoved )
        self.m_EventClassCategory = Event.EventClassCategory( Event.EventCategory.EventCategoryMouse | Event.EventCategory.EventCategoryInput )

    def GetX(self) -> float:
        return self.m_MouseX

    def GetY(self) -> float:
        return self.m_MouseY

    def __str__(self) -> str:
        return f"MouseMovedEvent"

    def GetEventClassType(self):
        return self.m_EventClassType

    def GetEventClassCategory(self):
        return self.m_EventClassCategory

class MouseScrolledEvent(Event):
    def __init__(self, xOffset, yOffset) -> None:
        super().__init__()
        self.m_MouseXOffset = xOffset
        self.m_MouseYOffset = yOffset
        self.m_EventClassType = Event.EVENT_CLASS_TYPE( Event.EventType.MouseScrolled )
        self.m_EventClassCategory = Event.EventClassCategory( Event.EventCategory.EventCategoryMouse | Event.EventCategory.EventCategoryInput )

    def GetXOffset(self) -> float:
        return self.m_MouseXOffset

    def GetYOffset(self) -> float:
        return self.m_MouseYOffset

    def __str__(self) -> str:
        return f"MouseScrolledEvent: {self.m_MouseXOffset}, {self.m_MouseYOffset}"

    def GetEventClassType(self):
        return self.m_EventClassType

    def GetEventClassCategory(self):
        return self.m_EventClassCategory

class MouseButtonEvent(Event):
    def __init__(self, button) -> None:
        super().__init__()
        self.m_Button = button
        self.m_EventClassCategory = Event.EventClassCategory(
            Event.EventCategory.EventCategoryMouse | Event.EventCategory.EventCategoryInput | Event.EventCategory.EventCategoryMouseButton
        )

    def GetButton(self) -> MouseCodes:
        return self.m_Button

    def GetEventClassCategory(self):
        return self.m_EventClassType

class MouseButtonPressedEvent(MouseButtonEvent):
    def __init__(self, button) -> None:
        super().__init__(button)
        self.m_EventClassType = Event.EVENT_CLASS_TYPE( Event.EventType.MouseButtonPressed )

    def __str__(self) -> str:
        return f"MousePressedEvent: {self.m_Button}"

    def GetEventClassType(self):
        return self.m_EventClassType

class MouseButtonReleasedEvent(MouseButtonEvent):
    def __init__(self, button) -> None:
        super().__init__(button)
        self.m_EventClassType = Event.EVENT_CLASS_TYPE( Event.EventType.MouseButtonReleased )

    def __str__(self) -> str:
        return f"MouseReleasedEvent: {self.m_Button}"

    def GetEventClassType(self):
        return self.m_EventClassType
