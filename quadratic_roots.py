#Write a script to evaluate the roots of quadratic equation.

print("Consider;\n# General quadratic equation : [ ax\u00b2 + bx + c ]")
a = float(input("Enter the value of a : "))
b = float(input("Enter the value of b : "))
c = float(input("Enter the value of c : "))

if a==0:
     print("Invalid value of a ")
else:
     delta = ((b**2)-(4*a*c)) 
     #Use () parentheses for mathematical operations; 
     #Use {} curly brackets to define a set or dictonary.

     x = (((-b)+(delta**0.5))/(2*a))
     y = (((-b)-(delta**0.5))/(2*a))

     if delta==0: #No need of parenthesis in python
         
         print("Roots of quadratic equation are 'Real' and 'Equal'. ")
         print(f"The value of identical root is : {round(x,2)}")

 #round(number, no. of decimals to keep) 
 #Also: if round(1234, -1) = 1230 for -2 ->1200 )

     elif delta>0: #Comparing of imaginary number isn't allowed.
                   #Therfore; didn't took the root over delta variable.
                   
         print("Roots of quadratic equation are 'Real'. ")
         print(f"Roots are : {round(x,2)} , {round(y,2)}")

     else:
          print("Roots of quadratic equation are 'Imaginary'. ")
          print(f"Roots are : ({round(x.real,2)}) + ({round(x.imag,2)})j ;",
                f"({round(y.real,2)}) + ({round(y.imag,2)})j")
          
# z = 3 + 5j ,
#By the following commands you can print on real or imaginary part of z.
#print(z.real)-> 3
#print(z.imag)-> 5
