# It's about defining my own functions so that is not that important

# Printing the result in the function
def shout(word):
    """Print a string with three exclamation marks"""
    shout_word = word + '!!!'
    print(shout_word)

shout("congratulations")


def shout(word):
    """Return a string with three exclamation marks"""
    shout_word = word + "!!!"
    return shout_word
yell = shout("congratulations")
print(yell)
