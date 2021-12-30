from packages import calculator as clc #Importing a module from a package
from prettytable import PrettyTable #Importing a Python Library

class SubjectList():
    
    #Constructor
    def __init__(self):
        self.numberOfSubject = 0 #Total subjects in a subject list
        self.subjects = [] #List of Subject() objects
    
    #Function to add a new Subject() to subjects[] list
    def addSubject(self, name): 
        self.subjects.append(Subject(name))
        self.numberOfSubject = self.numberOfSubject + 1
    
    #Function to return the index of a specified Subject() in subjects[] list
    def getSubjectIndex(self, name):
        names = []
        for i in range (len(self.subjects)):
            names.append(self.subjects[i].name) #Make a list only containing subjects name.
        x = names.index(name)
        return x
    
    #Function to print a detailed score data for a specified subjectName and studentName
    def getScoreData(self, subjectName, studentName):
        subjectIndex = self.getSubjectIndex(subjectName) #Get the index of subject that is being searched.
        subject = self.subjects[subjectIndex] #Get the Subject() object that is being searched according to its index.
        
        studentIndex = subject.getStudentIndex(studentName) #Get the index of student that is being searched.
        score = subject.subjectScores[studentIndex] #Get the ScoreDetail() object that is being searched according to its index.
        t = PrettyTable(['No.', 'Student Name', 'Subject', 'Daily Task', 'Quiz', 'Mid Exam', 'Final Exam', 'Total'])

        #Print all data from the retrieved ScoreDetail()
        t.add_row([(i+1),
                   score.studentName,
                   score.subjectName, 
                   score.dailyTaskScore, 
                   score.quizScore, 
                   score.midExamScore, 
                   score.finalExamScore,
                   "{:.2f}".format(score.totalScore)
                  ])

        print("\n")
        print(t)

    #Function to edit scores data for a specified subjectName and studentName
    def editScoreData(self, subjectName, studentName, a, b, c, d):
        subjectIndex = self.getSubjectIndex(subjectName) #Get the index of subject that is being searched.
        subject = self.subjects[subjectIndex] #Get the Subject() object that is being searched according to its index.
        
        studentIndex = subject.getStudentIndex(studentName) #Get the index of student that is being searched.
        score = subject.subjectScores[studentIndex] #Get the ScoreDetail() object that is being searched according to its index.
        
        score.dailyTaskScore = a #Assign inputed dailyTaskScore to the retrieved ScoreDetail()
        score.quizScore = b #Assign inputed quizScore to the retrieved ScoreDetail()
        score.midExamScore = c #Assign inputed midExamScore to the retrieved ScoreDetail()
        score.finalExamScore = d #Assign inputed finalExamScore to the retrieved ScoreDetail()
        score.totalScore = ((20 * a) + (15 * b) + (30 * c) + (35 * d)) / 100 #Re-calculate the total / overall score  
        
class Class():
    
    #Constructor
    def __init__(self, number, className):
        self.number = number #Class Level
        self.className = className #Class Name
        self.numberOfStudent = 0 #Number of Student in the class
        self.students = [] #List of Student() objects
        self.subjectList = SubjectList() #Object of SubjectList()
    
    #Function to add a new Student() to students[] list
    def addStudent(self, name):
        self.students.append(Student(name, (self.numberOfStudent + 1)))
        self.numberOfStudent = self.numberOfStudent + 1
    
    #Function to get a Student() by name
    def getStudent(self, name):
        names = []
        for i in range (len(self.students)):
            names.append(self.students[i].name) #Make a list only containing students name.
        x = names.index(name)
        return self.students[x] #Return a Student() by the found index according to the specified name.
        
    #Function to get the name of first ranked Student()
    def getFirstRank(self): 
        scores = []
        for i in range (len(self.students)):
            scores.append(self.students[i].totalScore) #Make a list only containing students' totalScore.
            
        maxScore, firstRankIndex = clc.getMax(scores) #Get maximum value from scores and its index.
        return self.students[firstRankIndex].name #Return the name of the first ranked student with the maximum totalScore.
    
    #Function to get the name of last ranked Student()
    def getLastRank(self):
        scores = []
        for i in range (len(self.students)):
            scores.append(self.students[i].totalScore) #Make a list only containing students' totalScore.
            
        maxScore, lastRankIndex = clc.getMin(scores) #Get minimum value from scores and its index.
        return self.students[lastRankIndex].name #Return the name of the last ranked student with the minimum totalScore.

    #Function to print out class report
    def printClassData(self):
        t = PrettyTable(['No.', 'Student Name', 'Total Score', 'Mean Score'])

        for i in range(len(self.students)): #Loop through all Student() in the Class()'s students[] list.
            t.add_row([(i+1), #Print out number according to loop
                       self.students[i].name, #Print student name
                       "{:.2f}".format(self.students[i].totalScore), #Print student's totalScore
                       "{:.2f}".format(self.students[i].mean) #Print student's mean score
                      ])

        print("\n")
        print(t)
        
class Student():
    
    #Constructor
    def __init__(self, name, studentNumber):
        self.name = name #The student's name
        self.studentNumber = studentNumber #The student's number
        self.totalScore = 0 #The student's total score for all subjects.
        self.mean = 0 #The student's mean score from all subject
        self.studentScores = [] #The student's detailed score data / a list of ScoreDetail() objects.
        
    #Function to add a new ScoreDetail() to studentScores[] list
    def addStudentScore(self, scoreDetail):
        self.studentScores.append(scoreDetail)
        self.setMeanTotal()
    
    #Function to set or renew the mean score and total score of the student
    def setMeanTotal(self):
        scores = []
        for i in range (len(self.studentScores)):
            scores.append(self.studentScores[i].totalScore) #Make a list only containing students' totalScore.
        
        self.mean = clc.getMean(scores) #Calculate the mean value using calculator module's function
        self.totalScore = clc.getTotal(scores) #Calculate the total value using calculator module's function
        
    #Function to print detailed scores of the student for every subject
    def printStudentScores(self):
        t = PrettyTable(['No.', 'Subject', 'Daily Task', 'Quiz', 'Mid Exam', 'Final Exam', 'Total'])

        for i in range(len(self.studentScores)):  #Loop through all ScoreDetail() in the Student()'s studentScores[] list.
            t.add_row([(i+1), #Print number according to loop
                       self.studentScores[i].subjectName,  #Print subject name
                       self.studentScores[i].dailyTaskScore, #Print Daily Task Score
                       self.studentScores[i].quizScore,  #Print Quiz Score
                       self.studentScores[i].midExamScore, #Print Middle Exam Score
                       self.studentScores[i].finalExamScore, #Print Final Exam Score
                       "{:.2f}".format(self.studentScores[i].totalScore) #Print totalScore with format of only two decimal number
                      ])

        print("\n")
        print(t)

class ScoreDetail():
    
    #Constructor
    def __init__(self, studentName, subjectName):
        self.studentName = studentName #Name of the student who owns the score
        self.subjectName = subjectName #Name of the subject that gets this score
        self.dailyTaskScore = 0 #Daily Task Score
        self.quizScore = 0 #Quiz Score
        self.midExamScore = 0 #Middle Exam Score
        self.finalExamScore = 0 #Final Exam Score
        self.totalScore = 0 #Overall Score
    
    def setScore(self, a, b, c, d):
        self.dailyTaskScore = a
        self.quizScore = b
        self.midExamScore = c
        self.finalExamScore = d
        self.totalScore = ((20 * a) + (15 * b) + (30 * c) + (35 * d)) / 100 #Formula to get the Overall Score

class Subject():
    
    #Constructor
    def __init__(self, name):
        self.name = name #Subject Name
        self.subjectScores = [] #The subject's score data / a list of ScoreDetail() objects.
        self.mean = 0 #Mean value of all student's score for this subject
        self.maxScore = 0 #Max value of all student's score for this subject
        self.minScore = 0 #Min value of all student's score for this subject
        self.maxName = "" #Name of student who got the highest score
        self.minName = "" #Name of student who got the lowest score
    
    #Function to add a new ScoreDetail() to subjectScores[] list
    def addSubjectScore(self, scoreDetail):
        self.subjectScores.append(scoreDetail)
        self.setMaxMinMean()
    
    #Function to set or renew the maximum value, minimum value, mean value, 
        # name of the student who got the highest and lowest score.
    def setMaxMinMean(self):
        scores = []
        for i in range (len(self.subjectScores)):
            scores.append(self.subjectScores[i].totalScore) #Make a list only containing students' totalScore in this subject.
        
        self.maxScore, maxIndex = clc.getMax(scores) #Get highest score using calculator module and the student index
        self.minScore, minIndex = clc.getMin(scores) #Get lowest score using calculator module and the student index
        self.maxName = self.subjectScores[maxIndex].studentName #Retrieve student with highest score's name
        self.minName = self.subjectScores[minIndex].studentName #Retrieve student with lowest score's name
        self.mean = clc.getMean(scores) #Get mean value of all student score in this subject
        
    #Function to get student index by name
    def getStudentIndex(self, name):
        names = []
        for i in range (len(self.subjectScores)):
            names.append(self.subjectScores[i].studentName) #Make a list only containing students name.
        x = names.index(name)
        return x    
    
    def printSubjectScores(self):
        t = PrettyTable(['No.', 'Student Name', 'Daily Task', 'Quiz', 'Mid Exam', 'Final Exam', 'Total'])

        for i in range(len(self.subjectScores)): #Loop through all ScoreDetail() in the Subject()'s subjectScores[] list.
            t.add_row([(i+1), #Print number according to loop
                       self.subjectScores[i].studentName, #Print student name
                       self.subjectScores[i].dailyTaskScore, #Print DailyTaskScore
                       self.subjectScores[i].quizScore, #Print Quiz Score
                       self.subjectScores[i].midExamScore, #Print Middle Exam Score
                       self.subjectScores[i].finalExamScore, #Print final exam score
                       "{:.2f}".format(self.subjectScores[i].totalScore) #Print overall score
                      ])

        print("\n")
        print(t)
    
    #Function to edit and rewrite the file where a score is just edited by user
    def rewriteFile(self):
        filename = self.name + ".txt"
        f = open(filename, "w")
        f.write("")
        f.close()
        
        f = open(filename, "a")
        for i in range(len(self.subjectScores)):
            if(i == 0):
                newLine = self.subjectScores[i].studentName + " - " + self.subjectScores[i].subjectName + " - " + str(self.subjectScores[i].dailyTaskScore) + " - " + str(self.subjectScores[i].quizScore) + " - " + str(self.subjectScores[i].midExamScore) +  " - " + str(self.subjectScores[i].finalExamScore)
            else:
                newLine = "\n" + self.subjectScores[i].studentName + " - " + self.subjectScores[i].subjectName + " - " + str(self.subjectScores[i].dailyTaskScore) + " - " + str(self.subjectScores[i].quizScore) + " - " + str(self.subjectScores[i].midExamScore) +  " - " + str(self.subjectScores[i].finalExamScore)
            f.write(newLine)
        f.close()

#Function to load and store a score data from a txt file 
def getAllScores(filename):
    with open(filename) as f:
        for line in f:
            part = line.split(" - ")
            scoreDetail = ScoreDetail(part[0], part[1])
            scoreDetail.setScore(int(part[2]), int(part[3]), int(part[4]), int(part[5]))
            
            subjectIndex = class10A.subjectList.getSubjectIndex(part[1])
            class10A.subjectList.subjects[subjectIndex].addSubjectScore(scoreDetail)

            class10A.getStudent(part[0]).addStudentScore(scoreDetail)

#Function to print out menu options       
def printMenu():
    print("\nMENU : \n"
          "1. Check Out Scores by Subject\n"
          "2. Check Out Scores by Student\n"
          "3. Search Specific Data\n"
          "4. Class Report\n"
          "5. Exit")

class10A = Class(10, "10A") #Object of Class()

with open('Subjects.txt') as f:
    for line in f:
        class10A.subjectList.addSubject(line.splitlines()[0]) #Load and store all subject list
        
with open('Students.txt') as f:
    for line in f:
        class10A.addStudent(line.splitlines()[0]) #Load and store all student liss
        
getAllScores("Mathematics.txt") #Load and store mathematics score
getAllScores("Physics.txt") #Load and store physics score
getAllScores("Chemistry.txt") #Load and store chemistry score
getAllScores("Biology.txt") #Load and store biology score
getAllScores("Indonesian Language.txt") #Load and store Indonesian Language score
getAllScores("English.txt") #Load and store English score

menu = 0
while(menu != 5):
    printMenu()
    menu = int(input("\nChoose a menu [1-5] : "))
    
    print("")
    
    if(menu == 1):
        for i in range(class10A.subjectList.numberOfSubject):
            print("\t" + str(i+1) + ". " + class10A.subjectList.subjects[i].name)
        
        pick = int(input(("\n\tPick a Subject to See Detail [0 to Back] : ")))
        
        if(pick > 0 and pick < 7):
            print("SUBJECT NAME :", class10A.subjectList.subjects[pick-1].name)
            print("HIGHEST SCORE :", class10A.subjectList.subjects[pick-1].maxName, 
                  "-", class10A.subjectList.subjects[pick-1].maxScore)
            print("LOWEST SCORE :", class10A.subjectList.subjects[pick-1].minName, 
                  "-", class10A.subjectList.subjects[pick-1].minScore)
            print("AVERAGE SCORE :", class10A.subjectList.subjects[pick-1].mean)
            class10A.subjectList.subjects[pick-1].printSubjectScores()
        
        edit = input("\nEdit a data? [y/n] : ")
        if(edit == "y"):
            studentName = input("\n\tStudent Name : ")
            subjectName = input("\tSubject : ")
            
            dailyTaskScore = int(input("\n\tDaily Task Score [Integer 0 - 100] : "))
            quizScore = int(input("\tQuiz Score [Integer 0 - 100] : "))
            midExamScore = int(input("\tMiddle Exam Score [Integer 0 - 100] : "))
            finalExamScore = int(input("\tFinal Exam Score [Integer 0 - 100] : "))
        
            class10A.subjectList.editScoreData(subjectName, studentName, 
                                               dailyTaskScore, quizScore, midExamScore, finalExamScore)
            
            subjectIndex = class10A.subjectList.getSubjectIndex(subjectName)
            class10A.subjectList.subjects[subjectIndex].rewriteFile()
        
    if(menu == 2):
        for i in range(class10A.numberOfStudent):
            print("\t" + str(i+1) + ". " + class10A.students[i].name)
        
        pick = int(input(("\n\tPick a Student to See Detail [0 to Back] : ")))
        
        if(pick > 0 and pick < 11):
            print("STUDENT NAME :", class10A.students[pick-1].name)
            print("TOTAL SCORE :", class10A.students[pick-1].totalScore)
            print("MEAN SCORE :", class10A.students[pick-1].mean)
            class10A.students[pick-1].printStudentScores()
            
        edit = input("\nEdit a data? [y/n] : ")
        if(edit == "y"):
            studentName = input("\n\tStudent Name : ")
            subjectName = input("\tSubject : ")
            
            dailyTaskScore = int(input("\n\tDaily Task Score [Integer 0 - 100] : "))
            quizScore = int(input("\tQuiz Score [Integer 0 - 100] : "))
            midExamScore = int(input("\tMiddle Exam Score [Integer 0 - 100] : "))
            finalExamScore = int(input("\tFinal Exam Score [Integer 0 - 100] : "))
        
            class10A.subjectList.editScoreData(subjectName, studentName, 
                                               dailyTaskScore, quizScore, midExamScore, finalExamScore)
            
            subjectIndex = class10A.subjectList.getSubjectIndex(subjectName)
            class10A.subjectList.subjects[subjectIndex].rewriteFile()
            
    if(menu == 3):
        studentName = input("\n\tStudent Name : ")
        subjectName = input("\tSubject : ")
        class10A.subjectList.getScoreData(subjectName, studentName)
        
    if(menu == 4):
        print("============================CLASS 10A REPORT============================")
        print("\nFIRST RANK :", class10A.getFirstRank())
        print("LAST RANK :", class10A.getLastRank())
        class10A.printClassData()
