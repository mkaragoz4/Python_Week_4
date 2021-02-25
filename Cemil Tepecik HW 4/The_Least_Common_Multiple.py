#=========The Least Common Multiple Module=============
# Developer: Cemil Tepecik
# Date:23.02.2021
#!!!!!!!!!!BE CAREFUL. This program is a sub module of  '4. The Least Common Multiple Module.py'

#============This function counts lcm of four numbers coming wiht number_list==================
def lcm_function(number_list):
    number_list=[int(number_list[0]),int(number_list[1]),int(number_list[2]),int(number_list[3])]
    from math import gcd
    from functools import reduce
    gcd_of_12=gcd(number_list[0],number_list[1])
    lcm_of_12 = number_list[0]*number_list[1]/gcd_of_12
#    print(lcm_of_12)
    gcd_of_34=gcd(number_list[2],number_list[3])
    lcm_of_34 =number_list[2]*number_list[3]/gcd_of_34
  #  print(lcm_of_34)

    gcd_of_fournumber= gcd(int(lcm_of_34),int(lcm_of_12))
#    print(gcd_of_fournumber)
    lcm_of_fournumber= lcm_of_34*lcm_of_12/gcd_of_fournumber
    return int(lcm_of_fournumber)
#-----------------end of the function----------------------------

#============This function detectsw the entry errors of  '4. The Least Common Multiple Module.py'==================
def error_detection_function(number_list):
    import sys
# """ if even one number is zero, ':LCM is directly zero"""
#    """int degilse float ise, 'ValueError: numbers must be integer"""
#   """non numerical inputs 'Type error': entry can not ve non numerical"""
    for x in number_list:
        if x == '0':
            return print('LCM (OKEK) of', number_list[0], ',', number_list[1], ',', number_list[2], 'and', number_list[3], 'is :', 'Zero')

    for x in number_list:
        try:
            number_list = [int(number_list[0]), int(number_list[1]), int(number_list[2]), int(number_list[3])]
#            from math import gcd
 #           gcd(x,2)
        except:
            return print('!There is an error in your operation:',sys.exc_info()[0] )
        else:
            return 11
#-----------------end of the function----------------------------

