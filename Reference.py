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
#~~~~~~~~~~tkinter~~~~~~~~~~#
import time
import tkinter as tk#insted of typing Tkinter every time we want to use the library we can just type tk. insted of tkinter. saving us time
#~~~~~~~~~~Basic window~~~~~~~~~~#
root = tk.Tk() #creates an object that is called root
#root.geometry('100x100') #changes the size in pixels of the window. The winodw will auto size if not specified
root.title('hello') #changes the text at the top of the window
#~~~~~~~~~~Label~~~~~~~~~~#
label = tk.Label(root, text='Hello World!') #creates a label called 'label' (creative I know)
label.pack() #packing is when the variable is put into the window in this case label is being packed into root. packing will always place thing in the next free slot
#~~~~~~~~~~Text~~~~~~~~~~#
text = tk.Text(root, height=3) #this makes a text box that is 3 row tall
text.pack() #packs the textbox into the 'root' object
#~~~~~~~~~~Entry~~~~~~~~~~#
entry = tk.Entry(root) #similar to text but is only 1 row tall no matter what
entry.pack() #packs the entry field into root
#~~~~~~~~~~Button~~~~~~~~~~#
button = tk.Button(root, text='Button!')
button.pack()
#~~~~~~~~~~Frames~~~~~~~~~~#
frame = tk.Frame(root) #creates a fram object under root
frame.columnconfigure(0, weight=1) #these 3 commands create a 3x3 grid layout for widgets
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
but1 = tk.Button(frame,text='1') #every single one of these fillowing 9 commands all do the same thing, they just store the button in a specific cell of the frame
but1.grid(row=0,column=0,sticky=tk.W+tk.E) #specifies where on the grid the button will go
but2 = tk.Button(frame,text='2')
but2.grid(row=0,column=1,sticky=tk.W+tk.E)
but3 = tk.Button(frame,text='3')
but3.grid(row=0,column=2,sticky=tk.W+tk.E)
but4 = tk.Button(frame,text='4')
but4.grid(row=1,column=0,sticky=tk.W+tk.E)
but5 = tk.Button(frame,text='5')
but5.grid(row=1,column=1,sticky=tk.W+tk.E)
but6 = tk.Button(frame,text='6')
but6.grid(row=1,column=2,sticky=tk.W+tk.E)
but4 = tk.Button(frame,text='7')
but4.grid(row=2,column=0,sticky=tk.W+tk.E)
but5 = tk.Button(frame,text='8')
but5.grid(row=2,column=1,sticky=tk.W+tk.E)
but6 = tk.Button(frame,text='9')
but6.grid(row=2,column=2,sticky=tk.W+tk.E)
frame.pack(fill='x') #packs everything in the frame object
#~~~~~~~~~~Opening Window~~~~~~~~~~#
root.mainloop() #opens 'root' as a window
#~~~~~~~~~~Opening Window~~~~~~~~~~#
