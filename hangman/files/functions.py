def match(letter, word):
    # Convert the word to underscore then make both to list
    word = list(word)
    mask = list('_' * len(word))

    i = 0
    while i < len(W):
        if W[i] == letter:
            mask[i] = word[i]
        i += 1
    return(''.join(mask))
