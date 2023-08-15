
# Напишите функцию, которая сереализует содержимое 
# текущей директории в json-файл. # В файле должен храниться список словарей, 
# словарь описывает элемент внутри директории: # имя, расширение, тип. 
# Если элемент - директория, то только тип и имя

import json
import os
os.system('cls')

def serial_func(directory):    
    dir_list = os.listdir(directory)
    res_list = []
    for obj in dir_list:
        if os.path.isfile(obj):
            res_list.append({
                'name': '.'.join(str(obj).split('.')[:-1]),
                'extension': '.' + str(obj).split('.')[-1],
                'type': 'file'
                })
        else:
            res_list.append({
                'name': str(obj),            
                'type': 'directory'
                })

    with open('result.json', 'w') as res_j:
        json.dump(res_list, res_j, indent=4)    

if __name__ == '__main__':
    serial_func(os.getcwd())