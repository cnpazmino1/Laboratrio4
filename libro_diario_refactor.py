class LibroDiario:
    ''' Clase para registrar egresos e ingresos'''

    def __init__(self):
        ''' Construcctor de la clase '''
        self.transacciones = []

    def agregar(self,fecha, descripcion,monto,tipo):
        ''' Agregar una transaccion '''
        self.transacciones.append({
            "fecha": fecha,
            "descripcion": descripcion,
            "monto": monto,
            "tipo": tipo
        })

    def resumen(self):
        ''' calcula el total de ingresos y egresos '''
        ingresos = 0
        egresos = 0
        for t in self.transacciones:
            if t["tipo"]=="ingreso":
                ingresos+=t["monto"]
            else:
                egresos+=t["monto"]
        return "Total ingresos: " + str(ingresos) + " Total egresos: " + str(egresos)

