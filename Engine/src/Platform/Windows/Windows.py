from Engine.src.Events.ApplicationEvent import WindowResizeEvent, WindowClosedEvent
from Engine.src.Events.KeyEvent import KeyPressedEvent, KeyReleasedEvent, KeyRepeatEvent
from Engine.src.Events.MouseEvent import MouseButtonPressedEvent, MouseButtonReleasedEvent, MouseScrolledEvent, \
    MouseMovedEvent
from Engine.src.gl_imports import *


class WindowProperties:
    def __init__(self,
                 title="UnnamedProject",
                 width=1280,
                 height=720):
        self.m_Title = title
        self.m_Width = width
        self.m_Height = height

    def GetTitle(self) -> str:
        return self.m_Title

    def GetWidth(self) -> int:
        return self.m_Width

    def GetHeight(self) -> int:
        return self.m_Height

    def __str__(self):
        return f"WindowTitle: {self.GetTitle()}, {self.GetWidth()}, {self.GetHeight()}"


class WindowsData:
    def __init__(self, title="none", width=0, height=0, vsync=False):
        self.Title = title
        self.Width = width
        self.Height = height
        self.Vsync = vsync

    def GetTitle(self):
        return self.Title

    def SetTitle(self, title):
        self.Title = title

    def GetHeight(self):
        return self.Height

    def SetHeight(self, height):
        self.Height = height

    def GetWidth(self) -> int:
        return self.Width

    def SetWidth(self, width):
        self.width = width

    def GetVsync(self):
        return self.Vsync

    def SetVsync(self, vsync):
        self.Vsync = vsync

    def EventCallBack(self, e):
        self.e = e

    def GetEventCallBack(self):
        return self.e

    def __str__(self):
        return f"I am a window Titled: {self.Title} - {self.GetWidth()} x {self.GetHeight()} ({self.GetVsync()})"

class Window:

    def OnUpdate(self):
        raise NotImplementedError()

    def GetWidth(self):
        raise NotImplementedError()

    def GetHeight(self):
        raise NotImplementedError()

    def SetEventCallBack(self, callback):
        raise NotImplementedError()

    def SetVsync(self, enabled):
        raise NotImplementedError()

    @staticmethod
    def Create(properties):
        return WindowsWindow(properties)


s_GFLWInit = False


class WindowsWindow:

    def __init__(self, properties):
        self.Init(properties)

    def Init(self, properties):
        print(get_version_string())
        global s_GFLWInit
        self.m_Data = WindowsData(
            properties.GetTitle(),
            properties.GetWidth(),
            properties.GetHeight()
        )
        print(f"{self.m_Data.GetTitle()}")

        if not s_GFLWInit:
            success = init()
            print(f"GLU Failed to init") if not success else print(f"GLU Init")
            set_error_callback(self.ErrorFunction)
            s_GFLWInit = True

        width = self.m_Data.GetWidth()
        height = self.m_Data.GetHeight()

        self.m_Window = create_window(width, height, self.m_Data.GetTitle(), None, None)
        if not self.m_Window:
            terminate()
            exit(1)
        make_context_current(self.m_Window)

        self.SetVsync(True)
        set_window_size_callback(self.m_Window, self.WindowResizeFunction)
        set_window_close_callback(self.m_Window, self.WindowCloseFunction)
        set_key_callback(self.m_Window, self.KeyCallFuction)
        set_mouse_button_callback(self.m_Window, self.MouseButtonFunction)
        set_scroll_callback(self.m_Window, self.ScrollFunction)
        set_cursor_pos_callback(self.m_Window, self.CursorPosCallback)

    def OnUpdate(self):
        swap_buffers(self.m_Window)
        poll_events()

    def SetVsync(self, enabled):
        if enabled:
            swap_interval(1)
        else:
            swap_interval(0)

        self.m_Data.SetVsync(enabled)

    def SetEventCallback(self, e):
        self.m_Data.EventCallBack(e)

    def ShutDown(self):
        destroy_window(self.m_Window)

    def WindowResizeFunction(self, window, width, height):
        WindowResizeEvent(width, height)

    def WindowCloseFunction(self, window):
        self.ShutDown()

    def KeyCallFuction(self, window, key, scancode, action, mods):
        switcher = {
            PRESS: KeyPressedEvent(key, 0),
            RELEASE: KeyReleasedEvent(key),
            REPEAT: KeyRepeatEvent(key, 1)
        }
        aa = switcher.get(action, "Fuck all")

    def MouseButtonFunction(self, window, button, action, mods):
        switcher = {
            PRESS: MouseButtonPressedEvent(button),
            RELEASE: MouseButtonReleasedEvent(button)
        }
        aa = switcher.get(action, "Fuck all")

    def ScrollFunction(self, window, xOffset, yOffset):
        MouseScrolledEvent(xOffset, yOffset)

    def CursorPosCallback(self, window, xPos, yPos):
        MouseMovedEvent(xPos, yPos)

    def ErrorFunction(self, err, desc):
        print(f"GLFW Error ({err}): {desc}")
