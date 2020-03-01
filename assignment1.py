
number = int(input('How many numbers: '))
total = 0
for n in range(number):
    height = float(input('Enter your height in meters : '))
    total+=height
avg = total/number
print('Average of ', number, ' heights  is :', round(avg,2), 'meters')       
