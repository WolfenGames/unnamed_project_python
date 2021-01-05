from enum import Enum
from Engine.src.Core.base import BIT


class EventType(Enum):
    NoneEvent = 0,
    WindowClose = 1,
    WindowResize = 2,
    WindowFocus = 3,
    WindowLostFocus = 4,
    WindowMoved = 5,
    AppTick = 6,
    AppUpdate = 7,
    KeyPressed = 8,
    KeyReleased = 9,
    KeyTyped = 10,
    MouseButtonPressed = 11,
    MouseButtonReleased = 12,
    MouseMoved = 13,
    MouseScrolled = 14


class EventCategory(Enum):
    NoneEvent = 0,
    EventCategoryApplication = BIT(0),
    EventCategoryInput = BIT(1),
    EventCategoryKeyboard = BIT(2),
    EventCategoryMouse = BIT(3),
    EventCategoryMouseButton = BIT(4)


class EventClassBase(object):
    def GetEventType(self) -> EventType:
        raise NotImplementedError()

    def GetName(self) -> str:
        raise NotImplementedError()


class EventCategoryBase(object):
    def GetCategoryFlags(self) -> int:
        raise NotImplementedError()


class EVENT_CLASS_TYPE(EventClassBase):
    def __init__(self, type) -> None:
        self.m_type = type

    @staticmethod
    def GetStaticType(self) -> EventType:
        return self.m_type

    def GetEventType(self) -> EventType:
        self.GetStaticType()

    def GetName(self) -> str:
        return self.m_type.name


class EventClassCategory(EventCategoryBase):
    def __init__(self, category) -> None:
        self.m_category = category

    def GetCategoryFlags(self) -> int:
        return self.m_category


class UPEvent:
    def __init__(self) -> None:
        self.Handled = False

    def GetHandled(self) -> bool:
        return self.Handled

    def SetHandled(self, handled):
        self.Handled = handled

    def GetEventType(self) -> EventType:
        raise NotImplementedError()

    def GetName(self) -> str:
        raise NotImplementedError()

    def GetCategoryFlags(self) -> int:
        raise NotImplementedError()

    def __str__(self) -> str:
        return self.GetName()


class EventDispatcher:
    def __init__(self, event) -> None:
        self.m_Event = event

    def Dispatch(self, T, F) -> bool:
        if self.m_Event.GetEventType() == T.GetStaticType():
            handled = self.m_Event.GetHandled()
            handled |= F(T(self.m_Event))
            self.m_Event.SetHandled(handled)
            return True
        return False
