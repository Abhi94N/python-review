

try:
    f = open('test_file.txt')
    if f.name == 'currupt_file.txt':
        raise Exception
    #var = bar
except FileNotFoundError as e:
    print(e)
# general error
except Exception as e:
    print('Error', e)
else:
    print(f.read())
finally:
    f.close()
    print("Excecuting Finally..")