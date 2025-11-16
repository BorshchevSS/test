def count_up_to(limit):
    count = 1
    while count <= limit:
        yield count
        count += 1

for n in count_up_to(5):
    print(n)