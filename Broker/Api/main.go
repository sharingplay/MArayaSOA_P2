package main


import (
	"encoding/json"
	"fmt"
	"strings"
	"net/http"
	log "github.com/sirupsen/logrus"
	"github.com/streadway/amqp"
	"os"
)

var rabbit_host = os.Getenv("RABBIT_HOST")
var rabbit_port = os.Getenv("RABBIT_PORT")
var rabbit_queue = os.Getenv("RABBIT_CONSUMER_QUEUE")

func enableCors(w* http.ResponseWriter) {
	(*w).Header().Set("Access-Control-Allow-Origin", "*")
}

func createNewRecord(msg []byte) {
	// w.Header().Add("Content-Type", "JSON")
	// reqBody, _ := ioutil.ReadAll(r.Body)
	// err := json.Unmarshal(reqBody, &newRecord)
	var newRecord record
	err := json.Unmarshal(msg, &newRecord)

	if err != nil {
		panic(err.Error())
	}

	var newEmpleado empleado
	for i := 0; i < len(newRecord.Empleados); i++ {
		newEmpleado = newRecord.Empleados[i]

		insert, err := db.Query("call addImage @imageName = 'imagen de prueba', @image = 'texto de prueba';
		INSERT INTO EMPLEADO_EMOTIONS (create_time, name, emotion) VALUES ('" + fecha + "','" + newEmpleado.Nombre + "','" + newEmpleado.Emocion + "')")

		if err != nil {
			panic(err.Error())
		}

		fmt.Println("Insertado record bien")
		defer insert.Close()
	}
}

func consume() {	

	conn, err := amqp.Dial("amqp://guest:guest@" + rabbit_host + ":" + rabbit_port +"/")

	if err != nil {
		log.Fatalf("%s: %s", "Failed to connect to RabbitMQ", err)
	}

	ch, err := conn.Channel()

	if err != nil {
		log.Fatalf("%s: %s", "Failed to open a channel", err)
	}

	q, err := ch.QueueDeclare(
		rabbit_queue, // name
		true,   // durable
		false,   // delete when unused
		false,   // exclusive
		false,   // no-wait
		nil,     // arguments
	)

	if err != nil {
		log.Fatalf("%s: %s", "Failed to declare a queue", err)
	}

	fmt.Println("Channel and Queue established")

	defer conn.Close()
	defer ch.Close()

	msgs, err := ch.Consume(
		q.Name, // queue
		"",     // consumer
		false,   // auto-ack
		false,  // exclusive
		false,  // no-local
		false,  // no-wait
		nil,    // args
	  )

	if err != nil {
		log.Fatalf("%s: %s", "Failed to register consumer", err)
	}

	forever := make(chan bool)

	go func() {
		for d := range msgs {
			log.Printf("Received a message: %s", d.Body)
			d.Ack(true)
			createNewRecord(d.Body)
		}
	  }()
	  
	  fmt.Println("Running...")
	  <-forever
}

func main() {
	consume()
}
