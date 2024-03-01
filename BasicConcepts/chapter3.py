# Functions 

# Functions in programming are blocks of reusable code that perform a specific task. 
# They allow you to break down your code into smaller, 
# manageable parts, making it easier to read, understand, and maintain. 


def greeting(name):
    print("Good moring!",name)
    
    
greeting("Manoj G")


def addition(a,b):
    return a + b


result = addition(10,5)

print(result)


# calculating the student of score and avarage


def student_details(name,scores):
    
    total_score = sum(scores)
    avg = total_score / len(scores)

    grade = ""
    
    if  avg >= 90:
        grade = "A"
    elif 80 <= avg >= 90:
        grade = "B"
    elif 70 <= avg >= 80:
        grade = "C"
    elif 60 <= avg >= 70:
        grade = "d"
    else:
        grade = "e"
        
    return f"This Student name is {name} and his score is {grade}"    
        
   
   
studentScores = [90,90,100,90,70,100]



studentResult =  student_details("Manoj",studentScores)


print(studentResult)