

"""
To Do List Manager

A simple terminal-based ToDo list

including actions:
    - add todo
    - show all saved todos
    - inactive todo
    - edit todo
    - search todo
    - exit

Attention:
    After exiting the programm, all saved data will be lost.

"""


from os import system
from datetime import date
from package.module import get_input, show_list, search


todo_list = []
active_list = []
inactive_list = []
search_list = []
message_list = []

number = 0

while True:

    print('\n\nTo Do List')
    print('-'*15)
    print('1. Add ToDo')    
    print('2. Show ToDo')   
    print('3. Inactive ToDo')   
    print('4. Edit ToDo')   
    print('5. Search ToDo') 
    print('6. Exit')    
    print('-'*15)

    menu = input('Enter menu: ')
    system('cls')

    
    match menu:

        case '1':
            
            while True:

                system('cls')

                # Number
                number += 1


                #region Title
                while True:

                    title = get_input(field='Title', is_empty=False)              

                    if todo_list:
                        search(todo_list, todo, 'title', title, search_list)

                        if search_list:
                            print('This title already exists! Try another one.')
                            search_list.clear()

                        else:
                            break

                    else:
                        break

                search_list.clear()
                #endregion
                    

                # Description
                description = get_input(field='Description')


                #region date
                print('Date Process:')
                year = int(get_input('Year', False))

                print('Date Process:')
                month = int(get_input('Month', False))

                print('Date Process:')
                day = int(get_input('Day', False))

                date_ = str(date(year, month, day))
                #endregion


                # Activation
                active = True


                todo = {
                    'id' : number,
                    'title' : title,
                    'description' : description,
                    'date' : date_,
                    'activation' : active
                    }

                todo_list.append(todo)



                #region get input again
                again = True

                while True:

                    input_again = input('Do you want to add another one (yes/no)? ')
                    system('cls')

                    if input_again == 'yes':
                        break

                    elif input_again == 'no':
                        again = False
                        break

                if not again:
                    break
                #endregion

        case '2':

            while True:
            
                print('What do you want to be shown?')
                print('\n1. Active List')
                print('2. Inactive List')
                print('3. Both')
                print('-'*15)

                show_menu = input('Enter menu: ')
                system('cls')

                match show_menu:

                    case '1':
                        
                        search(todo_list, todo, 'activation', True, active_list)
                        show_list(active_list, todo)
                        break

                    case '2':

                        search(todo_list, todo, 'activation', False, inactive_list)
                        show_list(inactive_list, todo)
                        break

                    case '3':
                        
                        show_list(todo_list, todo)
                        break

                    case _:
                        print('Error!\n')

            
            active_list.clear()
            inactive_list.clear()
   
        case '3':

            # show list
            show_list(todo_list, todo)


            flag = True
            value = int(input('\n\nEnter the ID of a todo which you want to inactive: '))
            system('cls')
            
            if value <= number:
                
                search(todo_list, todo, 'id', value, search_list)

                for todo in search_list:

                    for item in todo:

                        if todo['activation'] == True:

                            todo['activation'] = False
                            message_list.append('Done!')
                            flag = False
                            break

                if flag:
                    message_list.append('This todo is already inactive')


                print(*message_list)

            else:
                print('Error! ID does not exist.')


            message_list.clear()
            search_list.clear()
                    
        case '4':
            
            while True:

                # show list
                show_list(todo_list, todo)


                edit = int(input('\nEnter the ID of the todo you want to edit: '))
                system('cls')

                if edit > number:
                    print('Error!')

                else:

                    for todo in todo_list:

                        if todo['id'] == edit:

                            while True:  

                                print('1. Title')
                                print('2. Description')
                                print('3. Date')

                                edit_option = input('\nWhat do you want to edit? ')
                                system('cls')

                                match edit_option:

                                    case '1':
                                        
                                        new_title = get_input(field='Title', is_empty=False)
                                        todo['title'] = new_title
                                        message_list.append('Done!')
                                        break
                

                                    case '2':
                                        
                                        new_description = get_input(field='Description')
                                        todo['description'] = new_description
                                        message_list.append('Done!')
                                        break


                                    case '3':

                                        print('Date Process:')

                                        new_year = int(get_input('Year', False))
                                        new_month = int(get_input('Month', False))
                                        new_day = int(get_input('Day', False))

                                        new_date = str(date(new_year, new_month, new_day))

                                        todo['date'] = new_date
                                        message_list.append('Done!')
                                        break

                                    case _:
                                        print('Error!')


                    print(*message_list)


                message_list.clear()
                        
                #region edit again
                again = True

                while True:

                    edit_again = input('Do you want to edit another one (yes/no)? ')
                    system('cls')

                    if edit_again == 'yes':
                        break

                    elif edit_again == 'no':
                        again = False
                        break

                if not again:
                    break
                #endregion
                    
        case '5':

            while True:

                print('How do you want to search the list?')
                print('\n1. ID')
                print('2. Title')
                print('3. Description')
                print('4. Date')
                print('-'*15)

                search_todo = input('Based on: ')
                system('cls')

                match search_todo:

                    case '1':
                        
                        value = int(get_input('ID', False))

                        if value > number:
                            print('Error!')

                        else:
                            search(todo_list, todo, 'id', value, search_list)
                            show_list(search_list, todo)


                    case '2':
                        
                        value = get_input('Title', False)
                        search(todo_list, todo, 'title', value, search_list)
                        show_list(search_list, todo)

                        
                    case '3':
                        #search for each word in descriptions
                        value = get_input('Description', False)
                        search(todo_list, todo, 'description', value, search_list, True)
                        show_list(search_list, todo)


                    case '4':

                        value = get_input('Date', False)
                        search(todo_list, todo, 'date', value, search_list)
                        show_list(search_list, todo)

                    case _:
                        print('Error!')


                search_list.clear()
                

                #region get input again
                again = True

                while True:

                    search_again = input('Do you want to search again (yes/no)? ')
                    system('cls')

                    if search_again == 'yes':
                        break

                    elif search_again == 'no':
                        again = False
                        break

                if not again:
                    break
                #endregion       

        case '6':
            break


