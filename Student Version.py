# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: ....... 20220489 .........     # Date: ....... 21.04.2023 ..........

# The progression outcome in each academic year

print("\t\t______This is designed for the use of Students._____\n")
#Defined the variables
pass_mark=0
defer_mark=0
fail_mark=0
Return=True #use the while true

#Input the marks use the while    
while(Return):
    while(True):
        try:
            pass_mark=int(input("Please enter your credits at pass : "))
            if(0<=pass_mark<=120 and pass_mark%20==0):
                break
            else:
                print("Out of range.")#because marks is not in range
                        
        except ValueError:
                print("Integer required")

    while(True):
        try:
            defer_mark=int(input("Please enter your credit at defer : "))
            if(0<=defer_mark<=120 and defer_mark%20==0):
                break
            else:
                print("Out of range.")#because marks is not in range
                        
                        
        except ValueError:
            print("Integer required")

    while(True):
        try:
            fail_mark=int(input("Please enter your credit at fail : "))
            if(0<=fail_mark<=120 and fail_mark%20==0):
                break
            else:
                print("Out of range.")#because marks is not in range
                        
                        
        except ValueError:
            print("Integer required")
            

# To find out if the sum of pass mark, defer mark and fail mark is equal to 120
    total=pass_mark+defer_mark+fail_mark
    if(total>120 or total!=120):
        print("Total incorrect\n")
    elif (pass_mark==120 and defer_mark==0 and fail_mark==0):
        print("Progress")
        Return=False
    elif (pass_mark==100 and 0<=defer_mark<=20 and  0<=fail_mark<=20):
        print("Progress (module trailer)")
        Return=False
    elif (0<= pass_mark<=80 and 0<=defer_mark<=120 and 0<=fail_mark<=60):
        print("module retriever")
        Return=False
    elif (0<=pass_mark<=40 and 0<=defer_mark<=40 and 80<=fail_mark<=120):
        print("Exclude")
        Return=False

    
    
        


                                    

