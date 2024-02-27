import subprocess
import pkgutil
import importlib


def mostrar_modulos_y_descripciones(paquete):
    """
    Muestra los módulos y sus descripciones dentro de un paquete.
    :param paquete: Nombre del paquete a utilizar
    :return: Descripción del contenido del paquete
    """
    print(f"Modulos en el paquete '{paquete.__name__}':")
    for loader, name, is_pkg in pkgutil.walk_packages(paquete.__path__):
        module = importlib.import_module(paquete.__name__ + '.' + name)
        print(f" - {name}: {module.__doc__}")


# Faltaria modificar el código para que pueda elegirse qué paquetes instalar

# Este código debería estar disponible en el README del repositorio de Github

# modules = ['auxiliar_functions', 'exploratory', 'extract', 'imports']

# path = 'https://github.com/DanyRoh/packages/blob/2574b96dc7e27c0eef7bc00bf77f75fff42dde48/analisisdatos/main/'

# url = 'https://github.com/DanyRoh/packages/blob/2574b96dc7e27c0eef7bc00bf77f75fff42dde48/analisisdatos/main/auxiliar_functions.py'

# Instalar el paquete o módulo desde la URL usando pip
# subprocess.run(['pip', 'install', url])


#%%
