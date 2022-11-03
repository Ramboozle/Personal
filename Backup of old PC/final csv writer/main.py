import fileinput
import re
import csv
filein = open('/Users/ramboozle/PycharmProjects/final csv writer/bunch_location_edit.csv','r')
fileout = open('/Users/ramboozle/PycharmProjects/final csv writer/output.csv', 'w')
reader = csv.reader(filein)
writer = csv.writer(fileout)
writer.writerow(['BlockID','TreeID','FrameID','Xmin','Ymin','Xmax','Ymax'])
reader.__next__()
#print('--------------------')
for row in reader:
    #print(row)
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
    data = [BlockID, TreeID, BID, XMin, YMin, XMax, YMax]
    writer.writerow(data)
    #print('BlockID',BlockID)
    #print('TreeID',TreeID)
    #print('BID',BID)
    #print('Realframe',realframe)
    #print('BoxCo',BoxCo)
    #print('XMin',XMin)
    #print('YMin',YMin)
    #print('XMax',XMax)
    #print('Ymax',YMax)
    #print('data',data)
    #print('--------------------')
print('Finished :D')