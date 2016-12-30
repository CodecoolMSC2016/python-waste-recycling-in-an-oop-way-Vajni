from garbage import Garbage


class PaperGarbage(Garbage):

    def __init__(self, garbage_name, squeezed):
        self.name = garbage_name
        self.is_squeezed = squeezed

    def squeeze(self):
        if self.is_squeezed == False:
            self.is_squeezed = True
        return self.is_squeezed

