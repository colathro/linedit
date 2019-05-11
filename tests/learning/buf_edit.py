def bufedit(file, number, line):
    import os
    tempfile = file + '.new'
    with open(file, 'r') as r:
        with open(tempfile, 'w') as w:
            i = 0
            while True:
                i += 1
                origline = r.readline()
                if origline == '':
                    break
                if i == number:                             
                    w.writelines(f"{line}\n")
                else:
                    w.writelines(origline)
    try:
        os.remove(file)
        os.rename(tempfile, file)
    except:
        print('error')

if __name__ == '__main__':
    bufedit('/Users/colathro/Development/linedit/tests/learning/test_one_thousand.txt', 3, 'test')
