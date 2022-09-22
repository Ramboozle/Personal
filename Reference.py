#~~~~~~~~~~~~Variables~~~~~~~~~~~~#
String = 'Hello!'
Integer = 23
Float = 12.3
print(String,Integer,Float)
#~~~~~~~~~~~~Lists~~~~~~~~~~~~#
List = [1,2,3,4,5]
List.append(6) #to add another element to the list
List[2] = 3.14
print(List)
#~~~~~~~~~~~~Dictionary~~~~~~~~~~~~#
Dictionary = {'Hello':'an informal greeting'}
print(Dictionary['Hello'])
Dictionary['Goodbye'] = 'a way to announce you are leaving'
print(Dictionary['Goodbye'])
#~~~~~~~~~~~~Files-Read~~~~~~~~~~~~#
File = open('/Users/ramboozle/Library/Mobile Documents/com~apple~CloudDocs/Python/School Work/Things used for code/read.txt','rt') #rt at the end specifies read text
print(File.read()) #prints the whole file
print(File.read(5)) #will print the specified amount of charicters in the file
print(File.readline(40)) #will onlt print the row selected. adding numbers to the (works similarly to the read command)
File.close()
#~~~~~~~~~~~~Files-Write~~~~~~~~~~~~#
File = open('/Users/ramboozle/Library/Mobile Documents/com~apple~CloudDocs/Python/School Work/Things used for code/write.txt','wt') #Write Text this time, the directory leads to a non existant file so python will create one there
File.writelines('this file was created and written to!')
File.close()
File = open('/Users/ramboozle/Library/Mobile Documents/com~apple~CloudDocs/Python/School Work/Things used for code/write.txt','rt')
print(File.read())
#~~~~~~~~~~~~Procedures~~~~~~~~~~~~#
def textprocedure(): #names the procedure
    print('procedure!') #every time the procedure is called it will print whats here
textprocedure() #calls upon the prodedure

def addprocedure(num1,num2): #names the procedure
    num3 = num1 + num2 #variables created inside of procedures will stay in the procedure
    return(num3) #variables created inside of a procedure cannot leave the procedure unless returend
num1 = 1 #global variables have to be passed into the variable when it is called
num2 = 2
calcout = addprocedure(num1,num2) #sets the output of the procedure to a global variable
print('answer is ',calcout)
#~~~~~~~~~~~~REGEX (regular expressions)~~~~~~~~~~~~#
import re #imports regular expressions
txt = "The quick brown fox jumps over the lazy dog"
regexa = re.findall("a", txt) #will find and store all of the occourances that match the search criteria( in this case just the letter a)
regexspace = re.findall("^ ", txt)
print(regexa)
print(regexspace)