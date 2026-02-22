class Memory:
    def __init__(self, capacity, memory_type):
        self.__capacity = int(capacity)
        self.__memory_type = memory_type.strip()

    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        try:
            self.__capacity = int(value)
        except ValueError:
            raise ValueError("speed harus bisa dikonversi ke float")

    @property
    def memory_type(self):
        return self.__memory_type.strip()
    
    @memory_type.setter
    def memory_type(self, value):
        self.__memory_type = value