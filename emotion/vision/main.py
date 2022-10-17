import google.auth
from connection import process_consumer
import threading
 
credentials, project = google.auth.default()


# Uso de hilos para la conexion con el broker
consumer_thread = threading.Thread(target=process_consumer, args=())
consumer_thread.start()