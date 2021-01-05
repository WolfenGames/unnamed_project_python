from Engine import *
from Engine.src.Core.Application.Application import Application

class SandBox(Application):
    def __init__(self) -> None:
        super().__init__()

def CreateApplication():
    return SandBox()
