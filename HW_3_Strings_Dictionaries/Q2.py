def change_tone(phrase, new_tone):
    if phrase[-1] == '.':
        str = phrase[:-1]
    else:
        str = phrase

    if new_tone is True:
        if str[-2:] == "?!":
            str = str[:-2] + "?"
        elif str[-1] == '!':
            str = str[:-1] + '?'
        elif str[-1] == '?':
            str = str[:-1] + '!'
        else:
            str = str + "?!"
    else:
        if str[-2:] == "?!":
            str = str[:-2] + "!"
        elif str[-1] == '!':
            str = str[:-1] + '?!'
        elif str[-1] == '?':
            str = str[:-1] + '?'
        else:
            str = str + "?"

    if phrase[-1] == '.':
        str = str + '.'
    return str


def be_polite(paragraph):
    new_paragraph = []
    end_dot = False
    if paragraph[-1] == '.':
        end_dot = True

    sentences = [sen + "." for sen in paragraph.split('.')]
    if end_dot is False:
        sentences[-1] = sentences[-1][:-1]

    for sentence in sentences:
        str = change_tone(sentence, True)
        new_paragraph.append(str)
    return " ".join(new_paragraph)


print(change_tone(phrase="You don’t mess with cats!", new_tone=True))
print(change_tone(phrase="prepare to takeoff?!", new_tone=False))
print(be_polite(paragraph="I’m not mad!. I want soup?"))
