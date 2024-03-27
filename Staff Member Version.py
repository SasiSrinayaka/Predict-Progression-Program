# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: ....... 20220489 .........     # Date: ....... 21.04.2023 ..........

# The progression outcome in each academic year

print("\t\t______This is designed for the use of Staff Members._____\n")
#Defined the variables
pass_mark = 0
defer_mark = 0
fail_mark = 0
Return = True  #use the while true

progress = 0
trailer = 0
retriever = 0
exclude = 0

progress_list=[]


# Create Histrogram chart
def Histogram():

    print("\nHistogram\n")
    print("Progress  ",progress," : ","*"*progress)
    print("Trailer   ",trailer," : ","*"*trailer)
    print("Retriever ",retriever," : ","*"*retriever)
    print("Excluded  ",exclude," : ","*"*exclude)
    total=progress+trailer+retriever+exclude
    print()
    print(total,"outcomes in total")
    
#Input the marks use the while
while(Return):
    while(True):
        try:
            pass_mark=int(input("Please enter your credits at pass : "))
            if(0<=pass_mark<=120 and pass_mark%20==0):
                 break
            else:
                print("Out of range.") #because marks is not in range
                    
                    
        except ValueError:
            print("Integer required")

    while(True):
        try:
            defer_mark=int(input("Please enter your credit at defer : "))
            if(0<=defer_mark<=120 and defer_mark%20==0):
                 break
            else:
                print("Out of range.") #because marks is not in range
                    
                    
        except ValueError:
            print("Integer required")

    while(True):
        try:
            fail_mark=int(input("Please enter your credit at fail : "))
            if(0 <= fail_mark <= 120 and fail_mark % 20 == 0):
                 break
            else:
                print("Out of range.") #because marks is not in range
                    
                    
        except ValueError:
            print("Integer required")


# To find out if the sum of pass mark, defer mark and fail mark is equal to 120
    total = pass_mark + defer_mark + fail_mark
    while(True):
        if(total > 120 or total != 120):
            print("Total incorrect")
            break
        elif (pass_mark==120 and defer_mark==0 and fail_mark==0):
            print("Progress")
            progress_list.append(f"(Progress - {pass_mark} , {defer_mark} , {fail_mark})")
            progress=progress+1
            break
        elif (pass_mark==100 and 0<=defer_mark<=20 and  0<=fail_mark<=20):
            print("Progress (module trailer)")
            progress_list.append(f"(Progress (module trailer) - {pass_mark} , {defer_mark} , {fail_mark})")
            trailer=trailer+1
            break
        elif (0<= pass_mark<=80 and 0<=defer_mark<=120 and 0<=fail_mark<=60):
            print("module retriever")
            progress_list.append(f"(module retriever - {pass_mark} , {defer_mark} , {fail_mark})")
            retriever=retriever+1
            break
        elif (0<=pass_mark<=40 and 0<=defer_mark<=40 and 80<=fail_mark<=120):
            print("Exclude")
            progress_list.append(f"(Exclude - {pass_mark} , {defer_mark} , {fail_mark})")
            exclude=exclude+1
            break

# Ask the user if the program continues
    print("\nWould you like to enter another set of data?")
    choice=input("Enter 'y' for yes or 'q' to quit and view results: ")#if user said yes  print it will be continue or if not the program will stop
    print()
    if(choice=="y"):
        Return==True
    elif(choice=="q"):
        repeat=False
        Histogram()
        print("\n")
        print(progress_list) #display the list output
        file = open('Progress_outcome.txt','w')
        for item in progress_list:
            file.write(item+"\n")
        file.close()
    else:
        print("Invalid input")
        break

    
    
        


                                    

