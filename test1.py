#--------first program-------------
name = input("enter your name :")
print("hello  " + name)
#-----------third program------------
age = 14
age += 1 
print( "your age is " +str(age))
#------------logical operators------
temp = int(input("what is the temperature outside?"))
if temp >= 0 and temp <= 30:
    print("the temperature is good outside")
    print("go outside")
elif  temp < 0 or  temp > 30:
    print("weather is bad outside")
    print("stay inside")
   #---------------------------
