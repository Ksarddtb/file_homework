from csv import DictWriter,DictReader
from os.path import exists

class NameError(Exception):
    def __init__(self, txt):
        self.txt=txt

def get_date():
    flag=False
    while not flag:
        try:
            first_name=input('Введите имя:')
            if len(first_name)<2:
                raise NameError('Short Name')
            last_name=input('Введите Фамилию:')
            if len(last_name)<2:
                raise NameError('Short Last Name')
            phone=input('Введите телефон:')
            if len(phone)<7:
                raise NameError('Error Phone')
        except NameError as err:
            print(err)
        else:
            flag=True
    return [first_name,last_name,phone]
def print_list(res):
    print('#\t','Имя\t','Фамилия\t','Телефон\t')
    index=1
    for row in res:
        print(str(index)+"\t"+str(row["Имя"]+"\t")+str(row["Фамилия"]+"\t")+str(row["Телефон"]+"\t"))
        index+=1
        # print(row[1]+"\t")
        # print(row[2]+"\t")
        
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
    
def migrate_row(filename):
    number=int(input('Введите номер строки:'))    
    filenew=str(input('Введите имя файла:'))+'.csv'
    res=read_file(filename)
    obj=res[number-1]
    create_file(filenew)
    write_file(filenew,[obj['Имя'],obj['Фамилия'],obj['Телефон']])
    return filenew

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
            print_list(read_file(filename))
        elif command == 'f':
            if not exists(filename):
                print('File not found create it')
                continue
            print_list(row_search(filename))
        elif command == 'd':
            if not exists(filename):
                print('File not found create it')
                continue
            print_list(row_delete(filename))
        elif command == 'u':
            if not exists(filename):
                print('File not found create it')
                continue
            update_row(filename)
            print_list(read_file(filename))
        elif command == 'c':
            if not exists(filename):
                print('File not found create it')
                continue
            newfile=migrate_row(filename)
            print_list(read_file(newfile))
            
main()