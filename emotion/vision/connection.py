import pika
import threading
import json
import os
from vision import analyze_emotion

def received(ch, method, properties, body):
    """
    Funcion encargada de recibir los mensajes y ejecutarlos
    Entradas:
        -ch: type
        -method: type
        -properties: type
        -body:string 

    Output:
        -mensaje: Json
    """
    received_message = json.loads(body)
    print("Se recibio la informacion....")
    print("Analaizando datos....")
    # Toma de datos
    employee_name = received_message['name']
    employee_image = received_message['image']
    print("Se recibio la informacion....")
    # llama la funcion de vision
    print("Analaizando datos....")
    emotion = analyze_emotion(employee_image)
    print("Emociones Analizadad....")
    print("Enviando datos....")
    #agrega los datos al json
    json_object = {
        "name": employee_name,
        "employees": emotion
    }
    print(json_object)
    message = json.dumps(json_object)
    # envia el dato de la publicacion
    publisher_thread = threading.Thread(target=publisher, args=(message,))
    publisher_thread.start()

def process_consumer():
    """
    Funcion encargada de crear la conexion con el broker para obtener informacion
    Input: 
        -la cola de rabbit
    Output:
        - la conexion
    """
    # Variables de rabbit
    host = os.environ['RABBIT_HOST']
    port = os.environ['RABBIT_PORT']
    queue_consumer = os.environ['RABBIT_CONSUMER_QUEUE']
    #conexion con el broker
    connection_parameters = pika.ConnectionParameters(host=host, port=port)
    connection = pika.BlockingConnection(connection_parameters)
    # Canal de conexion default
    channel = connection.channel() 
    # Declaracion del queue
    channel.queue_declare(queue=queue_consumer)
    channel.basic_consume(queue=queue_consumer, auto_ack=True, on_message_callback=received)
    print("Se inicia la conexion.....")
    channel.start_consuming()  

def publisher(message_body):
    """
    Crea una conexion pero de publicacion 
    Input:
        - Message _body: type
    Output:
        - la cola
    """
    # Variables de rabbit
    host = os.environ['RABBIT_HOST']
    port = os.environ['RABBIT_PORT']
    queue_producer = os.environ['RABBIT_PRODUCER_QUEUE']
    # Creacion de conexion con el broker
    connection_parameters = pika.ConnectionParameters(host=host, port=port)
    connection = pika.BlockingConnection(connection_parameters)
    # Canal de conexion default
    channel = connection.channel()
    # Declaracion de colas producer
    channel.queue_declare(queue=queue_producer)
    channel.basic_publish(exchange='', routing_key=queue_producer, body=message_body)
    print("Los datos fueron publicados....")
    connection.close()