class Arista:

    def __init__(self):
        self.peso = None
        self.destino = None
        self.origen = None

    def set_data(self, i, j, peso):
        self.origen = i
        self.destino = j
        self.peso = peso
        return self
