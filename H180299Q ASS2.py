'''
Makanatsa L Paduze
H180299Q
Practical Security (Luhn's Algorithim)

ALGORITHIM STEPS:
    1. Enter your Card number
    2. Starting from the rightmost digit of the card number double the value of the second digit
    3. If doubling the number results in 2 digits then add the digit of the product to get a single digit ELSE leave the product alone .
    4. Now take the sum of all the digits.
    5. If Total MOD 10 = 0 then print" Credit card number valid " else print " Invalid credit card number "
'''

def creditcard():
    ccNum = input("Enter the credit card ")
    listOfNums=list(ccNum) #Changing input to list

    cal_num=[] #A variable that stores calculated varibales
    u_num =0 #Interger verify number>10

    check =0 #Sum up all digits

    if len(listOfNums) !=16:  #length check
        print("Your credit card number is invalid")
        quit()

    else:
        for i in range(len(listOfNums)):
            if((i%2)==0): #for loop for even numbers
                num=int((listOfNums[i]))*2 #Multiplication by 2

                if(num>=10):
                    u_num=num%10+1 #if doubling the number results in 2 digits then add the digit of the product to get a single digit

                    cal_num.append(u_num)
                else:
                    cal_num.append(num)
            else:
                
                cal_num.append(int(listOfNums[i]))

    
    for n in range(len(cal_num)):
        check=check+cal_num[n]
    if(check%10 == 0):
        print("valid credit card")
        return("Valid credit card")
    else:
        print("Invalid credit card")
        return("Invalid credit card")
    
creditcard()  

''' Q1a) 4137894711755904 : Valid
      b) 6499802450273568 : Invalid 
      c) 8504172191273888 : Valid 
      d) 0043668783485480 : Valid
'''
