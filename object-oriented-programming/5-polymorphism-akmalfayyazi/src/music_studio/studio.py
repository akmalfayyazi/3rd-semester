from .instrumen import *

class StudioMusik:
    def __init__(self):
        self._list_instrumen = []

    def tambah_instrumen(self, instrumen):
        if not isinstance(instrumen, Instrumen):
            raise TypeError("Harus turunan Instrumen")
        self._list_instrumen.append(instrumen)

    def mainkan_instrumen(self):
        return [f"{i.nama} berbunyi: {i.mainkan()}" for i in self._list_instrumen]
    
if __name__ == "__main__":
    studio = StudioMusik()
    gitar1 = Gitar('gitar')
    piano1 = Piano('piano')

    studio.tambah_instrumen(gitar1)
    studio.tambah_instrumen(piano1)

    print(studio.mainkan_instrumen())