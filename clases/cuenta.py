from datetime import datetime
class cuenta_bancaria:
    saldo= 0
    
    def __init__(self,id,titular,fecha,numero,saldo):
        self.id= id
        self.titular=titular
        self.fecha=fecha
        self.numero=numero
        self.saldo=saldo
    def cuenta(self):
        titular= input('Introduzca el nombre del titular:')
        fecha= datetime.now()
        numero= int(input('Introduzca su número de cuenta (8 dígitos):'))
        print('------------------------------------------------------------')
        print('TITULAR              FECHA ENTRADA                  NÚMERO')
        print('------------------------------------------------------------')
        print(titular, '\t',        fecha, '\t',         numero)
        print('------------------------------------------------------------')

    def operaciones(self):
        act = input('¿desea ingresar, retirar o transfeir dinero (si no desea realizar ninguna operación introduzca: no)?')
        saldo = 0
        if act== 'no':
            print('De acuerdo, muchas gracias y hasta la proxima!')
        if act == 'ingresar':
            ingreso = float(input('Introduzca la cantidad que desee ingresar:'))
            saldo = ingreso 
            print('Su saldo es', saldo, '€')
        if act == 'retirar':
            retiro = float(input('Introduca la cantidad que desea retirar:'))
            if retiro > saldo:
                print('No tiene suficiente dinero para retirar dicha cantidad')
            else:
                saldo = saldo - retiro
                print('Su saldo es', saldo, '€')
        if act == 'transferir':
            transferir = float(input('Introduce la cantidad que desea transferir:'))
            if transferir > saldo:
                print('No tiene suficiente saldo en la cuenta:')
            else:
                saldo = saldo - transferir
                print('La cantidad que ha transferido es:', transferir)
                print('Su saldo es', saldo, '€')

print(cuenta_bancaria.cuenta('titular, fecha,numero'))
print(cuenta_bancaria.operaciones('act'))