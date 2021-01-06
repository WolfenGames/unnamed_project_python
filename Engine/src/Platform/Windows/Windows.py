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
        print(e)
        self.e = e

    def GetEventCallBack(self):
        print(f"{self.e}")
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
        global s_GFLWInit
        self.m_Data = WindowsData(
            properties.GetTitle(),
            properties.GetWidth(),
            properties.GetHeight()
        )
        print(f"{self.m_Data.GetTitle()}")

        if not s_GFLWInit:
            success = glfw.init()
            print(f"GLU Failed to init") if not success else print(f"GLU Init")
            glfw.set_error_callback(self.ErrorFunction)
            s_GFLWInit = True

        width = self.m_Data.GetWidth()
        height = self.m_Data.GetHeight()

        self.m_Window = glfw.create_window(width, height, self.m_Data.GetTitle(), None, None)
        if not self.m_Window:
            glfw.terminate()
        glfw.make_context_current(self.m_Window)

        self.SetVsync(True)
        glfw.set_window_size_callback(self.m_Window, self.WindowResizeFunction)
        glfw.set_window_close_callback(self.m_Window, self.WindowCloseFunction)
        glfw.set_key_callback(self.m_Window, self.KeyCallFuction)
        glfw.set_mouse_button_callback(self.m_Window, self.MouseButtonFunction)
        glfw.set_scroll_callback(self.m_Window, self.ScrollFunction)
        glfw.set_cursor_pos_callback(self.m_Window, self.CursorPosCallback)

    def OnUpdate(self):
        glfw.swap_buffers(self.m_Window)
        glfw.poll_events()

    def SetVsync(self, enabled):
        if enabled:
            glfw.swap_interval(1)
        else:
            glfw.swap_interval(0)

        self.m_Data.SetVsync(enabled)

    def SetEventCallback(self, e):
        self.m_Data.EventCallBack(e)
        print(f"{self.m_Data.GetEventCallBack()}")

    def ShutDown(self):
        glfw.destroy_window(self.m_Window)

    def WindowResizeFunction(self, window, width, height):
        data = glfw.get_window_user_pointer(window)
        event = WindowResizeEvent(width, height)
        # data.SetWidth(width)
        # data.SetHeight(height)
        # data.EventCallBack(event)

    def WindowCloseFunction(self, window):
        glfw.set_window_should_close(window, glfw.TRUE)

    def KeyCallFuction(self, window, key, scancode, action, mods):
        data = WindowsData(glfw.get_window_user_pointer(window))
        switcher = {
            glfw.PRESS: KeyPressedEvent(key, 0),
            glfw.RELEASE: KeyReleasedEvent(key),
            glfw.REPEAT: KeyRepeatEvent(key, 1)
        }
        aa = switcher.get(action, "Fuck all")
        data.EventCallBack(aa)

    def MouseButtonFunction(self, window, button, action, mods):

        data = WindowsData(glfw.get_window_user_pointer(window))
        switcher = {
            glfw.PRESS: MouseButtonPressedEvent(button),
            glfw.RELEASE: MouseButtonReleasedEvent(button)
        }
        aa = switcher.get(action, "Fuck all")
        data.EventCallBack(aa)

    def ScrollFunction(self, window, xOffset, yOffset):
        data = WindowsData(glfw.get_window_user_pointer(window))
        event = MouseScrolledEvent(xOffset, yOffset)
        data.EventCallBack(event)

    def CursorPosCallback(self, window, xPos, yPos):
        data = WindowsData(glfw.get_window_user_pointer(window))
        event = MouseMovedEvent(xPos, yPos)
        data.EventCallBack(event)

    def ErrorFunction(self, err, desc):
        print(f"GLFW Error ({err}): {desc}")
