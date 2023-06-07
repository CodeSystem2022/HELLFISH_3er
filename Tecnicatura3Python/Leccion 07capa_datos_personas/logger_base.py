import logging as log # Es una herramienta de registro de informacion durante la ejecucion de codigo.
#Recordar la tabla de valores y niveles del logging
log.basicConfig(level=log.DEBUG,
                format='%(asctime)s:%(levelname)s [%(filename)s:%(lineno)s] %(message)s', # Esta linea nos va a indicar las caracteristicas del error que se va a enviar para identificarlo
                datefmt='%I:%M:%S %p', # Aca reformatea la hora del asctime de arriba
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])  # Debido a este nivel se van a ejecutar los msj

# LLamamos una config basica: pero vamos a hacer que solo se ejecuten las lineas en este archivo (lo vamos a usar para importar despues)
if __name__ == '__main__': # Esta linea es la que verifica que se ejecute el script directo y no importado
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel warning')
    log.error('Mensaje a nivel error')
    log.critical('Mensaje a nivel critical')

