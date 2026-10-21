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

    def validar_numero(self, numero):
        if 0 <= numero <= 10:
            return True
        return False

    def juega(self):
        self.reiniciar_partida()
        self.nro_a_adivinar = random.randint(0, 10)
        print('Adivine el numero random entre 0 y 10')

        while self.nro_de_vidas > 0:
            intento = int(input('Ingrese su numero: '))

            if self.validar_numero(intento):
                if intento == self.nro_a_adivinar:
                    print('Acertaste!!')
                    self.actualizar_record()
                    return self.record

                self.quitar_vidas()

                if self.nro_de_vidas > 0:
                    if self.nro_a_adivinar > intento:
                        print(f'El numero a adivinar es mayor a: {intento}\nIntenta de nuevo')
                    else:
                        print(f'El numero a adivinar es menor a: {intento}\nIntenta de nuevo')

                    print(f'Vidas restantes: {self.nro_de_vidas}')
                else:
                    print('Juego Perdido\nSuerte para la proxima')
            else:
                print('Numero invalido. Ingrese un numero entre 0 y 10.')

        return self.record


class Juego_Adivinar_Par(Juego_Adivina_Numero):
    def __init__(self, nro_de_vidas, record=0):
        super().__init__(nro_de_vidas, record)

    def juega(self):
        self.reiniciar_partida()
        self.nro_a_adivinar = random.choice([0, 2, 4, 6, 8, 10])
        print('Adivine el numero par entre 0 y 10')

        while self.nro_de_vidas > 0:
            intento = int(input('Ingrese su numero: '))

            if self.validar_numero(intento):
                if intento == self.nro_a_adivinar:
                    print('Acertaste!!')
                    self.actualizar_record()
                    return self.record

                self.quitar_vidas()

                if self.nro_de_vidas > 0:
                    if self.nro_a_adivinar > intento:
                        print(f'El numero a adivinar es mayor a: {intento}\nIntenta de nuevo')
                    else:
                        print(f'El numero a adivinar es menor a: {intento}\nIntenta de nuevo')

                    print(f'Vidas restantes: {self.nro_de_vidas}')
                else:
                    print('Juego Perdido\nSuerte para la proxima')
            else:
                print('Error!! Ingrese un numero par entre 0 y 10.')

        return self.record

    def validar_numero(self, numero):
        return 0 <= numero <= 10 and numero % 2 == 0


class Juega_Adivina_Impar(Juego_Adivina_Numero):
    def __init__(self, nro_de_vidas, record=0):
        super().__init__(nro_de_vidas, record)

    def juega(self):
        self.reiniciar_partida()
        self.nro_a_adivinar = random.choice([1, 3, 5, 7, 9])
        print('Adivine el numero impar entre 0 y 10')

        while self.nro_de_vidas > 0:
            intento = int(input('Ingrese su numero: '))

            if self.validar_numero(intento):
                if intento == self.nro_a_adivinar:
                    print('Acertaste!!')
                    self.actualizar_record()
                    return self.record

                self.quitar_vidas()

                if self.nro_de_vidas > 0:
                    if self.nro_a_adivinar > intento:
                        print(f'El numero a adivinar es mayor a: {intento}\nIntenta de nuevo')
                    else:
                        print(f'El numero a adivinar es menor a: {intento}\nIntenta de nuevo')

                    print(f'Vidas restantes: {self.nro_de_vidas}')
                else:
                    print('Juego Perdido\nSuerte para la proxima')
            else:
                print('Error!! Ingrese un numero impar entre 0 y 10.')

        return self.record

    def validar_numero(self, numero):
        return 0 <= numero <= 10 and numero % 2 != 0


class Aplicacion:
    @staticmethod
    def main():
        record = 0

        juego_normal = Juego_Adivina_Numero(3, record)
        print('\n   Juego normal    ')
        record = juego_normal.juega() or juego_normal.record

        juego_par = Juego_Adivinar_Par(3, record)
        print('\n   Juego pares    ')
        record = juego_par.juega() or juego_par.record

        juego_impar = Juega_Adivina_Impar(3, record)
        print('\n   Juego impares    ')
        record = juego_impar.juega() or juego_impar.record


Aplicacion.main()