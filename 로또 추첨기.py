import random

duplication = [ 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0 ]

lotto = [ 0, 0, 0, 0, 0, 0 ]
idx = 0

while idx < 6:
    num = random.randrange(1, 46)
    
    if duplication[num - 1] == 0:
        lotto[idx] = num
        duplication[num - 1] = 1
        idx += 1
    
    elif duplication[num - 1] == 1:
        idx -= 1
        
lotto.sort()

print("         LOTTO")
print("     오늘의 행운 번호\n", lotto)
