from Engine.src.Events.Event import UPEvent, EventClassCategory, EventCategory, EVENT_CLASS_TYPE, EventType
from Engine.src.Core.KeyCodes import KeyCode


class KeyEvent(UPEvent):
    def __init__(self, keyCode) -> None:
        super().__init__()
        self.m_keyCode = keyCode
        self.EventClassCategory = EventClassCategory(EventCategory.EventCategoryKeyboard.value[0] | EventCategory.EventCategoryInput.value[0] )

    def GetKeyCode(self) -> KeyCode:
        return self.m_keyCode

    def GetEventClassCategory(self):
        return self.EventClassCategory


class KeyPressedEvent(KeyEvent):
    def __init__(self, keyCode, repeatCount) -> None:
        super().__init__(keyCode)
        self.m_repeatCount = repeatCount
        self.EventClassCategory = EVENT_CLASS_TYPE(EventType.KeyPressed.value[0])

    def GetRepeatCount(self):
        return self.m_repeatCount

    def __str__(self) -> str:
        return f"KeyPressedEvent: {self.GetKeyCode()} ({self.m_repeatCount} repeats)"


class KeyReleasedEvent(KeyEvent):
    def __init__(self, keyCode) -> None:
        super().__init__(keyCode)
        self.EventClassCategory = EVENT_CLASS_TYPE(EventType.KeyTyped.value[0])

    def __str__(self) -> str:
        return f"KeyTypedEvent: {self.GetKeyCode()}"

class KeyRepeatEvent(KeyEvent):
    def __init__(self, keyCode, repeatCount) -> None:
        super().__init__(keyCode)
        self.m_repeatCount = repeatCount
        self.EventClassCategory = EVENT_CLASS_TYPE(EventType.KeyTyped.value[0])

    def __str__(self) -> str:
        return f"KeyTypedEvent: {self.GetKeyCode()} ({self.m_repeatCount} repeats)"