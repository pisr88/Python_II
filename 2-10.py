def DisplayOptions(options):
    for index, value in enumerate(options,start=1):
        print(index, value)
    return input('Select option above or press enter to exit: ')

options =  ['load data', 'export data', 'analyze & predict']
choice = 'x'

while choice:
    choice = DisplayOptions(options)
    if choice:
        try:
            choice_num = int(choice)
            print(options[choice_num-1]) if (choice_num >= 0 and (choice_num <= len(options))) else print(f'Dokonano niewłaściwego wyboru')
        except:
            print(f'Wartość powinna być liczbą')
    else:
        print(f'Program zakończył działanie')