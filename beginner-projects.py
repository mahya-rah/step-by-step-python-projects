##Python Comments/Multiline Comments
##Python Data Types
##Python Variables/Variable Names
##-------------------------------------------------------------------
#print("hello")
##-------------------------------------------------------------------
##Python Arithmetic Operators
##-------------------------------------------------------------------
##Rectangle Perimeter
##محیط مستطیل

# Width = int(input("Enter the width of the rectangle: "))
# Length = int(input("Enter the length of the rectangle: "))
# print(2 * Width + 2 * Length)
##-------------------------------------------------------------------
##Rectangle Area
##مساحت مستطیل

# Width = int(input("Enter the width of the rectangle: "))
# Length = int(input("Enter the length of the rectangle: "))
# print(Width * Length)
##-------------------------------------------------------------------
'''Read the radius and height of the cylinders, volume and total area
Calculates the cylinder. The volume and total area of ​​the cylinder are calculated as follows:
𝜋 * 2 (radius) * height = volume of cylinder
(2(radius) * 𝜋) * 2 + height * radius * 𝜋 * 2 = volume of the total area'''

'''شعاع و ارتفاع استوانهای را خوانده، حجم و مساحت کل￼
استوانه را محاسبه میکند. حجم و مساحت کل استوانه بهصورت زیر محاسبه  میشود:
𝜋 * 2 (شعاع) * ارتفاع = حجم استوانه
( 2(شعاع) * 𝜋) * 2 + ارتفاع * شعاع * 𝜋 * 2 = حجم مساحت کل'''

# pi = 3.14
# ertefa = float(input("Ertefa: "))
# r = float(input("Shoa: "))
# hajm = pi * r ** 2 * ertefa
# masahat = 2 * pi * r * ertefa + 2 * pi * r ** 2
# print("masahat ", masahat, " hast va hajm ", hajm, " hast")
##---------------------------------------------------------------------
##A progarm which reads reads two numbers and swaps their amount
##برنامه ای که دو عدد را خوانده و محتوی آنها را تعویض￼می کند

# number1=int(input("Enter your number1: "))
# number2=int(input("Enter your number2: "))
# x=number1
# number1=number2
# number2=x
# print("number1 is",number1,"and number2 is",number2)
##-------------------------------------------------------------------
##A program that reads two numbers, replaces their contents without using auxiliary variables
##برنامه ای که دو عدد را خوانده، بدون استفاده از متغیر کمکی محتوی آنها را تعویض￼می کند

# number1=int(input("Enter your number1: "))
# number2=int(input("Enter your number2: ")) 
# number2=number2+number1
# number1=number2-number1
# number2=number2-number1
# print("number1 is",number1,"and number2 is",number2)
##...................................................................
# number1=int(input("Enter your number1: "))
# number2=int(input("Enter your number2: ")) 
# number2=number2*number1
# number1=int(number2/number1)
# number2=int(number2/number1)
# print("number1 is",number1,"and number2 is",number2)
##---------------------------------------------------------------------
##A program that calculates the roots of the equation Ax² + Bx + C.
##ریشه ها معادله Ax2 + Bx + C را به دست اورید

# A = int(input("Enter the A: "))    
# B = int(input("Enter the B: ")) 
# C = int(input("Enter the C: ")) 
# delta = B ** 2 - 4 * A * C
# if delta < 0:
#     print("There are no roots")
# else:
#     root1 = (B * -1 + delta ** (1/2)) / 2 * A
#     root2 = (B * -1 - delta ** (1/2)) / 2 * A
#     print("Roots are", root1, root2)
##---------------------------------------------------------------------
##if/elif/else
##Python Comparison Operators
##-------------------------------------------------------------------
##A program that takes two numbers from the input and determine which one is bigger
##دو عدد از ورودی گرفته و مشخص کنین کدام بزرگ تر است

# Value1 = int(input("Enter the first number: "))
# Value2 = int(input("Enter the second number: "))
# if Value1 > Value2:
#     print("The largest value is: ", Value1)
# else:
#     print("The largest value is: ", Value2)        
##-------------------------------------------------------------------
##A program that takes two input numbers and determine which one is bigger and if they are equal
##دو عدد ورودی گرفته و مشخص کنین کدام بزرگ تر است و ایا مساوی اند

# Value1 = int(input("Enter the first number: "))
# Value2 = int(input("Enter the second number: "))
# if Value1 > Value2:
#     print("The largest value is: ", Value1)
# elif Value2 > Value1:
#     print("The largest value is: ", Value2)  
# else:
#     print("Numbers are equal")    
##-------------------------------------------------------------------
##A program that reads a number and determine whether the number is even or odd
##عددی خوانده و مشخص کنید عدد زوج است یا فرد

# number = int(input("Enter your number: "))
# if number%2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")    
##-------------------------------------------------------------------
##A program that reads a number and determine whether the entered number is divisible by "K" or not
##عددی را خوانده و مشخص کنین عدد بر کا وارد شده بخش پذیر است یا خیر

# number = int(input("Enter your number: "))
# k = int(input("Enter the k: "))
# if number % k == 0:
#     print("The number is divisible")
# else:
#     print("The number is not divisible")    
##-------------------------------------------------------------------
##A program that specify whether the student has passed the lesson or not. 4 marks were taken from the examination and their average score was below 60, the student failed the course
##مشخص کنین دانش اموز درس را پاس شده یا نه. ۴ نمره از وروی گرفته و اکر میانگین ان ها زیر ۶۰ بود دانش اموز درس را افتاده

# m1 = int(input("Enter the first score: "))
# m2 = int(input("Enter the second score: "))
# m3 = int(input("Enter the third score: "))
# m4 = int(input("Enter the fourth score: "))
# if (m1 + m2 + m3 + m4) / 4 >= 60:
#     print("Pass")
# else:
#     print("Fail")    
##-------------------------------------------------------------------
##A program that reads the three numbers and shows the bigger number
##سه عدد خوانده و عدد بزرگ تر را نشان دهید    

# number1 = int(input("Enter the first number: "))    
# number2 = int(input("Enter the second number: "))    
# number3 = int(input("Enter the third number: "))  
# if number1 > number2:
#     if number1 > number3:
#         max = number1  
#     else:
#         max = number3    
# elif number2 > number3:
#     max = number2
# else:
#     max = number3

# print("The largest number is : ", max)                
##....................................................................
##Python Logical Operators
##....................................................................
# number1 = int(input("Enter the first number: "))    
# number2 = int(input("Enter the second number: "))    
# number3 = int(input("Enter the third number: "))  
# if number1 > number2 and number1 > number3:
#     print("The largest number is : ", number1)
# elif number2 > number1 and number2 > number3:
#     print("The largest number is : ", number2)
# elif number3 > number1 and number3 > number2:
#     print("The largest number is : ", number3)    
##-------------------------------------------------------------------
##A program that reads the three sides of a triangle and determines whether the triangle is right-angled or not
##سه ضلع یک مثلث را خوانده و مشخص کنین مثلث قایم الزاویه است یا نه 
  
# number1 = int(input("Enter the first number: "))    
# number2 = int(input("Enter the second number: "))    
# number3 = int(input("Enter the third number: ")) 
# max = max(number1, number2, number3)
# if 2 * max ** 2 == number1 ** 2 + number2 ** 2 + number3 ** 2:
#     print("Yes")
# else:
#     print("No")    
##-------------------------------------------------------------------
##A program that takes the three sides of a triangle, determines whether this triangle can be formed or not
##با گرفتن سه ضلع یک مثلث مشخص کنید این مثلث قابل تشکل است یا خیر

# number1 = int(input("Enter the first number: "))    
# number2 = int(input("Enter the second number: "))    
# number3 = int(input("Enter the third number: ")) 
# max = max(number1, number2, number3)
# if 2 * max < number1 + number2 + number3:
#     print("Yes")
# else:
#     print("No") 
##....................................................................
# number1 = int(input("Enter the first number: "))    
# number2 = int(input("Enter the second number: "))    
# number3 = int(input("Enter the third number: ")) 
# if (number1 + number2) > number3 and (number1 + number3) > number2 and (number3 + number2) > number1:
#     print("Yes")
# else:
#     print("No")
##-------------------------------------------------------------------
##A program that takes two numbers as input. If their product is less than or equal to 1000, it displays the product; otherwise, it displays their sum.
##دو عدد را از ورودی گرفته و اگر ضرب هان ها کمتر یا مساوی ۱۰۰۰ بود ان را نشان دهد در غیر این صورت جمع ان هارا نشانه دهد

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the first number: "))
# if num1 * num2 <= 1000:
#     print("The result is", num1 * num2)
# else:
#     print("The result is", num1 + num2)
##-------------------------------------------------------------------
##A program that takes a person's birth year, month, and day as input, and determines how many years and days have passed since their birth.
##سال ماه و روز تولد شخص را گرفته و مشخص کنید چه سالی و چند روز بعد به دنیا امده

# year = int(input("Which year were yoy born? ")) 
# month = int(input("what is your month of birth ? "))
# day = int(input("what is your day of birthday ? "))
# if 31>=day>=1 and 12>=month>=1 :
#     if month<7 :
#         daily = 31*month+day
#     else : 
#         daily = 30*month+day+6 
#     print("you were born in", year, "and", daily, "days ! ")       
# else :
#     print("incorrect numbers")
##-------------------------------------------------------------------
##A program that takes a number less than 1000 and returns the sum of its digits.
## یه عدد کوچک تر از ۱۰۰۰ بده مجموع ارقامشو بدم 

# adad=int(input('adad bede'))
# sum=0
# while adad!=0:    
#     b=adad%10    
#     sum=sum+b    
#     adad=adad//10
# print(sum) 
##-------------------------------------------------------------------
##while
##-------------------------------------------------------------------
##A program that prints 'Hello World' ten times using a loop.
## ده بار با لوپ"hello world"
# count = 0
# while count < 10:
#     print("hello world")
#     count += 1
##-------------------------------------------------------------------
##A program that prints a given name n times.
## پرینت کند نام وارد شده را n دفعه

# name = input("Enter your name: ")
# n = int(input("Enter the n:"))
# counter = 0
# while counter < n:
#     print(name)
#     counter += 1
##-------------------------------------------------------------------
##A program that calculates the sum of 5 entered numbers using a loop.
## مجموع ۵ عدد وارد شده را با کمک حلقه به دست اورید    

# sum = 0 
# counter = 0
# while counter < 5:
#     n = int(input("Enter the number: "))
#     sum += n
#     counter += 1
# print(sum)    
##-------------------------------------------------------------------
##A program that determines whether a student has passed the course or not. It takes n grades as input, and if the average is below 60, the student has failed.
## مشخص کنین دانش اموز درس را پاس شده یا نه. n نمره از وروی گرفته و اکر میانگین ان ها زیر ۶۰ بود دانش اموز درس را افتاده

# n = int(input("How many lessons does the student have: "))
# counter = 0
# sum = 0
# while counter < n:
#     score = int(input("Enter the score: "))
#     sum += score
#     counter += 1
# if sum / n >= 60:
#     print("pass") 
# else:
#     print("fail")       
##-------------------------------------------------------------------   
##A program that calculates the sum of the first 50 numbers starting from 1.
##مجموع ۵۰ عدد اول شروع از ۱ را حساب کنید

# sum = 0
# counter = 0
# while counter <= 50:
#     sum += counter
#     counter += 1
# print(sum)    
##------------------------------------------------------------------- 
##A program that calculates the sum of numbers between 1 and a natural number entered by the user.
##مجموع اعداد بین ۱ تا عدد طبیعی که ورودی وارد کرده است را حساب کنید

# n = int(input("Enter the number: "))
# sum = 0
# counter = 0
# while counter <= n:
#     sum += counter
#     counter += 1
# print(sum)  
##------------------------------------------------------------------- 
##A program that displays the even numbers between 9 and 100.
##اعداد زوج بین ۹ تا ۱۰۰ را نشان دهید

# counter = 10
# while counter < 100:
#     if counter % 2 == 0:
#         print(counter)
#     counter += 1
##-------------------------------------------------------------------
##A program that displays the even numbers between two natural numbers entered by the user.
## اعداد زوج بین دو عدد طبیعی که ورودی میدهد را نشان دهید

# first_number = int(input("Enter the first number: "))
# last_number = int(input("Enter the last number: "))
# counter = first_number + 1
# while counter > first_number and counter < last_number:
#     if counter % 2 == 0:
#         print(counter)
#     counter += 1
##..................................................................
# first_number = int(input("Enter the first number: "))
# last_number = int(input("Enter the last number: "))
# z = min(first_number, last_number)
# x = max(first_number, last_number)
# if z % 2 == 0:
#     z += 2
#     while z < x:
#         print(z)
#         z += 2
# else:
#     z += 1
#     while z < x:
#         print(z)
#         z +=2      
##-------------------------------------------------------------------
##A program that reads two numbers and displays their product without using the multiplication operator.
##دو عدد خوانده و حاصلضرب آنها را بدون استفاده از عملگر ضرب نمایش میدهد

# number = int(input("Enter the number: "))
# zarb = int(input("Enter the number: "))
# counter = 0
# sum = 0
# while counter < zarb:
#     sum += number
#     counter += 1
# print(sum) 
##-------------------------------------------------------------------
##A program that calculates the roots of the equation Ax² + Bx + C.
##ریشه ها معادله Ax2 + Bx + C را به دست اورید

# A = int(input("Enter the A: "))    
# B = int(input("Enter the B: ")) 
# C = int(input("Enter the C: ")) 
# delta = B ** 2 - 4 * A * C
# if delta < 0:
#     print("There are no roots")
# else:
#     root1 = (B * -1 + delta ** (1/2)) / 2 * A
#     root2 = (B * -1 - delta ** (1/2)) / 2 * A
#     print("Roots are", root1, root2)   
##-------------------------------------------------------------------
##A program that generates the Fibonacci series up to a natural number entered by the user.
##سری فیبوناچی تا عدد طبیعی وارد شده

# n = int(input("Enter the number: "))
# counter = 0
# sum1 = 0
# sum2 = 1
# print(sum1)
# print(sum2)
# while counter < n:
#     final = sum1 + sum2
#     print(final)
#     sum1 = sum2
#     sum2 = final
#     counter += 1
##------------------------------------------------------------------- 
##break and continue
##-------------------------------------------------------------------
##A program that keeps taking numbers as input until the user enters 0, then prints the product of all entered numbers except zero.
##برنامه ای که تا زمانی که کاربر عدد ۰ راوارد نکرده عدد وارد کند سپس حاصل ضرب اعداد ورود، بجر صفر را چاپ کند
# Final=1
# while True:
#     number=int(input("Enter the number: "))
#     if number==0:
#         break
#     else:
#         Final=Final*number    
# print(Final) 
##-------------------------------------------------------------------
##A program that calculates the greatest common divisor (GCD) of two numbers.
## ب.م.م دو عدد رو جاپ کن

# a = int(input("enter your first number :  "))
# b = int(input("enter your second number :"))
# if a>b :
#    n = b
# else :
#    n = a
# while b%n!=0 or a%n!=0 :
#    n=n-1
# print(n)
##-------------------------------------------------------------------
##
## دو عدد را خوانده، کوچکتریب مضرب مجترک آنها را نمایش می دهد

# x = int(input("Enter x:"))
# y = int(input("Enter y:"))
# if x > y:
#     z=x 
# else:
#     z=y
# while(True):
#     if (z%x==0) and (z%y==0):
#         lcm = z
#         break
#     z += 1 
# print("lcm is ", lcm)
##-------------------------------------------------------------------
##A program that reads numbers from input and outputs whether the numbers are perfect or not. A number is perfect if the sum of its divisors (excluding itself) equals the number itself. After checking each number, ask the user if they want to continue working.
'''اعدادی را از ورودی خوانده خروجی ای میدهد که آیا اعداد￼
موردنظر کامل هستند یا خير. عددی کامل است که مجموع مقسوم عليه های آن  (به جز خود) برابر با آن عدد باشد، پس از بررسی هر عدد از کاربر سؤال
کند که میخواهد به کار  ادامه دهد یا خير'''

# while True:
#     num = int(input("Enter a number:"))
#     sum = 0
#     i = 1
#     while i < num:
#         if (num % i == 0): 
#             sum += i
#         i += 1    
#     if (sum == num):
#         print("Perfect")
#     else:
#         print("Not perfect")
#     yes = input("Continue ?")
#     if (yes == 'N' or yes == 'n'):
#         break
##------------------------------------------------------------------- 
##A program that reads a number and determines whether it is symmetric or not. A number is symmetric if it equals its reverse. Example: 12321
##عددی را خوانده، مشخص میکند آیا عدد متقارن است یاخیر. عددی که برابر با مقلوبش باشد متقارن است ۱۲۳۲۱

# pow = 10
# sum = 0
# num = int(input("Enter a number:")) 
# temp = num
# while temp > 0:
#     sum = (pow * sum) + temp % 10
#     temp =temp // 10 
# if (sum == num):
#    print("Yes")
# else:
#     print("No")
##-------------------------------------------------------------------
##A program that reads a number and a digit, returns and prints how many times the digit appears in the number.
##یک عدد و یک رقم را خوانده و تکرار رقم در عدد را برمیگرداند و چاپ میکند

# adad = int(input("Enter adad:"))
# ragham = int (input ("Enter ragham:"))
# counter = 0
# while adad > 0:
#     if (adad % 10) == ragham:
#         counter = counter + 1
#     adad //= 10
# print (ragham, " Repeated ", counter, " times")    
##-------------------------------------------------------------------
##For 
##-------------------------------------------------------------------
##A program that receives a natural number and prints all smaller natural numbers in descending order.
#يك عدد طبيعي دريافت كرده، اعداد طبيعي كوچكتر از آن را به صورت نزولي چاپ نمايد

# x = int(input("enter a number")) 
# for i in range (1, x) :
#     x -= 1
#     print(x)
##....................................................................    
#for i in range (x,0,-1) :
#    print(i)
##------------------------------------------------------------------- 
##A program that finds all multipliers of the entered number that are less than 100.
##مضارب کا کوچک تر از ۱۰۰

# k = int(input("enter a number : "))
# for i in range(2,100):
#     if i * k <= 100 :
#         print(i*k)
##-------------------------------------------------------------------      
##A program that calculates university GPA by taking the number of courses, then grade and credit hours for each course.
##معدل دانشگاه با گرفتن تعداد درس ها و سپس نمره و تعداد واحد هر درس  

# x = int(input("tedade dars"))
# b=x
# sum = 0
# for i in range(x,0,-1):
#     y = float(input("nomre"))
#     z = int(input("vahed"))
#     sum +=y*z
#     x+=z
# print(sum/(x-b))
##-------------------------------------------------------------------
##A program that determines whether a number is prime or not.
##برنامه‌ای بنویسید که مشخص کند یک عدد اول هست یا نه

# number = int(input('please input your number: '))
# counter = 0
# for i in range(1, number+1):
#     if number%i == 0:
#         counter+=1
# if counter==2:
#     print('your number is prime')
# else:
#     print('your number is not prime')
##...................................................................
# number = int(input('please input your number: '))
# if number > 1 and number != 4:
#     for i in range(2 , number//2):
#         if number % i == 0:
#             print('your number is not prime')
#             break
#     else:
#         print('your number is prime')  
# else:
#     print('your number is not prime')
##---------------------------------------------------------------------
##A program that displays all three-digit prime numbers.
##برنامه‌ای بنویسید که اعداد اول سه رقمی را نمایش دهد

# for i in range(100,1000) :
#     c=0
#     for j in range(1,i+1) :
#         if i%j==0 :
#             c=c+1
#     if c==2 :
#         print(i)    
##----------------------------------------------------------------------
##A program that prints stars from the left side according to the number of entered rows.
##برنامه‌ای بنویسید که به تعداد ردیف‌های وارد شده، ستاره‌ها را از سمت چپ چاپ کند

# rows = int(input("Enter the number of rows: "))
# for i in range(rows+1):
#         print(i * "*")
##..................................................
# rows = int(input("Enter the number of rows: "))
# for i in range(rows, 0, -1):
#         print(i * "*")
##----------------------------------------------------------------------
##A program that prints stars from the right side according to the number of entered rows.
##برنامه‌ای بنویسید که به تعداد ردیف‌های وارد شده، ستاره‌ها را از سمت راست چاپ کند

# rows = int(input("Enter the number of rows: "))
# for i in range(rows+1):
#         print(i * " ", (rows - i) * "*")
##----------------------------------------------------------------------
##A program that prints a diamond shape made of stars.
##برنامه‌ای بنویسید که یک لوزی از ستاره‌ها چاپ کند

# h = int(input("please enter diamond's height:"))
# for i in range(h):
#     print(" "*(h-i), "*"*(i*2+1))
# for i in range(h-2, -1, -1):
#     print(" "*(h-i), "*"*(i*2+1))
##----------------------------------------------------------------------
##A program that prints the sum of n + nn + nnn + ...
##برنامه‌ای بنویسید که مجموع n + nn + nnn + ... را چاپ کند

# n=int(input("enter your n: "))
# tedad=int(input("tedad: "))
# sum=0
# for i in range (0,tedad):
#     sum+=10**(i)*n
#     num=sum
# for j in range (1,tedad):
#     num=num//10
#     sum+=num       
# print(sum)   
##-------------------------------------------------------------------
##A program that reads two positive integers m and n, and calculates the m raised to the power of n with "+".
## برنامه ای بنویسید که با جمع ام به توان ان را حساب کندm و n دو عدد صحيح و مثبت را خوانده، با￼

# m = int(input("Enter n:")) 
# n = int(input("Enter m:")) 
# sum = 0
# temp = m
# for i in range(1, n): 
#     sum = 0
#     for j in range(1, m + 1):
#         sum= sum + temp
#     temp =sum
# print(m, " ^ ",n, " = ",sum)
##-------------------------------------------------------------------
##A program that reads an integer from input and displays all prime numbers less than it.
##برنامه‌ای بنویسید که عددی صحیح را از ورودی خوانده، تمام اعداد اول قبل از آن را نمایش دهد

# n=int(input("enter your number: "))
# counter=0
# for i in range (1,n):
#     for j in range (1,i+1):
#         if i%j==0:
#             counter+=1
#     if counter==2:
#         print(i)
#     counter=0            
##-------------------------------------------------------------------
##A program that calculates the factorial of a number.
##برنامه ای که فاکتوریل یک عدد را محاسبه میکند

# num = int(input("Enter the number: "))
# factorial = 1
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1, num + 1):
#        factorial = factorial * i
#    print("The factorial of", num, "is", factorial)
#.............................................................
##with out multiplication operator 

# num = int(input("Enter the number: "))
# factorial = 1
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#     ans = num
#     i = num - 1
#     while (i > 0):
#         sum = 0
        
#         for j in range(i):
#             sum += ans
 
#         ans = sum
#         i -= 1
# print("The factorial of", num, "is", ans)  
##-------------------------------------------------------------------
##string
##-------------------------------------------------------------------
# string = input("Enter tour string: ")
##-------------------------------------------------------------------
##A program that receives a string and displays the word with the greatest length.
##برنامه‌ای که رشته‌ای دریافت کرده و لغتی که بیشترین طول را دارد نمایش می‌دهد

# s1 = input("Enter a string:")
# s2 = input("Enter a string:")
# if len(s1) > len(s2):
#     print(s1)
# elif len(s1) < len(s2):
#     print(s2)
# else:
#     print("Equal")      
##------------------------------------------------------------------------
##A program that prints the number of vowels in a word entered by the user.
##برنامه‌ای بنویسید که تعداد حروف صدادار کلمه‌ای که کاربر وارد کرده را چاپ کند

# a = input()
# t=0
# for i in range(len(a)) :
#     if a[i]=='a' or a[i]=='i' or a[i]=='u' or a[i]=='e' or a[i]=='o' :
#         t=t+1
# print(t)        
##------------------------------------------------------------------------
##A program that reads a string and displays its characters separated by a space.
##برنامه‌ای بنویسید که یک رشته را خوانده و کاراکترهای رشته را با یک فاصله نمایش دهد

# s = input("Enter a string:") 
# for i in s:
#     print(i, end = ' ')
##-------------------------------------------------------------------    
##A program that takes a string and displays the characters at even indices.
##برنامه‌ای بنویسید که رشته‌ای را گرفته و کاراکترهای با اندیس زوج آن را نمایش می‌دهد

# str = input("Enter a string:")
# result = ""
# for i in range(len(str)):
#     if i % 2 == 0:
#         result = result + str[i]
# print(result)        
##-------------------------------------------------------------------   
##A program that takes a string and displays the frequency of each word.      
## برنامه ای که یک رشته را گرفته تعداد تکرار هر کلمه را نمایش میدهد￼

# string = input("Enter a string:")
# words = input("Enter the word; ")
# counter = 0
# for word in string:
#     if words in word:
#         counter += 1
# print(counter)
##-------------------------------------------------------------------  
##A program that receives a string and reverses it.
## برنامه ای که رشتهای را دریافت کرده، مقلوب میکند

# string = input()
# sum = ""
# for i in range(len(string)):
#     sum += string[len(string) - 1 - i]
# print(sum)
##................................................... 
# mystring = input('enter your string : ')
#print(mystring[ : :-1])
##...................................................
## .reverse()
##...................................................
# mystring = input('enter your string : ')
# a = list(mystring)
# a.reverse()
# print(a)      
##------------------------------------------------------------------- 
##A program that receives a string and identifies and removes the repeated characters. It just use them once
##رشته ای را دریافت میکند و حروف تکراری را تمایز میکند

# string = input("Enter a string:")
# counts = ""
# for word in string:
#     if word in counts:
#         continue
#     else:
#         counts += word
# print(counts)  
##-------------------------------------------------------------------  
##A program that takes a string and displays the frequency of each character.
##رشته ای را گرفته تعداد تکرار هر حرف را نمایش میدهد 

# string = input("Enter a string:")
# counts = ""
# counter = 0
# for word in string:
#     if word in counts:
#         continue
#     else:
#         counts += word
#         for i in string:
#             if word == i:
#                 counter += 1
#         print(word, "repeated", counter, "times.")   
#         counter = 0             
##------------------------------------------------------------------------
##A program that takes a string and replaces every occurrence of the letter ‘a’ with ‘x’.
##بزاره‘a’ داشت بجاش ‘x’  برنامه ای بنویسید که یک رشته را بگیرد و هرجا حرف 

# mystring = input('enter your string : ')
# counter = 0
# for i in mystring :
#     if i=='x':
#         new_letter = mystring[counter+1:]
#         mystring = mystring[:counter]+'a'+new_letter
#     counter = counter+1  
# print(mystring) 
##.................................................................
## .join()
##.................................................................
# mystring = input('enter your string : ')
# counter = 0
# listmystring = list(mystring)
# for i in listmystring :
#     if i == 'x' :
#         listmystring[counter]='a'
#     counter = counter+1 
# finalString = ''.join(listmystring)
# print(finalString)
##------------------------------------------------------------------- 
##string method (upper/lower/replace/count)
##--------------------------------------------------------------------------
##A program that receives a string and displays the number of vowels in it.
##رشته ای را ریافت کرده و تعداد حروف صدا دار آن را نشان دهد

# str = input()
# a = str.count('a')
# o = str.count('o')
# e = str.count('e')
# i = str.count('i')
# u = str.count('u')
# print("a: ", a, "\no: ", o, "\ne: ",e, "\ni: ", i, "\nu: ",u)
##--------------------------------------------------------------------------
##A program that reads a string and converts all lowercase letters to uppercase and all uppercase letters to lowercase.
##برنامه‌ای بنویسید که رشته‌ای را خوانده و تمام حروف کوچک را به بزرگ و حروف بزرگ را به کوچک تبدیل کند

# s = ""
# str = input("Enter a string:")
# for i in range(0, len(str)):
#     if  str[i].lower() == str[i]:
#         s += str[i].upper()
#     else:
#         s += str[i].lower()
# print("Result is ", s)       
##-----------------------------------------------------------------------------
##A program that receives a string and a set of characters, and removes those characters from the string.
##برنامه‌ای بنویسید که رشته و مجموعه‌ای از کاراکترها را دریافت کرده و آن کاراکترها را از رشته حذف کند

# string = input("Enter a string:")
# words = input("Enter your words: ")
# for i in string:
#     if i in words:
#         string = string.replace(i, '')
# print(string)        
##---------------------------------------------------------------------------------
##A program that receives a string and removes any digits if present.
##برنامه‌ای بنویسید که رشته‌ای را دریافت کرده و اگر عددی در آن باشد، آن را حذف کند

# txt = input()
# for i in txt:
#     for j in range(10):
#         if i == str(j):
#             txt = txt.replace(i, '')
# print(txt)   
##--------------------------------------------------------------------------------
##List
##---------------------------------------------------------------------------------
##A program that has a list of foods, takes a food as input, and if it exists, says it is available.
##برنامه‌ای بنویسید که لیستی از غذاها داشته باشد و غذایی را از ورودی بگیرد و اگر موجود بود بگوید موجود است

# food = ["ghorme", "gheyme", "pizza", "pasta"]
# sefaresh = input().lower()
# if sefaresh in food:
#     print(sefaresh, " mojood ast")
# else:
#     print(sefaresh, "mojood nist.")  
#----------------------------------------------------------------
##A program that takes n from the user and puts its digits into a list.
##برنامه ای بنویسید که ان را از کاربر بگیرد و ارقام آن را در یک لیست بریزد

# n=list(input('\n enter your number : '))
# print(n)
#...................................................
# n=input(' \n enter your number : ')
# c = len(n)*[0]
# h= len(n)
# i = 1
# while n!=0:    
#     b=int(n)%10 
#     a=i   
#     while i!=0 :
#         c[h-i] = b
#         i=0
#     i=1+a    
#     n=int(n)//10
# print(c) 
##--------------------------------------------------------------------------------
##.split()
##.strip()
##---------------------------------------------------------------------------------
##A program that takes a list of names and returns the names whose first letter is "M"
## برنامه‌ای بنویسید که لیستی از اسم‌ها را گرفته، اگر حرف اول لیست با «م» شروع شده بود، آن اسم‌ها را برگرداند

# mylist = input().split()
# for i in mylist:
#     if i[0] == 'm' or i[0] == "M":
#         print(i)       
##---------------------------------------------------------------------------------
## .append()
##---------------------------------------------------------------------------------
##A program that receives a list and filters out the positive numbers
##برنامه‌ای که یک لیست را دریافت کرده و اعداد مثبت آن را فیلتر می‌کند
 
# mylist = input().split()
# mylist2 = []
# for i in mylist:
#     if int(i) > 0:
#         mylist2.append(i)
# print(mylist2)
##---------------------------------------------------------------------
##A program that reads a natural number from input, stores all prime numbers less than it in a list, and prints the list.
##برنامه‌ای بنویسید که عددی طبیعی را از ورودی خوانده، تمام اعداد اول قبل از آن را در لیستی بریزد و چاپ کند

# n=int(input("enter your number: "))
# counter=0 
# mylist=[]
# for i in range (1,n):
#     for j in range (1,i+1):
#         if i%j==0:
#             counter+=1
#     if counter==2:
#         mylist.append(i)
#     else:
#         counter=0 
# print(mylist)      
##---------------------------------------------------------------------
##A program that takes a list, removes duplicate elements, and displays the unique elements.
## یک لیست را گرفته عناصر تکراری آن را یکتا کرده و نمایش میدهد
# mylist=input().split()
# result = [] 
# for i in mylist: 
#     if i not in result: 
#         result.append(i) 
# print (result) 
##---------------------------------------------------------------------
##A program that takes two lists and determines how many elements they have in common.
##برنامه‌ای بنویسید که دو لیست را گرفته و تعیین کند چند عضو مشترک دارند

# mylist1=input("Enter your first list: ").split()
# mylist2=input("Enter your second list: ").split()
# mylist3=[]
# for i in mylist1:
#     for j in mylist2:
#         if i==j:
#             mylist3.append(j)
# final = []
# for num in mylist3:
#     if num not in final:
#         final.append(num)
# print(len(final))            
##---------------------------------------------------------------------
##A program that reads a natural number from input, stores all prime numbers less than it in a list, and prints the list.
##برنامه‌ای بنویسید که عددی طبیعی را از ورودی خوانده، تمام اعداد اول قبل از آن را در لیستی بریزد و چاپ کند

# n=int(input("enter your number: "))
# counter=0 
# mylist=[]
# for i in range (1,n):
#     for j in range (1,i+1):
#         if i%j==0:
#             counter+=1
#     if counter==2:
#         mylist.append(i)
#     else:
#         counter=0 
# print(mylist)      
##---------------------------------------------------------------------
## .pop()/.remove()
##---------------------------------------------------------------------
##A program that receives a list and displays its second smallest value.
##برنامه‌ای بنویسید که لیستی را دریافت کرده و دومین کوچک‌ترین مقدار آن را نمایش دهد

# mylist=input("Enter your list: ").split()
# mylist.remove(str(max(mylist)))
# print(max(mylist))
##------------------------------------------------------------------------
##A program that takes a list and removes the last element if its index is even.
## برنامه‌ای بنویسید که لیستی را گرفته و اگر ایندکس آخرش زوج بود آن عنصر را حذف کند

# n = int(input())
# num = n*[0]
# for i in range(n) :
#     num[i] = int(input())
# lastindex=num[-1]
# if num[-1]%2==0 :
#     num.remove(lastindex)    
# print(num)    
##---------------------------------------------------------------------------------
## .reverse()
##---------------------------------------------------------------------------------
##A program that takes the elements of an n-sized list and then reverses the list.
##برنامه ای بنویسید که اعضای یک لیست ان تایی را بگیرد و سپس لیست را برعکس کند 

# mylist = list(input())
# mylist.reverse()
# print(mylist)
##........................................................................
# n=int(input())
# b=n*[0]
# for i in range (n):
#       b[i]=int(input())
# for j in range (n//2):
#       c=b[j]
#       b[j]=b[n-j-1]
#       b[n-j-1]=c 
#       print(b) 
##---------------------------------------------------------------------------------
##Random Library 
##https://docs.python.org/3/library/random.html
##-----------------------------------------------------------------------------------
##random.choice()
##-----------------------------------------------------------------------------------
##A program for the coin toss game (heads or tails).
##برنامه‌ای برای بازی شیر یا خط بنویسید

# import random

# coin = random.choice(["heads", "tails"])
# print(coin)
##-----------------------------------------------------------------------------------
##A program for the dice game.
##برنامه‌ای برای بازی تاس بنویسید

# import random

# dice = random.choice([1, 2, 3, 4, 5, 6])
# print(dice)
##-----------------------------------------------------------------------------------
##A program that reads a string, randomly selects one character from it, and displays it.
##برنامه‌ای بنویسید که رشته‌ای را خوانده، یک کاراکتر را به طور تصادفی از رشته انتخاب کرده و نمایش دهد

# import random

# s = input("Enter a string:")
# print("Random char is ", random.choice(s))
##-----------------------------------------------------------------------------------
##random.randint()
##-----------------------------------------------------------------------------------
##A program that generates 25 random integers between 0 and 20 and then prints the average of the scores.
##برنامه‌ای بنویسید که ۲۵ نمره تصادفی صحیح بین ۰ و ۲۰ تولید کند و سپس میانگین نمره‌ها را چاپ کند

# import random

# i = 0
# k = 0
# while i<25 :
#     n = random.randint(0,20)
#     k = n+k
#     i = i+1
# print(k/25)    
##.......................................................................
# import  random

# s=0
# for i in range (20):
#     a=random.randint(0,20)
#     s=s+a
# print('miyangin=',s/20)
##-----------------------------------------------------------------------------------
#Function
##-----------------------------------------------------------------------------------
##A program that displays a random array containing numbers between 2 and 100
##برنامه‌ای بنویسید که یک آرایه تصادفی شامل اعداد بین ۲ تا ۱۰۰ را نمایش دهد

# import random 
# n = int(input())
# randomlist=n*[0]
# while n>0 :
#     num=random.randint(2,100)
#     randomlist[n-1]=num
#     n = n-1
#print(randomlist)
##------------------------------------------------------------------------------
##A program that rolls a die and sums the numbers, but if a 6 appears, it rolls again.
##برنامه‌ای بنویسید که یک تاس می‌اندازد و مجموع اعداد را حساب می‌کند، اما اگر عدد ۶ بیاید دوباره تاس می‌اندازد

# import random 

# def Nomre():
#     tas_numbers = [1, 2, 3, 4, 5, 6]
#     tas = random.choice(tas_numbers)
#     nomre = tas
#     while tas == 6:
#         tas = random.choice(tas_numbers)
#         nomre += tas
#     return nomre

# print(Nomre())           
##------------------------------------------------------------------------------
## A program that simulates the Bingo game.
##برنامه‌ای بنویسید که بازی بینگو را شبیه‌سازی کند
''' Bingo!" means "Correct guess! You win!
it’s a simple congratulatory word that signals the player has successfully guessed the secret random number within the allowed attempts.'''

# import random

# rand_num = random.randint(0, 10)
# guess_left = 3
# name = input("Enter your name: ")

# def check_answer(answer):
#     if answer > rand_num:
#         return (False, "Choose lower number.")
#     elif answer < rand_num:
#         return (False, "Choose higher number.")
#     elif answer == rand_num:
#         return (True, "Bingo!")
    
# while True:
#     if guess_left == 0:
#         print(f"You ran out of guesses! /n answer was: {rand_num}")
#         break
#     answer_input = int(input(f"{name}, Please enter your guess number: "))    
#     answer_result = check_answer(answer_input)
#     if answer_result[0] == False:
#         print(answer_result[1])
#     else:
#         print(answer_result[1])
#         break
#     guess_left -= 1
    
# print("End of game")        
##-----------------------------------------------------------------------------------
##A program that generates a random password.
##برنامه‌ای که رمز عبور تصادفی تولید می‌کند

# import random 

# def Random_Password_Generator():
#     S_letters = [
#         'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
#         'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
#     ]
#     C_letters = [
#         'A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
#         'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
#     ]
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '_']

#     password_list = []
#     letters_num = random.randint(1, 6)
#     numbers_num = random.randint(1, 8-letters_num-1)
#     symbols_num = 8-numbers_num-letters_num

#     for char in range (1, (letters_num + 1) // 2 + 1):
#         password_list.append(random.choice(S_letters))
#         password_list.append(random.choice(C_letters))
    
#     for char in range(1, numbers_num + 1):
#         password_list.append(random.choice(numbers))

#     for char in range(1, symbols_num + 1):
#         password_list.append(random.choice(symbols))

#     random.shuffle(password_list)
#     password_string = ""
#     for i in password_list:
#         password_string += i
#     return(password_string)    

# print(Random_Password_Generator())
##------------------------------------------------------------------------------
##A program that generates random art with user-defined width and height.
##برنامه‌ای که یک هنر تصادفی با عرض و ارتفاع دلخواه تولید می‌کند

# import random

# def random_art_generator():
#     width = int(input("Enter the width: "))
#     height = int(input("Enter the height: "))
#     for i in range(height):
#         row = ''
#         for j in range(width):
#             if random.randint(0, 1) == 0:
#                 row += '*'
#             else:
#                 row += ' '
#         print(row) 
        
# random_art_generator()               
##------------------------------------------------------------------------------
##A program that generates random names for characters, pets, or any other purpose.
##برنامه‌ای بسازید که نام‌های تصادفی برای شخصیت‌ها، حیوانات خانگی یا هر منظور دیگری تولید کند

# import random

# def generate_name():
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
#     name = ''
#     for _ in range(random.randint(3, 5)):
#         name += random.choice(consonants)
#         name += random.choice(vowels)
#     return name

# print(generate_name())
##------------------------------------------------------------------------------
##Statistics Library 
##https://docs.python.org/3/library/statistics.html
##------------------------------------------------------------------------------
##statistics.mean()
##------------------------------------------------------------------------------
##A program that gives the mean of given scores
##برنامه‌ای که میانگین نمرات داده شده را محاسبه کند

# import statistics

# scores = input("Give the scores: ").split()
# print(statistics.mean(scores))
##------------------------------------------------------------------------------
##Cowsay Library
##------------------------------------------------------------------------------
##https://pypi.org/project/cowsay/
##------------------------------------------------------------------------------
##pip install cowsay
##------------------------------------------------------------------------------
##Lets hear Hello from a cow !
##A program that uses the cowsay library to display a "Hello" message spoken by a cow.
##cowsay،برنامه‌ای که با استفاده از کتابخانه  پیغام "سلام" را از زبان یک گاو نمایش می‌دهد

# import cowsay

# name = input("Enter your name: ")
# cowsay.cow("Hello, " + name)
##------------------------------------------------------------------------------
##We cal them "Ascii Art"
##------------------------------------------------------------------------------
##Lets hear Hello from a trex !
##A program that uses the cowsay library to display a "Hello" message from a T-Rex.
##برنامه‌ای که با استفاده از کتابخانه cowsay، پیغام "سلام" را از زبان یک دایناسور تی‌رکس نمایش می‌دهد

# import cowsay

# name = input("Enter your name: ")
# cowsay.trex("Hello, " + name)
##------------------------------------------------------------------------------
##Dictionary
##------------------------------------------------------------------------------
'''
A program that receives student information including name, last name, student number, university, major, and number of courses taken,
and allows the user to enter the name of any of these fields to see the corresponding value
'''
'''
برنامه‌ای که اطلاعات دانشجو شامل نام، نام خانوادگی، شماره دانشجویی، دانشگاه، رشته و تعداد واحدهای گذرانده شده را دریافت کند 
و به کاربر اجازه دهد که با وارد کردن نام هر کدام از این اطلاعات، مقدار مربوطه را مشاهده کند
'''

# name = input("Enter your name: ")
# lastname = input("Enter your last name: ")
# student_number = input("Enter your student number: ")
# university = input("Enter your university's name: ")
# major = input("What is your major? ")
# course = input("Enter number of your courses: ")
# student = {"name" : name,
#            "last name" : lastname,
#            "student number" : student_number,
#            "university" : university,
#            "major" : major,
#            "course" : course,
#            }
# question = input("What information do you want from the student?")
# for i in list(student.keys()):
#     if question == i:
#         print("The student's", i, "is", student[i])
##-----------------------------------------------------------------------------------
##A program that creates a dictionary from two lists.
##برنامه‌ای که از دو لیست یک دیکشنری می‌سازد

# list1 = input("Enter the first list: ").split()
# list2 = input("Enter the second list: ").split()
# myDictionary = {}
# if len(list2) >= len(list1):
#     for i in range(len(list1)):
#         myDictionary.update({list1[i]:list2[i]})
#     print(myDictionary)
# else:
#     print("needed more value.")    
##-----------------------------------------------------------------------------------
##.items()
##eval()
##-----------------------------------------------------------------------------------
##A program that receives two dictionaries, sums the values of matching keys, and merges the two dictionaries.
##برنامه‌ای که دو دیکشنری را دریافت کرده، مقادیری که کلیدهای آنها مشترک است را با هم جمع می‌کند و دو دیکشنری را ترکیب می‌کند

# dict1 = eval(input("Enter first dictionary (e.g., {'a': 2, 'b': 3}): "))
# dict2 = eval(input("Enter second dictionary (e.g., {'b': 4, 'c': 5}): "))
# merged_dict = dict1

# # Merge with second dictionary
# for key in dict2:
#     if key in merged_dict:
#         merged_dict[key] += dict2[key]
#     else:
#         merged_dict[key] = dict2[key]

# print("Merged dictionary:", merged_dict)

##-----------------------------------------------------------------------------------
##A program that has a menu of foods and their prices, takes a food order from the user, displays the price if it exists, otherwise asks the user if they want to add the food and then adds it to the menu.
##برنامه‌ای که منویی از غذاها و قیمت‌هایشان دارد، غذایی را از کاربر می‌گیرد، اگر موجود بود قیمت را نمایش می‌دهد، در غیر این صورت از کاربر می‌پرسد آیا می‌خواهد آن غذا را اضافه کند و سپس به منو اضافه می‌کند

# myDictionary= {"pasta": "30","gheimeh" : "20","fesenjoon": "0", "pizza": "5" , "lasagna": "10"}
# x=input("chi mikhori?")
# if x in myDictionary.keys():
#   print(myDictionary.get(x))
# else:
#   print("nadarim dadash")
#   y=input("mikhay ezafe konam azizam?")
#   if y=="yes":
#     d=input("chand ta bzarm")
#     myDictionary.update({x:d})
#     print(myDictionary)
#   else :
#       print("be salamat")
##----------------------------------------------------------------------------------- 
##A program that takes a dictionary and a list of keys, and creates a new dictionary containing only the specified keys and their corresponding values.
##برنامه‌ای بنویسید که یک دیکشنری و لیستی از کلیدها را دریافت کند و یک دیکشنری جدید بسازد که فقط شامل کلیدهای مشخص شده و مقادیر مربوطه باشد

# library = {"interstellar" : 2014, "friends" : 1994, "inception" : 2010}
# mylist = input("Please enter your list: ").split()
# mylibrary = {}
# for i in mylist:
#     if i in library.keys():
#         mylibrary.update({i:library[i]})
# print(mylibrary)        
##-----------------------------------------------------------------------------------
##A program that takes a dictionary and sorts it by its values, for example {'Math':81, 'Physics':83, 'Chemistry':87}.
##برنامه‌ای بنویسید که یک دیکشنری را گرفته و آن را بر اساس مقادیرش مرتب کند مانند {'Math':81, 'Physics':83, 'Chemistry':87}

# data = eval(input("Enter a dictionary (مثلاً {'Math':81, 'Physics':83, 'Chemistry':87}): "))
# sorted_dict = dict(sorted(data.items(), key=lambda item: item[1]))
# print("Sorted dictionary by values:", sorted_dict)
##-----------------------------------------------------------------------------------
##A program that reads a string and displays its uppercase and lowercase letters as two separate categories in a dictionary.
##برنامه‌ای بنویسید که رشته‌ای را خوانده و حروف بزرگ و کوچک آن را به صورت دو دسته در یک دیکشنری نمایش دهد

# string = input("Enter your string: ")

# uppercase_letters = []
# lowercase_letters = []

# for char in string:
#     if char.isupper():
#         uppercase_letters.append(char)
#     elif char.islower():
#         lowercase_letters.append(char)

# result = {
#     "uppercase": uppercase_letters,
#     "lowercase": lowercase_letters
# }

# print(result)
##----------------------------------------------------------------------------------- 
##A program to remove a specific key from a dictionary
##برنامه‌ای بنویسید که یک کلید مشخص را از دیکشنری حذف کند

# data = eval(input("Enter a dictionary (مثلاً {'a':1, 'b':2, 'c':3}): "))
# key_to_remove = input("Enter the key to remove: ")

# if key_to_remove in data:
#     del data[key_to_remove]
#     print(f"Key '{key_to_remove}' removed.")
# else:
#     print(f"Key '{key_to_remove}' not found.")

# print("Updated dictionary:", data)
##----------------------------------------------------------------------------------- 