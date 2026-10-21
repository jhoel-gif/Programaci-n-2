class Sensor:
    tipo = 'Generico'
    def __init__(self , id ):
        self.id = id
        self.encendido = False
        
    def activar(self):
        self.encendido = True
        return print("Encendido!!")
    
    def desactivar(self):
        self.encendido = False
        return print("Apagado")
    

class Camara(Sensor):
    tipo = "Camara"
    def __init__(self, id,resolucion):
        super().__init__(id)
        self.resolucion = resolucion
        

class Sensor_Luz_Laser(Sensor):
    tipo = 'Luz Laser'
    def __init__(self, id , alcance):
        super().__init__(id )
        self.alcance = alcance
        

class Vehiculo_Autonomo(Camara,Sensor_Luz_Laser):
    tipo = 'Vehiculo Autonomo'
    def __init__(self, id, resolucion ,alcance):
        Sensor.__init__(self,id)
        self.resolucion = resolucion
        self.alcance = alcance
        