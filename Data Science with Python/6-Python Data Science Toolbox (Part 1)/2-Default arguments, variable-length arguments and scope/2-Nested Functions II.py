def echo(n):

    def inner_echo(word1):
        return word1 * n
    return inner_echo

twice = echo(2)
thrice = echo(3)

print(twice("hello"), thrice("hello"))
