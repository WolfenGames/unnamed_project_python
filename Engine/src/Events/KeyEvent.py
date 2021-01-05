from Engine.src.Events.Event import UPEvent
from Engine.src.Core.KeyCodes import KeyCode


class KeyEvent(UPEvent):
    def __init__(self, keyCode) -> None:
        super().__init__()
        self.m_keyCode = keyCode
        self.EventClassCategory = UPEvent.EventClassCategory(UPEvent.EventCategory.EventCategoryKeyboard | UPEvent.EventCategory.EventCategoryInput)

    def GetKeyCode(self) -> KeyCode:
        return self.m_keycode

    def GetEventClassCategory(self):
        return self.EventClassCategory


class KeyPressedEvent(KeyEvent):
    def __init__(self, keyCode, repeatCount) -> None:
        super().__init__(keyCode)
        self.m_repeatCount = repeatCount
        self.EventClassCategory = UPEvent.EVENT_CLASS_TYPE(UPEvent.EventType.KeyPressed)

    def GetRepeatCount(self):
        return self.m_repeatCount

    def __str__(self) -> str:
        return f"KeyPressedEvent: {self.GetKeyCode()} ({self.m_repeatCount} repeats)"


class KeyReleasedEvent(KeyEvent):
    def __init__(self, keyCode) -> None:
        super().__init__(keyCode)
        self.EventClassCategory = UPEvent.EVENT_CLASS_TYPE(UPEvent.EventType.KeyTyped)

    def __str__(self) -> str:
        return f"KeyTypedEvent: {self.GetKeyCode()}"
