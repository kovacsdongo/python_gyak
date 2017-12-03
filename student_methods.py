import pprint

admins = {"admin": "1234", 'aa': 'aa'}
studentDict = {'bob': [4, 7, 9],
               'jeff': [1, 4, 5]}
print studentDict
for k in studentDict:
    print k



def addmember():
    nameEnter = raw_input("student name: ")
    if nameEnter not in studentDict:
            if nameEnter not in studentDict and nameEnter != studentDict[k]:
                print 'adding member...'
                studentDict.update({nameEnter:[]})
    else:
        print 'member already be...'
    pprint.pprint(studentDict)

def entergardes():
    nameEnter = raw_input("student name: ")
    gradeEnter = raw_input("grade: ")
    if nameEnter in studentDict:
        print 'adding grade...'

        grades = gradeEnter.split(',')
        print grades[0]
        print grades[1]
        for i in grades:
        #studentDict[nameEnter].append(grades)
            studentDict[nameEnter].append(int(i))
    else:
        print "student not exists"
    print studentDict

def removeStudent():
    nameToRemove = raw_input("add the student name to delete: ")
    if nameToRemove in studentDict:
        print "deleting studet..."
        del studentDict[nameToRemove]
    else:
        print "invalid name try again..."
        removeStudent()
    print studentDict

def average():
    for eachStudents in studentDict:
        gradeList = studentDict[eachStudents]
        avg = statistics.mean(gradeList)
        print (eachStudents, 'has an avg grade of: %3d,2' %avg)

def main():
    print('''
    1 - enter grades
    2 - remove students
    3 - students average
    4 - add member
    5 - exit
    ''')
    action = raw_input("what do u want to do? ")
    if (action=="1"):
        entergardes()
    if (action == "2"):
        removeStudent()
    elif (action == "3"):
        average()
    elif (action == "4"):
        addmember()
    elif (action == "5"):
        print 5
    else:
        print (" no valid number action")
