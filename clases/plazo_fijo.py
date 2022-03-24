from datetime import datetime
from datetime import timedelta
class fijo:
    def __init__(self, saldo, fecha_vencimiento, penalizacion):
        self.saldo=saldo
        self.fecha_vencimiento = fecha_vencimiento
        self.penalizacion = penalizacion

    def retirada(self):
        penalizacion = 1.05
        saldo = 10000
        fecha_entrada = datetime.now()
        delta =timedelta (days= 50)
        fecha_vencimiento = fecha_entrada + delta
        x = input('¿Desea retirar dinero?: (si o no)')
        if x == 'no':
            print('De acuerdo, muchas gracias!')
        if x == 'si' and fecha_entrada < fecha_vencimiento:
            print('Puede realizar la operacion, pero recuerde que tiene hasta:', fecha_vencimiento, 'para seguir retirando dinero')
            retirar= float(input('¿Cuanto desea retirar?:'))
            saldo = saldo - retirar*penalizacion
            print('Su saldo es', saldo, '€')

print(fijo.retirada('penalizacion, saldo, fecha_entrada, delta, fecha_vencimiento'))