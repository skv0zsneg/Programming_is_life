def deco(func):
    print("I am decorator, thats why you read me first.")
    return func


@deco
def foo1():
    print("I am function foo1.")


@deco
def foo2():
    print("I am function foo2.")


def foo3():
    print("I am function foo2.")


def main():
    print("I am function main.")
    foo1()
    foo2()
    foo3()


if __name__ == "__main__":
    main()
