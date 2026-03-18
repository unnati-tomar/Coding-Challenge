 #Calculate electricity bill based on units consumed
def bill(u):
    return u*5 if u<=100 else u*10
print(bill(150))
