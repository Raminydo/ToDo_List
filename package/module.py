


from os import system
from typing import Hashable


def get_input(field: str, is_empty: bool = True) -> str:
    
    error_list = []

    while True:
        
        val = input(f'\nEnter {field}: ')
        system('cls')

        if not is_empty and val == '':
            error_list.append(f'{field} is empty')

        if not error_list:
            return val
        
        print(*error_list, sep='\n')
        error_list.clear()



def show_list(data: list[dict], subject: str) -> None:

    show_column = ['id', 'title', 'description', 'date']
                    
    print(*show_column, sep='\t')
    print('-'*30)

    for subject in data:

        for index in show_column:
            print(subject[index], end='\t')
            
        print()

    print('-'*30)



def search(data: list[dict], subject: str, method: str, val: Hashable, list: list = [],
           search_inside_string: bool = False) -> None:
    
    for subject in data:

        if not search_inside_string:

            if subject[method] == val:

                list.append(subject)

        else:
            # to check each word in a string
            for text in subject[method].split(' '):

                if text == val:

                    list.append(subject)
                    break      


