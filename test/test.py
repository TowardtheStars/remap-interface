
import remap_interface

@remap_interface.remap()
class A:
    def __init__(self):
        self.a = []

print(hasattr(A(), 'append'))