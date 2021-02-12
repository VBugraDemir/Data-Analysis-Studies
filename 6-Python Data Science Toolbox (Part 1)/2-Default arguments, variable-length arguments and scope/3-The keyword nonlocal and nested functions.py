def echo_shout(word):

    echo_word = word * 2
    print(echo_word)

    def shout():
        nonlocal echo_word
        echo_word = echo_word + "!!!"

    shout()
    print(echo_word)

echo_shout("hello")
