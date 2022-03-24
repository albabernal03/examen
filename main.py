from clases.cuenta_vip import cuenta_bancaria_vip
from clases.cuenta import cuenta_bancaria
from clases.libro import Libro
from clases.plazo_fijo import fijo

if __name__ == "__main__":
  print(cuenta_bancaria_vip.cuenta('titular, fecha,numero'))
  print(cuenta_bancaria_vip.operaciones('act'))

if __name__ == "__main__":
  print(cuenta_bancaria.cuenta('titular, fecha,numero'))
  print(cuenta_bancaria.operaciones('act'))

if __name__ == "__main__":
  Libro()

if __name__ == "__main__":
  print(fijo.retirada('penalizacion, saldo, fecha_entrada, delta, fecha_vencimiento'))
  
  