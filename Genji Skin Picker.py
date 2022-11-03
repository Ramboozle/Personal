import random
skinList = {1 :'CYBER DEMON',2:'BAINU',3:'KARASU-TENGU',4:'SENTAI'
            ,5:'CONTENDERS AWAY',6:'CONTENDERS HOME',7:'SEOUL DYNASTY',
            8:'SEOUL DYNASTY AWAY',9:'SKELETON',10:'TORONTO DEFIANT'
            ,11:'TORONTO DEFIANT AWAY',12:'OCHRE',13:'OVERWATCH 2'
            ,14:'OVERWATCH 1'}
list = []
while input() != 'f':
    x = random.randint(1,14)
    while x in list:
        x = random.randint(1, 14)
    list.append(x)
    print('The random number is',x,'and is the skin',skinList[x])
    if len(list) == 13:
        list = []
        print('list complete! starting again')
