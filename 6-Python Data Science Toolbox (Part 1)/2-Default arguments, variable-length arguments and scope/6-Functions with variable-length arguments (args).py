
def gibberish(*args):

    hodgepodge = ""

    for word in args:
        hodgepodge += word

    return hodgepodge

one_word = gibberish("luke")
many_words = gibberish("luke", "leia", "han", "obi", "darth")

print(one_word)
print(many_words)
