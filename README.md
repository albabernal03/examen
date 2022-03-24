# examen

```
from datetime import datetime
class cuenta_bancaria_vip:

    
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
        saldo = 10000
        saldo_negativo = saldo + 2000
        if act== 'no':
            print('De acuerdo, muchas gracias y hasta la proxima!')
        if act == 'ingresar':
            ingreso = float(input('Introduzca la cantidad que desee ingresar:'))
            saldo = ingreso 
            print('Su saldo es', saldo, '€')
        if act == 'retirar':
            retiro = float(input('Introduca la cantidad que desea retirar:'))
            if retiro > saldo_negativo:
                print('No tiene suficiente dinero para retirar dicha cantidad')
            else:
                saldo = saldo - retiro
                print('Su saldo es', saldo, '€')
        if act == 'transferir':
            transferir = float(input('Introduce la cantidad que desea transferir:'))
            if transferir >  saldo_negativo:
                print('No tiene suficiente saldo en la cuenta:')
            else:
                saldo = saldo - transferir
                print('La cantidad que ha transferido es:', transferir)
                print('Su saldo es', saldo, '€')

print(cuenta_bancaria_vip.cuenta('titular, fecha,numero'))
print(cuenta_bancaria_vip.operaciones('act'))

```

```
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

```


```
class Libro():
    def __init__(self,nombrelibro, codigo, fecha_prestamo, fecha_devolucion, nombre_lector):
        self.nombrelibro = nombrelibro
        self.codigo = codigo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.nombre_lector = nombre_lector

    def setnombrelibro(self,nombrelibro):
        self.nombrelibro= nombrelibro

    def getnombrelibro(self):
        return self.nombrelibro

    def setcodigo(self,codigo):
        self.codigo= codigo

    def getcodigo(self):
        return self.codigo
    
    def setfecha_prestamo(self,fecha_prestamo):
        self.fecha_prestamo= fecha_prestamo

    def getfecha_prestamo(self):
        return self.fecha_prestamo

    def setfecha_devolucion(self,fecha_devolucion):
        self.fecha_devolucion= fecha_devolucion

    def getfecha_devolucion(self):
        return self.fecha_devolucion
    
    def setnombrelector(self,nombre_lector):
        self.nombre_lector= nombre_lector

    def getnombrelibro(self):
        return self.nombre_lector
```

```
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
        else:
            print('No puede realizar la operación, se ha superado la fecha de vencimiento')

print(fijo.retirada('penalizacion, saldo, fecha_entrada, delta, fecha_vencimiento'))

    

```
