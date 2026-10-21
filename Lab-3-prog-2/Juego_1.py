import random

class Juego:
    def __init__(self, nro_de_vidas, record=0):
        self.nro_de_vidas = nro_de_vidas
        self.record = record

    def reiniciar_partida(self):
        self.nro_de_vidas = 3
        print(f'''
                Record = {self.record}
                Vidas = {self.nro_de_vidas}
                ''')

    def actualizar_record(self):
        self.record += 1
        return self.record

    def quitar_vidas(self):
        self.nro_de_vidas -= 1
        return self.nro_de_vidas


class Juego_Adivina_Numero(Juego):
    def __init__(self, nro_de_vidas, record=0):
        super().__init__(nro_de_vidas, record)
        self.nro_a_adivinar = 0

    def juega(self):
        self.reiniciar_partida()
        self.nro_a_adivinar = random.randint(0, 10)
        print('Adivine el numero random entre 0 y 10')

        while self.nro_de_vidas > 0:
            intento = int(input('Ingrese su numero: '))

            if intento == self.nro_a_adivinar:
                print('Acertaste!!')
                self.actualizar_record()
                return

            else:
                self.quitar_vidas()

                if self.nro_de_vidas > 0:
                    if self.nro_a_adivinar > intento:
                        print(f'El numero a adivinar es mayor a: {intento}\nIntenta de nuevo')
                    else:
                        print(f'El numero a adivinar es menor a: {intento}\nIntenta de nuevo')

                    print(f'Vidas restantes: {self.nro_de_vidas}')
                else:
                    print('Juego Perdido\nSuerte para la proxima')


class Aplicacion:
    @staticmethod
    def main(record):
        partida = Juego_Adivina_Numero(3, record)
        partida.juega()
        return partida.record


record = 0
seguir_juagndo = True

while seguir_juagndo:
    record = Aplicacion.main(record)

    seguir_juagndo = input('Quiere seguir jugando\n(si / no): ').lower()

    if seguir_juagndo != 'si':
        print('Hasta la proxima')
        seguir_juagndo = False