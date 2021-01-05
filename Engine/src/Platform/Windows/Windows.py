from Engine.src.gl_imports import *

class WindowProperties():
    def __init__(self,
        title = "UnnamedProject",
        width = 1280,
        height = 720):
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

class WindowsData():
    def __init__(self, title="none", width=0, height=0,vsync=False):
        self.Title = title
        self.Width = width
        self.Height = height
        self.Vsync = vsync

    def GetTitle(self):
        return self.Title

    def SetTitle(self, title) -> str:
        self.Title = title
    
    def GetHeight(self):
        return self.Height

    def SetHeight(self, height):
        self.Height = height

    def GetWidth(self) -> int:
        return self.Width

    def SetWidth(self, height) -> int:
        self.width = width

    def GetVsync(self):
        return self.Vsync

    def SetVsync(self, vsync):
        self.Vsync = vsync


class Window():

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

    def Create(self, properties):
        return WindowsWindow(properties)

    def __str__(self):
        self

s_GFLWInit = False        

class WindowsWindow():

    # def Create(self, properties):
    #     self.m_Window = self.Create(properties)
    #     return self.m_Window

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

        if s_GFLWInit == False:
            success = glfw.init()
            print(f"GLU Failed to init") if success == False else print(f"GLU Init")
            s_GFLWInit = True

        width = self.m_Data.GetWidth()
        height = self.m_Data.GetHeight()
        self.m_Window = glfw.create_window(width, height, self.m_Data.GetTitle(), None, None)
        if self.m_Window == None:
            glfw.terminate()
        glfw.make_context_current(self.m_Window)

        self.SetVsync(True)

    def OnUpdate(self):
        glfw.swap_buffers(self.m_Window)
        glfw.poll_events()

    # def GetWidth(self):
    #     pass

    def SetVsync(self, enabled):
        if enabled:
            glfw.swap_interval(1)
        else:
            glfw.swap_interval(0)

        self.m_Data.SetVsync(enabled)

    # def SetEventCallBack(self):
    #     pass

    def ShutDown(self):
        glfw.destroy_window(self.m_Window)
