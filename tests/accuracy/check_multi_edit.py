import linedit

lines = [
    (4, 'Test Line Edit'),
    (1, 'Test Line Edit'),
    (13, 'Test Line Edit'),
    (500, 'Test Line Edit'),
    (31, 'Test Line Edit'),
    (501, 'Test Line Edit'),
    (77, 'Test Line Edit'),
    (999, 'Test Line Edit'),
    (21, 'Test Line Edit'),
    (20, 'Test Line Edit')
]

linedit.medit('test_pre.txt', lines)

with open('test_pre.txt') as updated:
    updatedd = updated.readlines()
    with open('test_good.txt') as good:
        goodd = good.readlines()
        for i in range(len(goodd)):
            if updatedd[i] != goodd[i]:
                print(f'good: {goodd[i]} ---- pre: {updatedd[i]}')