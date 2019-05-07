with open('test_one_thousand.txt', 'w') as file:
   for i in range(1000):
       file.writelines("Test Test Test Test Test Test Test Test Test\n")

with open('test_one_hundred_thousand.txt', 'w') as file:
   for i in range(100000):
       file.writelines("Test Test Test Test Test Test Test Test Test\n")

with open('test_one_million.txt', 'w') as file:
   for i in range(1000000):
       file.writelines("Test Test Test Test Test Test Test Test Test\n")
