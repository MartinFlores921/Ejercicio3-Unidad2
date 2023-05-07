class Registro:
    __temp: float = 0
    __humedad: int = 0
    __presion: int = 0
    def __init__(self, temperatura:float, humedad:int, presion:int):
        self.__temp = temperatura
        self.__humedad= humedad
        self.__presion = presion
    def get_temperatura (self):
        return self.__temp
    def get_humedad(self):
        return self.__humedad
    def get_presion(self):
        return self.__presion
