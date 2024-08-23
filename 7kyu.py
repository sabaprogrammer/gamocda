#last survivor
def last_survivor(letters, coords): 
    letters = list(letters)
    for pos in coords:
        del letters[pos]

    return letters[0]

str_ = "zbk"
arr = [0, 1]
print(last_survivor(str_, arr))  
    