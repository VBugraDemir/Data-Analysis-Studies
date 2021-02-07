
def shout_echo(word1, echo=1):
    echo_word = word1 * echo
    shout_word = echo_word + "!!!"
    return shout_word

no_echo = shout_echo("Hey")

with_echo = shout_echo("Hey", 5)

print(no_echo)
print(with_echo)
