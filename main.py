class Asiento:

    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color in ["rojo", "verde", "amarillo", "negro", "blanco"]:
            self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, newregistro):
        self.registro = newregistro

    def asignarTipo(self, newtipo):
        if newtipo in ["electrico","gasolina"]:
            self.tipo = newtipo


class Auto:
    cantidadCreados = 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1

    def cantidadAsientos(self):
        count = 0
        for asiento in self.asientos:
            if isinstance(asiento, Asiento):
                count += 1
        return count
    
    def verificarIntegridad(self):
        if self.registro != self.motor.registro:
            return "Las piezas no son originales"
        for asiento in self.asientos:
            if asiento and asiento.registro != self.registro:
                return "Las piezas no son originales"
        return "Auto original"