#!/usr/bin/env python3
import sys
import prompt
sys.path.insert(1,'/home/artur/Документы/project_nukhimzon_b24-505/project_func')

def main():
    print('Первая попытка запустить проект!')
    from cli import welcome
    welcome()

if __name__ == '__main__':
    main()