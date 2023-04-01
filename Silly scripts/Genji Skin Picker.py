import random

skinList = {1: 'CYBER DEMON', 2: 'BAINU', 3: 'KARASU-TENGU', 4: 'SENTAI'
    , 5: 'CONTENDERS AWAY', 6: 'CONTENDERS HOME', 7: 'SEOUL DYNASTY',
    8: 'SEOUL DYNASTY AWAY', 9: 'SKELETON', 10: 'TORONTO DEFIANT'
    , 11: 'TORONTO DEFIANT AWAY', 12: 'OCHRE', 13: 'OVERWATCH 1'
    , 14: 'OVERWATCH 2'}

selectedSkinList = []
def ran():
    return(random.randint(1, 14))
def pick():
    randomNum = ran()
    while skinList[randomNum] in selectedSkinList:
        randomNum = ran()
    return(skinList[randomNum])

while len(selectedSkinList) != 13:
    selectiton = pick()
    if selectiton in selectedSkinList:
        selectiton = pick()
    selectedSkinList.append(selectiton)
    print(selectiton)
    if len(selectedSkinList) != 13:
        if input() == 1:
            break
print('\nAll skins picked!')
selectedSkinList = []