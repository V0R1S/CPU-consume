import psutil
import time
from colorama import init, Fore, Style

# Inicializa la librería
init()

# Función para obtener la temperatura de la CPU
def get_cpu_temp():
    # Obtener el uso de la CPU
    cpu_percent = psutil.cpu_percent()
    return cpu_percent

# Función para obtener la temperatura de la GPU
def get_gpu_temp():
    # Obtener el uso de la GPU
    gpu_percent = 0
    # Devolver el uso de la GPU
    return gpu_percent

# Bucle infinito para mostrar la información en tiempo real
while True:
    # Obtener la temperatura de la CPU y la GPU
    cpu_temp = get_cpu_temp()
    gpu_temp = get_gpu_temp()
    trafico_red = psutil.net_io_counters()

    porcentaje_trafico = (trafico_red.bytes_recv + trafico_red.bytes_sent) / trafico_red.bytes_recv
    
    # Mostrar la temperatura de la CPU en rojo
    print("Temperatura de la CPU: ", end="")
    print(Fore.GREEN + f"{cpu_temp}", end="")
    print(" grados")
    
    # Mostrar la temperatura de la GPU en verde
    print("Temperatura de la GPU: ", end="")
    print(Fore.RED + f"{gpu_temp}", end="")
    print(" grados")

    time.sleep(2)

    print(f"Porcentaje de tráfico de red: ", end="")
    print(Fore.YELLOW + f"{porcentaje_trafico}", end="")
    
    # Resetea el color del texto a su valor por defecto
    print(Style.RESET_ALL)
    
    # Esperar 1 segundo antes de volver a obtener la información
    time.sleep(1)
