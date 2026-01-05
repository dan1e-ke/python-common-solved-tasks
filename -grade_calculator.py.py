Score=float(input("Enter the score (0-100): "))  #get score from user
if Score<0 or Score>100:  #check for valid score

    print("Invalid score. Please enter a score between 0 and 100.") #

else: #check the grade based on score

    if Score>=90:    #range for one to score an A
        Grade='A',"Excellent"

    elif Score>=80:  #range for one to score a B
        Grade='B',"Very Good"

    elif Score>=70:  #range for one to score a C
        Grade='C',"Good"

    elif Score>=60:  #range for one to score a D
        Grade='D',"Pass"

    else:  #range for one to score an F
        Grade='F',"Needs Improvement"

    print(f"Grade:{Grade[0]}")   #print the grade
    print(f"Performance:{Grade[1]}")  # End of the program
          
        
       
