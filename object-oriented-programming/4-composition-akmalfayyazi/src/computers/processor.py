class Processor:
    def __init__(self, brand: str, speed: float):
        self.__brand = brand.strip()
        try:
            self.__speed = float(speed)
        except ValueError:
            raise ValueError("speed harus bisa dikonversi ke float")

    @property
    def brand(self):
        return self.__brand
    
    @brand.setter
    def brand(self, value):
        self.__brand = value.strip()

    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, value):
        try:
            self.__speed = float(value)
        except ValueError:
            raise ValueError("speed harus bisa dikonversi ke float")
