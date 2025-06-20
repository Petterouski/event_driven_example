import time

def consume_event():
    while True:
        try:
            with open("events.txt", "r") as file:
                events = file.readlines()
            if events:
                print(f"Consumiendo evento: {events[-1].strip()}")
            else:
                print("Esperando eventos...")
        except FileNotFoundError:
            print("No hay eventos disponibles.")
        time.sleep(2)

if __name__ == "__main__":
    consume_event()