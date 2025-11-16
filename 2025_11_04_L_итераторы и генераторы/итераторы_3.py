with open("log_server/access.log", "r") as file:
    iterator = iter(file)
    for _ in range(10):
        print(next(iterator).strip())