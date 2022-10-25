def print_chars(phrase, repeat):
    """
    Bubble Sort
    :param phrase:
    :param repeat:
    :return:
    """
    swapped = False
    phrase = list(phrase)
    for i in range(len(phrase) - 1):
        for j in range(len(phrase) - i - 1):
            if ord(phrase[j]) > ord(phrase[j+1]):
                swapped = True
                phrase[j], phrase[j+1] = phrase[j+1], phrase[j]
        if not swapped:
            break
    if repeat is True:
        return phrase
    else:
        return list(dict.fromkeys(phrase))


print(print_chars(phrase="Bojack you are a crazy horse", repeat=True))
print(print_chars(phrase="Bojack you are a crazy horse", repeat=False))