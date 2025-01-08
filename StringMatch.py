def stringMatching(words):
    result = []
    for w1 in words:
        for w2 in words:
            if w1 != w2 and w1 in w2:
                result.append(w1)
                break  # No need to check further if `w1` is already a substring
    return result

#example
words=["mass","as","hero","superhero"]
print(stringMatching(words))