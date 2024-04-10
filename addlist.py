L1 = [5, 7, 8]
L2 = [7, 8, 9]

carryover = 0
L = []

for num1, num2 in zip(L1, L2):
    total = num1 + num2 +carryover
    
    if total > 9:
        carryover = total //10
        total %= 10
    else:
        carryover = 0
        
    L.append(total)
if carryover > 0:
    L.append(carryover)

print(L)
        
        
        