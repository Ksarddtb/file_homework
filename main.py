from csv import DictWriter,DictReader
from os.path import exists

def get_date():
    first_name=input('Введите имя:')
    last_name=input('Введите Фамилию:')
    phone=input('Введите телефон:')
    return [first_name,last_name,phone]

def create_file(filename):
    with open(filename,'w',encoding='utf-8') as data:
        f_w=DictWriter(data,fieldnames=['Имя','Фамилия','Телефон'])
        f_w.writeheader()
        
def read_file(filename):
    with open(filename,'r',encoding='utf-8') as data:
        f_r=DictReader(data)
        return list(f_r)

def standart_write(filename,res):
    with open(filename,'w',encoding='utf-8') as data:
        f_w=DictWriter(data,fieldnames=['Имя','Фамилия','Телефон'])
        f_w.writeheader()
        f_w.writerows(res)

def write_file(filename,lst):
    res=read_file(filename)
    obj={'Имя':lst[0],
         'Фамилия':lst[1],
         'Телефон':lst[2]}
    res.append(obj)
    standart_write(filename,res)

def row_search(filename):
    last_name=input('Введите Фамилию:')    
    res=read_file(filename)
    for row in res:
        if last_name==row['Фамилия']:
            return row
    return "row not found"

def row_delete(filename):
    number=int(input('Введите номер строки:'))    
    res=read_file(filename)
    res.pop(number-1)
    standart_write(filename,res)

def update_row(filename):
    number=int(input('Введите номер строки:'))    
    res=read_file(filename)
    lst=get_date()
    res[number-1]={'Имя':lst[0],
         'Фамилия':lst[1],
         'Телефон':lst[2]}
    standart_write(filename,res)

filename='phone.csv'

def main():
    while True:
        command=input('Введите комаду:')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(filename):
                create_file(filename)
            write_file(filename,get_date())
        elif command == 'r':
            if not exists(filename):
                print('File not found create it')
                continue
            print(read_file(filename))
        elif command == 'f':
            if not exists(filename):
                print('File not found create it')
                continue
            print(row_search(filename))
        elif command == 'd':
            if not exists(filename):
                print('File not found create it')
                continue
            print(row_delete(filename))
        elif command == 'u':
            if not exists(filename):
                print('File not found create it')
                continue
            update_row(filename)
            print(read_file(filename))
            
main()