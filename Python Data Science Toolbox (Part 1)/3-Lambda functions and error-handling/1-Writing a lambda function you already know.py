def echo_word(word1, echo):
    words = word1 * echo
    return words

print(echo_word("hey", 5))


# Writing labda function

echo_word = lambda word1, echo: word1 * echo
result = echo_word("hey", 5)
print(result)
