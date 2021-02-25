### All Rights Reserved ###
'''
Developer: Alper Kaan
Date: 25.02.2021
Purpose of Software: LCM
'''
#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
'''
---PROJECT---
As a user, I want to use a program which can calculate the least common multiple (L.C.M.) of four numbers.
So that I can find the least common multiple (L.C.M.) of my inputs.

Acceptance Criteria:
Ask user to enter the four numbers. Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs.
Calculate the least common multiple (L.C.M.) of four numbers Use gcd function in module of math
'''
import math

dongu = True
while(dongu == True):
    numbers =[]
    try:
        
        for i in range(1,5):
            print()
            num = int(input(f"Enter number {i} : "))
            numbers.append(num)
        print()
        
        LCM = math.lcm(numbers[0],numbers[1],numbers[2],numbers[3])
        
        
        print(f'LCM of "{numbers[0]},{numbers[1]},{numbers[2]},{numbers[3]}" = {LCM}')
        dongu = False
    
    except ValueError:
        print("please enter a number")
        dongu = True
### All Rights Reserved ###

#Copyright (c) ${LCM.2021} ${Alper_Kaan}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.