from Mis_Calculator import addition, substraction, division, multiplication
condition=True
while condition:

    print("Enter the mathematical process you want to do:\n For addition enter >>>a\n For substraction enter >>>s\n For multiplication enter >>>m\n For division enter >>>d")
    process=input()
    if process=='a'or process=='d'or process=='s'or process=='m':
        first_number=(input('Enter the first number:'))
        second_number=(input('Enter the second number:'))

        if process=='a':
            result_of_process=addition(first_number,second_number)
            print(first_number,'+',second_number,'=',result_of_process)
        if process=='s':
            result_of_process=substraction(first_number,second_number)
            print(first_number,'-',second_number,'=',result_of_process)
        if process=='m':
            result_of_process=multiplication(first_number,second_number)
            print(first_number,'*',second_number,'=',result_of_process)
        if process=='d':
            result_of_process=division(first_number,second_number)
            if type(result_of_process)!=float:
                print()
    #    break
            print(first_number,'/',second_number,'=',result_of_process)
    #-------------ceil the result---------------------------------------------
 #   from math import ceil
  #  print(ceil(result_of_process)) #ceil the result upper number

    #-------------next math operation---------------------------------------
        print('Do you want to continue for the next '
      'mathematical operation?\n To continue press y, To exit press n ')
        next_process=input().upper()
        print(next_process)
        if next_process=='Y':
            condition=True
        elif next_process=='N':
            condition:False
            break
        else:
            print('Enter a valid expression; y or n')
    else:
        print('!!!This is not a valid mathematical operation!!!')