from Engine.src.Layers.Layer import Layer

class LayerStack(Layer):

    def __init__(self):
        self.layers = []
        self.layer_position = 0

    def AddLayer(self, name = "default layer", status = True):
        self.layers.insert(self.layer_position ,Layer(0, name, status))
        self.layer_position += 1

    def AddOverlay(self, name = "default layer", status = True):
        self.layers.insert(0, Layer(len(self.layers), name, status))

    def RemoveLayer(self, m_layer):
        self.layers.remove(m_layer)

    def RemoveOverlay(self, m_layer):
        self.RemoveLayer(m_layer)

    def MoveLayerUp(self, m_layer):
        t_position = self.layers.index(m_layer)
        if t_position > 0:
            t_layer = self.layers.pop(m_layer)
            self.layers.insert(t_position-1, m_layer)

    def MoveLayerDown(self, m_layer):
        t_position = self.layers.index(m_layer)
        if t_position < (len(self.layers)-1):
            t_layer = self.layers.pop(m_layer)
            self.layers.insert(t_position+1, m_layer)

    def Destruct(self):
        for m_layer in self.layers:
            del m_layer

    def Debug_info(self):
        for t_layer in self.layers:
            print(f"Layer [{self.layers.index(t_layer)}]")
            print(f"\tlayer name   - '{t_layer.GetName()}'")
            print(f"\tlayer status - '{t_layer.Getstatus()}'")
