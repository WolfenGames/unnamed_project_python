from Engine.src.Events.Event import UPEvent, EVENT_CLASS_TYPE, EventClassCategory, EventCategory, EventType
from Engine.src.Core.KeyCodes.MouseCodes import MouseCodes

class MouseMovedEvent(UPEvent):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.m_MouseX = x
        self.m_MouseY = y
        self.m_EventClassType = EVENT_CLASS_TYPE( EventType.MouseMoved.value[0] )
        self.m_EventClassCategory = EventClassCategory( EventCategory.EventCategoryMouse.value[0] | EventCategory.EventCategoryInput.value[0] )

    def GetX(self) -> float:
        return self.m_MouseX

    def GetY(self) -> float:
        return self.m_MouseY

    def __str__(self) -> str:
        return f"MouseMovedEvent {self.m_MouseX}, {self.m_MouseY}"

    def GetEventClassType(self):
        return self.m_EventClassType

    def GetEventClassCategory(self):
        return self.m_EventClassCategory

class MouseScrolledEvent(UPEvent):
    def __init__(self, xOffset, yOffset) -> None:
        super().__init__()
        self.m_MouseXOffset = xOffset
        self.m_MouseYOffset = yOffset
        self.m_EventClassType = EVENT_CLASS_TYPE( EventType.MouseScrolled.value )
        self.m_EventClassCategory = EventClassCategory( EventCategory.EventCategoryMouse.value[0] | EventCategory.EventCategoryInput.value[0] )

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

class MouseButtonEvent(UPEvent):
    def __init__(self, button) -> None:
        super().__init__()
        self.m_Button = button
        categoryMouse = EventCategory.EventCategoryMouse.value[0]
        categoryInput = EventCategory.EventCategoryInput.value[0]
        categoryMouseButton = EventCategory.EventCategoryMouseButton.value
        self.m_EventClassCategory = EventClassCategory(
            categoryMouse | categoryInput | categoryMouseButton | categoryMouseButton
        )

    def GetButton(self) -> MouseCodes:
        return self.m_Button

    def GetEventClassCategory(self):
        return self.m_EventClassType

class MouseButtonPressedEvent(MouseButtonEvent):
    def __init__(self, button) -> None:
        super().__init__(button)
        self.m_EventClassType = EVENT_CLASS_TYPE( EventType.MouseButtonPressed.value[0] )

    def __str__(self) -> str:
        return f"MousePressedEvent: {self.m_Button}"

    # def GetEventClassType(self):
    #     return self.m_EventClassType

class MouseButtonReleasedEvent(MouseButtonEvent):
    def __init__(self, button) -> None:
        super().__init__(button)
        self.m_EventClassType = EVENT_CLASS_TYPE( EventType.MouseButtonReleased.value[0] )

    def __str__(self) -> str:
        return f"MouseReleasedEvent: {self.m_Button}"

    def GetEventClassType(self):
        return self.m_EventClassType
