# ("is2 Thi1s T4est 3a") to "Thi1s is2 3a T4est"
# %%
# my solution dint work


def order(sentence):
    sen = sentence.split()
    act_sen = []
    sum = 1
    for i in range(len(sen)):
        if str(sum) in sen[i]:
            sum = sum + i
            act_sen.append(sen[i])
    print(act_sen)
# %%
# my copied solution


def order(sentence):
    words = []
    for i in range(1, 10):
        for word in sentence.split():
            if str(i) in word:
                words.append(word)
    return " ".join(words)
# %%
# solution 1


def order(words):
    return ' '.join(sorted(words.split(), key=lambda w: sorted(w)))
