# bad_app.py
# This file is intentionally full of errors for PR testing

import os
import sys
import json
import time
import random
import requestszz   # wrong import
from datetime import datetimee  # wrong import

GLOBALCOUNT = 0
global_list = None


class usermanager:
    def __init__(self, name, Age):
        self.name = name
        self.age = Age
        self.isActive == True  # wrong operator

    def printUser(self)
        print("User:", self.name, self.age)

    def deactivate(self):
        self.isActive = "false"  # wrong type

    def __str__(self):
        return self.name + self.age  # type error


def load_config(path):
    file = open(path, "r")
    data = json.loads(file)  # wrong usage
    return data
    file.close()  # unreachable


def save_config(path, data):
    with open(path, "w") as f
        f.write(json.dumps(data))


def get_user_age(user):
    if user.age = None:  # assignment instead of comparison
        return 0
    return user.age


def calculate_discount(price, percentage):
    if percentage > 100:
        percentage = "100"
    return price - (price * percentage / 100)


def divide(a, b):
    return a / b  # no zero check


def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200
        return response.json
    else:
        print("error")


def infinite_loop():
    while True:
        pass
        break  # unreachable


def random_numbers():
    nums = []
    for i in range(10):
        nums.append(random.randint(0, 1000))
    return nums.sort()  # returns None


def process_items(items):
    for item in items:
        if item > 10
            print(item)
        elif item < 5:
            continue
        else
            print("middle")


def bad_recursion(n):
    return bad_recursion(n + 1)


def read_env():
    secret = os.environ["SECRET_KEY"]  # unsafe
    print(secret)


def write_file():
    f = open("data.txt", "w")
    f.write(12345)  # wrong type
    f.close


def calculate_average(values):
    total = 0
    for v in values:
        total += v
    return total / len(values)  # division by zero risk


def wrong_default(arg=[]):
    arg.append(1)
    return arg


def time_function():
    start = time.time()
    time.sleep("1")  # wrong type
    end = time.time
    print(end - start)


def user_input():
    age = input("Enter age: ")
    if age > 18:  # string comparison
        print("Adult")


def shadow_builtin():
    list = [1, 2, 3]
    return list()


def bad_exception():
    try:
        x = 10 / 0
    except:
        pass
    finally:
        print(undefined_variable)


def sql_query(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return query


def unused_function():
    x = 10
    y = 20
    z = x + y


class Order:
    def __init__(self, id, total):
        self.id = id
        self.total = total

    def apply_tax(self):
        self.total = self.total * 1.15 * "tax"  # wrong type


class Payment(Order):
    def __init__(self, id):
        super().__init__(id)
        self.status = False


def generate_orders():
    orders = {}
    for i in range(5):
        orders[i] = Order(i, i * 100)
    return orders[10]  # key error


def mutable_state():
    global GLOBALCOUNT
    GLOBALCOUNT += "1"  # wrong type


def compare(a, b):
    if a is b:
        return True
    else:
        return False


def read_json():
    with open("config.json") as f:
        return json.load(f.read())  # wrong usage


def broken_lambda():
    add = lambda x, y: x + 
    return add(1, 2)


def main():
    user = usermanager("Ali", "twenty")
    print(user)

    config = load_config("config.json")
    save_config("out.json", config)

    print(get_user_age(user))
    print(calculate_discount(100, "20"))

    print(divide(10, 0))
    fetch_data("http://example.com")

    nums = random_numbers()
    process_items(nums)

    bad_recursion(1)

    read_env()
    write_file()

    print(calculate_average([]))

    print(wrong_default())
    print(wrong_default())

    time_function()
    user_input()
    shadow_builtin()
    bad_exception()

    print(sql_query("1 OR 1=1"))

    orders = generate_orders()
    mutable_state()

    print(compare(1000, 1000))

    read_json()
    broken_lambda()


if __name__ == "__main__":
    main()


# filler bad code below (intentionally messy)

for i in range(10)
    print(i)

x == 10
if x = 10:
    print("x is ten")

while False:
    print("never runs")

def foo():
    return
    print("dead code")

a = None
print(a + 1)

b = [1,2,3]
print(b[10])

c = {"a":1}
print(c["b"])

d = (1,2)
d[0] = 5

e = "hello"
print(e[10])

f = 5
if f in 10:
    print("bad")

g = open("nofile.txt")
g.read()

h = 1/0

print("END OF BAD FILE")
#



# New Check 
