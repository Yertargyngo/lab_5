from random import shuffle
 
lot_san = [*range(1, 50)]
shuffle(lot_san)
print(sorted(lot_san[:6]))