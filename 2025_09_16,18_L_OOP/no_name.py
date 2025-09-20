def test(*args): # *-распаковка
    print(*args)

test(1,2,3)
# args - неименованные (преобразуются в картеж)

def sum_num(*args):
    res = 0
    for m in args:
        res += m
    return  res
print(sum_num(1,2,3,4,5,6,9))

def user_info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")
user_info(name="Sacha", age = "55", city = "NSK")

#def func(simple_args, *args, simple_kwargs, **kwargs)

user = {"name":"Sacha", "age":55, "city": "NSK"}
print(user.items())
