import threading
import json
import os
import pika
import mysql.connector



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
    print("Recibiendo la informacion....")
    # Toma de datos
    employee_name = received_message['name']
    employee_image = received_message['image']
    employee_emotion = received_message['emotion']
    print("Se recibio la informacion....")
    # llama la funcion de vision
    print("Guardado datos....")
    #ingresar datos a la base ******************************************************
    db = mysql.connector.connect(host = 'mysql', user = 'root', password = 'root', port = 3306)
    db_conn = db.cursor()
    #s_query = "insert into images(+imageName,dateAdded,image) values (" + employee_image"," +CURRENT_TIMESTAMP, image_data);"
    s_query = "call addImage("+str(employee_name)+","+str(employee_image)+");"
    db_conn.execute(s_query)
    db_conn.close()
    db.close()

    db_conn = db.cursor()
    s_query = "call addResult("+str(employee_name)+","+str(employee_emotion)+");"
    db_conn.execute(s_query)
    db_conn.close()
    db.close()
    print("Datos guardados....")
    #llamar base de datos para obtener imagenes ***********************************
    print("Enviando datos....")
    #agrega los datos al json

    db_conn = db.cursor()
    s_query = "call viewAll();"
    db_conn.execute(s_query)
    message = json.dumps(db_conn)
    db_conn.close()
    db.close()
    # envia el dato de la publicacion
    publisher_thread = threading.Thread(target=publisher, args=(message,))
    publisher_thread.start()
def consumer():
    """
    Funcion encargada de crear la conexion con el broker para obtener informacion
    Input:
        -la cola de rabbit
    Output:
        - la conexion
    """
    db = mysql.connector.connect(host = 'mysql', user = 'root', password = 'root', port = 3306)
    db_conn = db.cursor()
    s_query = "call viewAll();"
    db_conn.execute(s_query)
    for a_row in db_conn:
        print(a_row)
    db_conn.close()
    db.close()

    # Variables de rabbit
    host = os.environ['RABBIT_HOST']
    port = os.environ['RABBIT_PORT']
    queue_consumer = os.environ['RABBIT_PRODUCER_QUEUE']
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