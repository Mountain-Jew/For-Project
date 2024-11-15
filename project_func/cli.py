import prompt

def welcome():
    print('cli exit - выйти из программы\ncli help - справочная информация')
    command = prompt.string(prompt="Введите команду:")
    if command == 'cli help':
        print('cli exit - выйти из программы\ncli help - справочная информация')
        welcome()
    if command == 'cli exit':
        return 0
