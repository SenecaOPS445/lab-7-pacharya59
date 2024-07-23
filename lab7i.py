# Student ID: pacharya9(100706225)
def function1():
    global schoolName
    schoolName = 'SICT'
    print('print() in function1 on schoolName:', schoolName)

def function2():
    global schoolName
    schoolName = 'SSDO'
    print('print() in function2 on schoolName:', schoolName)

schoolName = 'Seneca'
print('print() in main on schoolName:', schoolName)
function1()
print('print() in main on schoolName:', schoolName)  # This should print 'SICT'
function2()
print('print() in main on schoolName:', schoolName)  # This should print 'SSDO'

