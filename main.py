import pika, sys, os

def main():
    credentials = pika.PlainCredentials("guest","guest")
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq',port=5672, credentials=credentials))
    channel = connection.channel(channel_number=1)

    # channel.queue_declare(queue='publisher')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body, flush=True)

    channel.basic_consume(queue='publisher', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C',  flush=True)
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted', flush=True)
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
      