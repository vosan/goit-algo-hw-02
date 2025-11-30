from queue import Queue
from uuid import uuid7

q = Queue()


def generate_request():
    uuid = uuid7()
    q.put(uuid)
    return uuid


def process_request():
    if not q.empty():
        return q.get()
    else:
        return None


print("Welcome to the request processing system!")
print("Commands: "
      "\n\tall - show all requests"
      "\n\tg - generate request"
      "\n\tp - process request"
      "\n\tq - quit")

while True:
    match input("Enter command: "):
        case "q":
            break
        case "g":
            request = generate_request()
            print(f"\tRequest generated: {request}")
        case "p":
            request = process_request()
            if request is None:
                print("\tQueue is empty")
                continue
            print(f"\tRequest processed: {request}")
        case "all":
            for request in q.queue:
                print(f"\t{request}")
        case _:
            print("\tUnknown command")
