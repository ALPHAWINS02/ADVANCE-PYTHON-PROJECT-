import math
import random
import datetime
import turtle

Name = input("Enter your Name : ")
Now=datetime.datetime.now()
print (Now)
print ()
print (Name,", नमस्कार")
print ('''
Welcome to Student Utility Program!!
Please Enter Code as per your Desire

DESIRE CODE
1. INTERNAL MARKS CHECKING
2. ATTENDANCE CHECKER
3. MATH HELP CALCULATOR
4. CS HELPER
5. LET'S PLAY A GAME
6. WANT SOME INTERACTIVE
7. END

Well, On a Lighter Note, We Promise that we will not instruct "HELLO FRANDS चाय पी लो" anywhere in Code:-)))))
And also we will not annoy with "Selfie Maine Le li Aaj"

NOTE : Be Careful, else SCARY RED ERROR MESSAGE IS WAITING "\U0001f600" ''')

print()

X='Y'


while X=='Y' or X!='N':
    print()
    DCode = int(input("Enter your DESIRE CODE : "))
    print()
    if DCode>7 or DCode<1:
        print (Name, ", It's a ERROR, Try Again!!")
        X='Y'
    if DCode==7:
        print("TERMINATING!!")
        X='N'
    if DCode==1:
        print (Name, ''', For Which Subject you want to Check Internal Exam?
        SUBJECT CODE
        042. Physics
        043. Chemistry
        083. Computer Science (New)
        048. Physical Education
        301. English Core
        041. Mathematics
        ''')
        SCode = input("Enter your Subect Code:")
        print()
        if SCode in ['042', '043','083','048']:
            PT1=float(input("Enter your Marks in Periodic Test 1: "))
            HY=float(input("Enter your Marks in Half Yearly: "))
            PT2=int(input("Enter your Marks in Periodic Test 2: "))
            Marks=((2*PT1)/7)+((3*HY)/7)+((2*PT2)/7)
            print (Name, ", you will get", Marks, "Marks out of 50 in Internal Exam")
            print ("ALL THE BEST FOR SESSION ENDING EXAM")            
        
        elif SCode=='301':
            PT1=float(input("Enter your Marks in Periodic Test 1: "))
            HY=float(input("Enter your Marks in Half Yearly: "))
            PT2=int(input("Enter your Marks in Periodic Test 2: "))
            Marks=(PT1/4)+((3*HY)/8)+(PT2/4)
            print (Name, ", you will get", Marks, "Marks out of 50 in Internal Exam")
            print ("ALL THE BEST FOR SESSION ENDING EXAM")
        
        elif SCode=='041':
            PT1=float(input("Enter your Marks in Periodic Test 1: "))
            HY=float(input("Enter your Marks in Half Yearly: "))
            PT2=int(input("Enter your Marks in Periodic Test 2: "))
            Marks=(PT1/5)+((3*HY)/10)+(PT2/5)
            print (Name, ", you will get", Marks, "Marks out of 50 in Internal Exam")
            print ("ALL THE BEST FOR SESSION ENDING EXAM")
        
        else:
            print ("Error! RESTARTING")
            X='Y'
            continue
            

    if DCode==2:
        Tot=int(input("Enter Total Attendance : "))
        Pre=int(input("Enter Present Attendance : "))
        if Pre>(0.75*Tot):
            print ("HURRAY!!",Name,", Attendance Good. Keep it Up")
        else:
            print ("OOPS!",Name,", Short Attendance, Best of Luck")

    if DCode==3:
        print ('''WELCOME TO MOST CHARMING FEATURE
Please Choose

MATHCODE
1. Number of SubSet
2. Trigonometric Value
3. Smallest Integer Function
4. Greatest Integer Function
5. Angle Converter
6. Factorial Calculator
7. nth term of AP
8. Sum to nth term of AP
9. Exponent Calculator
10. Arithmetic Mean
11. nth term of GP
12. Sum to nth term of GP
13. Geomteric Mean
14. Angle Between Two Lines
15. Equation of Line
16. Distance of a Point from Line
17. Quadratic Equation Solver
18. Collinearlity in 2D
19. Distance between two point 2D/3D
20. Midpoint of Two Point 2D/3D
21. Multiple Set Functions
''')
        MCode=int(input("Enter your MATH CODE: "))
        print()
        if MCode==1:
            n=int(input("Enter Number of Elements in Set: "))
            print ("Set has",2**n,"Subsets")
        elif MCode==2:
            d=float(input("Enter Angle in Degrees : "))
            arg=math.radians(d)
            print ("sin",d,"is", math.sin(arg))
            print ("cos",d,"is", math.cos(arg))
            print ("tan",d,"is", math.tan(arg))
            print ("cosec",d,"is", (1/math.sin(arg)))
            print ("sec",d,"is", (1/math.cos(arg)))
            print ("cot",d,"is", (1/math.tan(arg)))
        elif MCode in [3,4]:
            n=float(input("Enter Value:"))
            print ("GREATEST INTEGER FUNCTION", math.floor(n))
            print ("SMALLEST INTEGER FUNCTION", math.ceil(n))
        elif MCode==5:
            n=float(input("Enter Angle : "))
            print (n,"Degrees is", math.radians(n),"Radians")
            print (n,"Radians is", math.degrees(n),"Degrees")
        elif MCode==6:
            n=float(input("Enter Number: "))
            fact,a=1,1
            while a<=n:
                fact*=a
                a+=1
            print ("Factorial of",n,"is",fact)
        elif MCode in [7,8]:
            a=float(input("Enter First Term : "))
            n=float(input("Enter Number of Terms : "))
            d=float(input("Enter Common Difference : "))
            print ("nth term is",a+((n-1)*d))
            print ("Sum to nth term is",(n/2)*(2*a+((n-1)*d)))
        elif MCode==9:
            b=float(input("Enter Base : "))
            e=float(input("Enter Exponent : "))
            print (math.pow(b,e))
        elif MCode in [10,13]:
            a=float(input("Enter First Number : "))
            b=float(input("Enter Second Number : "))
            print ("Arithmetic Mean is",(a+b)/2)
            print ("Geometric Mean is",math.sqrt(a*b))
        elif MCode in [11,12]:
            a=float(input("Enter First Term : "))
            n=float(input("Enter Number of Terms : "))
            r=float(input("Enter Common Ratio : "))
            print ("nth term is",math.pow(r,n-1)*a)
            if r==1:
                print ("Sum to nth term is",n*a)
            else:
                print ("Sum to nth term is",((math.pow(r,n)-1)*a)/(r-1))
        elif MCode==14:
            print('''- TO CALCULATE SLOPE, SORT EQUATION in Ax + By + C=0, and find (-A/B)
- If you know angle, then use Math Code 2 to get slope using tangent function''')
            m1=float(input("Enter Slope of First Line: "))
            m2=float(input("Enter Slope of Second Line: "))
            x=math.fabs((m2-m1)/(1+(m1*m2)))
            a=math.degrees(math.atan(x))
            print ("Angle is",a,"or", 180-a,"Degrees")
          
        elif MCode==15:
            print ('''Which form?
A. y-intercept slope form
B. Intercept Form
C. Normal Form
''')
            i=input("Form: ")
            if i=='A':
                m=float(input("Enter slope: "))
                c=float(input("Enter y-intercept: "))
                print ("y=x",m,"+",c)
            elif i=='B':
                a=float(input("Enter x-intercept: "))
                b=float(input("Enter y-intercept: "))
                print (b,"x+",a,"y=",a*b)
            elif i=='C':
                p=float(input("Enter normal distance from Origin: "))
                a=float(input("Enter angle between normal and positive x-axis: "))
                print (math.cos(math.degrees(a)),"x",math.sin(math.degrees(a)),"y=",p)
            else:
                X='Y'
                continue
        elif MCode==16:
            print ("Reduce Equation in Ax+By+C=0 form")
            A=float(input("Enter A: "))
            B=float(input("Enter B: "))
            C=float(input("Enter C: "))
            x=float(input("Enter Abscissa of Point: "))
            y=float(input("Enter Ordinate of Point: "))
            N,D=math.fabs((A*x)+(B*y)+C),math.sqrt((A**2)+(B**2))
            print (Name,",Distance is",N/D,"units")
        elif MCode==17:
            print ("For Quadration Equation Ax**2 + Bx + C = 0, Enter coefficients:")
            A=int(input("Enter A : "))
            B=int(input("Enter B : "))
            C=int(input("Enter C : "))
            if A==0:
                print ("Oops",Name,"!, Value of a must not be zero")
            else:
                D=B*B-(4*A*C)
                if D>0:
                    R1,R2=(-B + math.sqrt(D))/(2*A),(-B - math.sqrt(D))/(2*A)
                    print (Name,", Roots are REAL and UNEQUAL:",R1,R2)
                elif D==0:
                    R1=-B/(2*A)
                    print (Name,", Roots are REAL and EQUAL:",R1,R1)
                else:
                    print (Name,", Roots are COMPLEX and IMAGINARY!!!")
        elif MCode==18:
            print ("Let three Points be P,Q and R")
            x1=float(input("Enter Abscissa of P:"))
            x2=float(input("Enter Abscissa of Q:"))
            x3=float(input("Enter Abscissa of R:"))
            y1=float(input("Enter Ordinate of P:"))
            y2=float(input("Enter Ordinate of Q:"))
            y3=float(input("Enter Ordinate of R:"))
            if (y1-y3)/(x1-x3)==(y2-y1)/(x2-x1):
                print (Name,",P,Q and R are Collinear")
            else:
                print (Name,",P,Q and R are Not Collinear")
        elif MCode==19:
            print ("Let two points be P and Q")
            x1=float(input("Enter Abscissa of P:"))
            x2=float(input("Enter Abscissa of Q:"))
            y1=float(input("Enter Ordinate of P:"))
            y2=float(input("Enter Ordinate of Q:"))
            z1=float(input("Enter Applicate of P:"))
            z2=float(input("Enter Applicate of Q:"))
            A,B,C=(x2-x1)**2,(y2-y1)**2,(z2-z1)**2
            print(Name,", Length of PQ is",math.sqrt(A+B+C),"units")
        elif MCode==20:
            print ("Let two points be P and Q")
            x1=float(input("Enter Abscissa of P:"))
            x2=float(input("Enter Abscissa of Q:"))
            y1=float(input("Enter Ordinate of P:"))
            y2=float(input("Enter Ordinate of Q:"))
            z1=float(input("Enter Applicate of P:"))
            z2=float(input("Enter Applicate of Q:"))
            A,B,C=(x1+x2)/2,(y2+y1)/2,(z2+z1)/2
            print(Name,",Co-ordinate of Mid-point of PQ is",A,",",B,",",C)
        elif MCode==21:
            print ("INPUT ELEMENTS SEPARATED BY COMMA")
            a=eval(input("Enter element of Set A:"))
            b=eval(input("Enter element of Set B:"))
            A,B=set(a),set(b)
            print ("A∩B",A.intersection(B))
            print ("A∪B",A.union(B))
            print ("A-B", A.difference(B))
            print ("B-A", B.difference(A))
            print('Are A and B disjoint? i.e. A∩B=Ø', A.isdisjoint(B))
            print("A⊃B",A.issubset(B))
            print("B⊃A",B.issubset(A))
            print("A∆B",A.symmetric_difference(B))
        else:
            print (Name,", INVALID MCode!!")
            X='Y'
        
    if DCode==4:
        print ('''Choose CSCode :-)
1. Number System Conversion
2. ASCII Value
3. Sorting Elements
4. Palindrome Checker
5. Leap Year Checker
               ''')
        CSCode=int(input("Enter CSCode: "))
        print()
        if CSCode==1:
            x=int(input("Enter Value in Decimal: "))
            print("Binary",bin(x))
            print("Octal",oct(x))
            print("HexaDecimal",hex(x))
        if CSCode==2:
            A=input("Enter Character:")
            print ("The ASCII value of",A,"is",ord(A))
        if CSCode==3:
            print ("SEPARATE ELEMENTS BY COMMA")
            T=eval(input("Enter Elements: "))
            L=list(T)
            L.sort()
            print("SORTED LIST")
            print(L)
        if CSCode==4:
            print ('''Palindrome is a word, phrase, or sequence that reads the same backwards as forwards.
''')
            x=input("Enter String : ")
            for i in range(len(x)):
                if x[i]==x[length-i-1]:
                    print ("CONGO!!! Yup, it is a Palindrome")
                else:
                    print ("SAD(:-, It is NOT a Palindrome")
        if CSCode==5:
            print ('''A year that contains 366 days, with February 29 as an additional day: occurring
in years whose last two digits are evenly divisible by four, except for centenary
years not divisible by 400
''')
            yr = int(input("Enter any Year : "))
            if yr%4==0:
                if yr%100==0:
                    if yr%400==0:
                        print ("It is a Leap Year")
                    else:
                        print ("It is not a Leap Year")
                else:
                    print ("It is a leap year")
            else:
                print ("It is not a leap year")

    if DCode==5:
        print ('''WELCOME TO SABZEE GAME ARENA :-)

THIS GAME ARENA HAS MULTIPLE GAMES, CHOOSE ANY ONE
1. GRAB THE JERRY!!
2. BE THE HACKER!!
''')
        GCode=int(input("ENTER GAME CODE: "))
        print()
        if GCode==1:
            print ("WELCOME",Name, ", But Sorry, for this Game your Alias Name is TOM :-))))))")
            print ('''I, the JERRY will CHOOSE a number based on your Given Range,
so, Mister Tom Please select Range''')
            l=int(input("Lower Limit: "))
            u=int(input("Upper Limit: "))
            number=random.randint(l,u)
            print ('''Now, Jerry has chosen a Number within the range,
YOU HAVE TO DETECT JERRY'S NUMBER IN 6 GUESSES!!
And thus, you will be able to GRAB JERRY!''')
            G=0
            while G<7:
                guess=int(input("Go Ahead: "))
                G=G+1
                if guess<number:
                    print ("Tom, Your Number is TOO LOW")
                if guess>number:
                    print ("Tom, Your Number is TOO HIGH")
                if guess==number:
                    break
            if guess==number:
                print ("CONGO!!, TOM, YOU WON!!!, You have Grabbed Jerry in ",G,"guesses!!!")
            if guess!=number:
                print ("NOPE!! TOM, YOU LOSE!! Jerry's number was",number)
            print ('''
So, with this Game, you have learned skills of 'EXPERIMENTAL DEDUCTION' ''')
            print ("Thank You,", Name)
        if GCode==2:
            print ("WELCOME",Name,", Are you a Good HACKER?")
            print ('''
WELL, THIS GAME WILL GUIDE YOU THROUGH THE MOST BASIC SKILL THAT A HACKER REQUIRES...............
THE SKILL IS "DEDUCTIVE AND INDUCTIVE REASONING"

I have a SECRET LIST containing 12 Letter
You have to Guess a WORD which must not contain ANYONE of those letters.......

RULES:
- Only English Letters are Supported, Not Digits
- Digits may be considered as part of List
- WORD must contain atleast 5 English Letters
- The Word need not to have Logical Meaning
''')
            L=['A','P','T','M','Q','X','Z','R','S','D','H','N','1','2','3','4','5','6','7','8','9','0',' ']
            M, W='Y',0
            while M=='Y':
                Word=input("ENTER WORD : ")
                Word.upper()
                Word.replace(" ", "")
                if len(Word)<5 :
                    print ("OOPS! You Violated Rule, Select LONG WORD!")
                    continue
                for i in range(len(Word)):
                    if Word[i] in L:
                        W=0
                        print ("Oops! My List has ATLEAST one letter of your Word")
                        break
                    else:
                        W=1
                if W==1:
                    print('''YOU WIN

So, with this Game, you have learned skills of 'DEDUCTION AND INDUCTION' ''')
                    break
                M=input("WANT TO TRY AGAIN?, Enter 'Y': ")
                    
           
            print ("Thank You,", Name,)
    if DCode==6:
        print('''
1. Draw a Star
2. Spiral a Star
3. Constructing a Polygon
4. Illusion
''')
        FC=int(input("Enter Fun Code : "))
        print()
        T=turtle.Turtle()
        if FC==1:
            L=float(input("Enter Length of Each Side : "))
            for i in range(5):
                T.forward(L)
                T.right(144)
            turtle.done()
        elif FC==2:
            for i in range(1,20):
                T.forward(i*10)
                T.right(144)
            turtle.done()
        elif FC==3:
            N=int(input("Enter Number of Sides : "))
            L=float(input("Enter Length of Each Side : "))
            Angle=360/N
            for i in range(N):
                T.forward(L)
                T.right(Angle)
            turtle.done()
        elif FC==4:
            T.speed(10)
            for i in range(1,181):
                T.forward(100)
                T.right(30)
                T.forward(20)
                T.left(60)
                T.forward(50)
                T.right(30)
                T.penup()
                T.setposition(0, 0)
                T.pendown()
                T.right(2)  
            turtle.done()
    
print ('''
THANKS''', Name)
After=datetime.datetime.now()
print ("Well, you spent", After-Now,'''Time in the Student Utility Program!!
Have a Great Time ahead!!''')
