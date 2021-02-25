#===================The Least Common Multiple Module=======================
# Developer: Cemil Tepecik
# Date:23.02.2021
#!!!!!!!!!!BE CAREFUL. This program rquires to operate 'The_Least_Common_Multiple.py'
#As a user, I want to use a program which can calculate the least common multiple (L.C.M.) of four numbers.
# So that I can find the least common multiple (L.C.M.) of my inputs.
# Acceptance Criteria:
#Ask user to enter the four numbers. Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs.
# Calculate the least common multiple (L.C.M.) of four numbers Use gcd function in module of math
#=======================MAIN PROGRAM=========================================
continues=True
while continues:

    number_1=input('Enter the first number to count LCM:')
    number_2=input('Enter the second number to count LCM:')
    number_3=input('Enter the third number to count LCM:')
    number_4=input('Enter the fourth number to count LCM:')
    from The_Least_Common_Multiple import lcm_function,error_detection_function
    number_list=[number_1,number_2,number_3,number_4]
    some=error_detection_function(number_list) # error detection. if some==none there is error, otherwise everythin is okay
    print(some)

    if some==11: #No errror
        final_result = lcm_function(number_list) #LCM calculation
        print('LCM (OKEK) of', number_1, ',', number_2, ',', number_3, 'and', number_4, 'is :', final_result)

#---------------main program , do you want to continiue to next calculation?---------------
    answer = input('Do you want to continue? If yes, press Y').lower()
    if answer=='y':
        continues = True
    else:
        print('Thank you for using The Least Common Multiple Module.')
        break
#====================================END OF THE PROGRAM===========================================




