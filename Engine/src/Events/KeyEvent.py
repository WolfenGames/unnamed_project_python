from Engine.src.Events import Event
from Engine.src.Core.KeyCode import *

class KeyEvent(Event):
    def __init__(self, keyCode) -> None:
        super().__init__()
        self.m_keyCode = keyCode
        self.EventClassCategory = Event.EventClassCategory(Event.EventCategory.EventCategoryKeyboard | Event.EventCategory.EventCategoryInput)

    def GetKeyCode(self) -> KeyCode:
        return self.m_keycode
        
    def GetEventClassCategory(self):
        return self.EventClassCategory

class KeyPressedEvent(KeyEvent):
    def __init__(self, keyCode, repeatCount) -> None:
        super().__init__(keyCode)
        self.m_repeatCount = repeatCount
        self.EventClassCategory = Event.EVENT_CLASS_TYPE(Event.EventType.KeyPressed)

    def GetRepeatCount(self):
        return self.m_repeatCount

    def __str__(self) -> str:
        return f"KeyPressedEvent: {self.GetKeyCode()} ({self.m_repeatCount} repeats)"

class KeyReleasedEvent(KeyEvent):
    def __init__(self, keyCode) -> None:
        super().__init__(keyCode)
        self.EventClassCategory = Event.EVENT_CLASS_TYPE(Event.EventType.KeyTyped)

    def __str__(self) -> str:
        return f"KeyTypedEvent: {self.GetKeyCode()}"
