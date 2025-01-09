def prefixCount(words, pref):
        n=len(words)
        count= 0
        for i,w1 in enumerate(words):
            if w1.startswith(pref):
                count +=1
        return count

#Usage
words=["pay","attention","practice","attend"]
pref="at"
print(prefixCount(words,pref))