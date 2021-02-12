
def shout_echo(word1, echo=1, intense=False):

    echo_word = word1 * echo

    if intense == False:
        echo_word_new = echo_word + "!!!"
    else:
        echo_word_new = echo_word.upper() + "!!!"
    return echo_word_new

with_big_echo = shout_echo("Hey", echo=5, intense=True)
with_no_echo = shout_echo("Hey", intense=True)
print(with_big_echo)
print(with_no_echo)
