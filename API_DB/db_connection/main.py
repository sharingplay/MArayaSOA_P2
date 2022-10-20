import threading
from db_conn import consumer
# Uso de hilos para la conexion con el broker
print("hola")
consumer_thread = threading.Thread(target=consumer, args=())
consumer_thread.start()
