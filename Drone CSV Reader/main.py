import re
import csv
filein = open('/Users/ramboozle/Library/Mobile Documents/com~apple~CloudDocs/Python/Personal/Drone CSV Reader/bunch_location.csv','r')
fileout = open('/Users/ramboozle/Library/Mobile Documents/com~apple~CloudDocs/Python/Personal/Drone CSV Reader/Output.csv', 'w')
reader = csv.reader(filein)
writer = csv.writer(fileout)
reader.__next__()
print('--------------------')
for row in reader:
    BlockID = row[0][10:22]
    TreeID = row[0][23:29]
    BID = row[1][12:]
    frame = re.findall('\d', row[2])
    realframe = ''.join(frame)
    BoxCo = re.findall('\d+',row[3][49:])
    XMin = BoxCo[0]
    YMin = BoxCo[1]
    XMax = BoxCo[2]
    YMax = BoxCo[3]
    print(BlockID)
    print(TreeID)
    print(BID)
    print(realframe)
    print(XMin)
    print(YMin)
    print(XMax)
    print(YMax)
    print('--------------------')
    data = [BlockID,TreeID,BID,XMin,YMin,XMax,YMax]
    writer.writerow([data])
