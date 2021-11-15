def new_entry():
    file = open('shapes.txt','w')
    file.write('')
    file.close()

def end_entry():
    file = open('shapes.txt','a')
    file.write('\n')
    file.close()

def get_previous():
    file = open('shapes.txt', 'r')
    red = file.read()
    print(red)
    file.close() 

def written(property,value):  
    file = open('shapes.txt','a')
    file.write(f'{property} : {value}\n')
    file.close()



