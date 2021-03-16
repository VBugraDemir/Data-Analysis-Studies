def three_shouts(word1, word2, word3):

    def inner(word):
        return word + "!!!"
    return (inner(word1), inner(word2), inner(word3))

print(three_shouts("a", "b", "c"))
