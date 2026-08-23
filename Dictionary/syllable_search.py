import pandas as pd
import random

letters = ['i', 'u', 'a', 'o', 'q', 'e', 'y', 'm', 'n', 'p', 'b', 't', 'd', 'k', 'g', 'l', 'w', 'r', 'v', 'z', 'j', 's', 'f']

df = pd.read_csv("syllables.csv")

def check_next_to(syllable):
    for i in range(len(syllable) - 1):
        if syllable[i] == syllable[i + 1]:
            return True
    return False

length = random.choice([2])
syllable = "".join(random.choices(letters, k=length))

while syllable in df["treeform"].values or check_next_to(syllable):
    length = random.choice([2])
    syllable = "".join(random.choices(letters, k=length))

print(syllable)
