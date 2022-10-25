def init_dict(known_words):
    dic = {}
    for word in known_words:
        dic[word] = word
    return dic


def add_corrections(spell_check_dict, rules):
    corrections = []
    for word in spell_check_dict.keys():
        for rule in rules:
            corrections.append(spelling_errors(word, rule))
    # corrections = [[x for x in ele] for ele in corrections if ele != []]
    corrections = sum(corrections, [])
    spell_check_dict.update(corrections)  # add to the dict with update method (input: list of tuples(key: value))


def spelling_errors(word, rule):
    pairs = []
    for i in range(len(word)):
        if word[i] == rule[0]:  # If letter 1 found
            bad_word = word[0:i] + rule[1] + word[i + 1:]
            subtitution = (bad_word, word)
            pairs.append(subtitution)
    return pairs


def correct_spelling(text, dict):
    corrected_words = []
    for word in text.split():
        corrected_words.append(dic[word])
    return " ".join(corrected_words)


known_words = ['the', 'in', 'of', 'center', 'we', 'here', 'are', 'town']
rules = [('e', 'r'), ('e', 'w'), ('a', 's'), ('o', 'p')]
dic = init_dict(known_words)
text = 'hwre ww sre in thr centrr pf tpwn'
add_corrections(dic, rules)
print(correct_spelling(text, dic))
