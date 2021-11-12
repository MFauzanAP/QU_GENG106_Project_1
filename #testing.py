


def entry(property, val,file_name):
    file = open(f'{file_name}.txt', 'a')
    file.write(f'{property} : {val}\n')
    file.close()

def end_entry(file_name):
    file = open(f'{file_name}.txt', 'a')
    file.write('-----------------')
    file.close()

def get_entry(file_name):
    file = open(f'{file_name}.txt', 'r')
    red = file.read()
    print(red)
    file.close() 


