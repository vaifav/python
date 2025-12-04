def greet(name):
    print(f"Hello {name}")


greet("John")

num = 10
double = lambda x: x * 2
print(double(num))


def logs(level, *msgs, **userDetails):
    print(f"level - {level}, msgs - {msgs}, user details - {userDetails}")


logs(10, "start", "continuing", name="John", age=30, gender="male")


def logIn(func):
    def wrapper(*args, **kwargs):
        print(f"user logs in...")
        func(*args, **kwargs)

    return wrapper


def auth(func):
    def wrapper(*args, **kwargs):
        print(f"user auth ...")
        func(*args, **kwargs)

    return wrapper


@logIn
@auth
def user(name):
    print(name)


user("Mark")

print(sum.__doc__)