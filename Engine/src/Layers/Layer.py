
class Layer:

    def __init__(self,  priority=0, name="default layer", status=True):
        self.priority = priority
        self.Enabled = status
        self.DebugName = name

    #here for possible expansion and intergration into engine
    def OnAttach(self):
        return self

    def OnDetach(self):
        return self

    def OnUpdate(self):
        return self

    def OnEvent(self, event):
        return self
    #------------------------------------------------

    def GetName(self):
        return self.DebugName

    def SetName(self, name):
        self.DebugName = name

    def Getstatus(self):
        return self.Enabled

    def SetStatus(self, status):
        self.Enabled = status
