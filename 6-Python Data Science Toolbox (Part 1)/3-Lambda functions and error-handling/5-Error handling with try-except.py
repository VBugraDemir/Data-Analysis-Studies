def shout_echo(word1, echo=1):
    shout_words = ""
    try:
        echo_word = word1 * echo

        shout_words = echo_word + "!!!"
    except:
        print("word1 must be a string and echo must be an integer.")
    return shout_words

print(shout_echo("particle", echo="accelerator"))
