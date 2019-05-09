with open('test_pre.txt', 'w') as file:
   for i in range(1000):
       file.writelines("Test Test Test Test Test Test Test Test Test\n")

li = [4,1,13,500,31,501,77,999,21,20]

with open('test_good.txt', 'w') as file:
   for i in range(1000):
        if i+1 in li:
           file.writelines('Test Line Edit\n')
        else:
            file.writelines("Test Test Test Test Test Test Test Test Test\n")