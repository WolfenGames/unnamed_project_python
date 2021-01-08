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

    def RemoveLayer(self, layer):
        self.layers.remove(layer)

    def RemoveOverlay(self, layer):
        self.RemoveLayer(layer)

    def MoveLayerUp(self, layer):
        t_position = self.layers.index(layer)
        if t_position > 0:
            t_layer = self.layers.pop(layer)
            self.layers.insert(t_position-1, layer)

    def MoveLayerDown(self, layer):
        t_position = self.layers.index(layer)
        if t_position < (len(self.layers)-1):
            t_layer = self.layers.pop(layer)
            self.layers.insert(t_position+1, layer)

    def Destruct(self):
        for layer in self.layers:
            self.layers.remove(layer)

    def Debug_info(self):
        for t_layer in self.layers:
            print(f"Layer [{self.layers.index(t_layer)}]")
            print(f"\tlayer name   - '{t_layer.GetName()}'")
            print(f"\tlayer status - '{t_layer.Getstatus()}'")
