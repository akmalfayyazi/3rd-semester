from .processor import *
from .memory import *

class Computer:
    def __init__(self, processor, memory):
        if not isinstance(processor, Processor):
            raise TypeError("processor harus Processor")
        if not isinstance(memory, Memory):
            raise TypeError("memory harus Memory")
        self.__processor =  processor
        self.__memory = memory

    @property
    def processor(self):
        return self.__processor
    
    @processor.setter
    def processor(self, value):
        if not isinstance(value, Processor):
            raise TypeError("processor harus Processor")
        self.__processor = value

    @property
    def memory(self):
        return self.__memory
    
    @memory.setter
    def memory(self, value):
        if not isinstance(value, Memory):
            raise TypeError("memory harus Memory")
        self.__memory = value

    def get_info(self):
        return f"Processor Brand: {self.processor.brand.strip()}, Kecepatan: {self.processor.speed}, Memory Kapasitas: {self.memory.capacity}, Tipe: {self.memory.memory_type.strip()}"
    
if __name__ == "__main__":
    processor = ('Intel Core i9-14900KF', 9.13)
    memory = (192, 'DDR5')
    computer1 = Computer(processor, memory)
    print(computer1.get_info())