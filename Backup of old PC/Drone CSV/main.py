import re
import csv
file = open('/Users/ramboozle/Library/Mobile Documents/com~apple~CloudDocs/Projects/Drone script thing/bunch_location.csv','r')
reader = csv.reader(file)
reader.__next__()
for row in reader:
    print(row[1][12:])
    frame = re.findall('\d', row[2])
    if len(frame) > 3:
        realframe = frame[0]+frame[1]+frame[2]+frame[3]
    elif len(frame) >2:
        realframe = frame[0]+frame[1]+frame[2]
    elif len(frame) >1:
        realframe = frame[0]+frame[1]
    else:
        realframe = frame[0]
    print(realframe)
    print('--------------------')
with open('/Users/ramboozle/PycharmProjects/CSV write/Test.csv','w') as file:
    writer = csv.writer(file)
    header = ['BlockID','TreeID','FrameID','Xmin','Ymin','Xmax','Ymax']
    writer.writerow(header)