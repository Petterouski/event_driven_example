import time
import random

def produce_event():
    while True:
        event = f"Evento-{random.randint(1, 100)}"
        print(f"Produciendo evento: {event}")
        # Simular envío de evento
        with open("events.txt", "a") as file:
            file.write(event + "\n")
        time.sleep(2)

if __name__ == "__main__":
    produce_event()