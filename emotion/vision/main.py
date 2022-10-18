import threading
import google.auth
from connection import consumer
credentials, project = google.auth.default()
# Uso de hilos para la conexion con el broker
consumer_thread = threading.Thread(target=consumer, args=())
consumer_thread.start()
