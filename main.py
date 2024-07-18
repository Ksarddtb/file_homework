from csv import DictWriter,DictReader


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
