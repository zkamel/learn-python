def greeting():
    def sayhello():
        return "Hello"
    return sayhello
hello=greeting()

print(hello())

