def coord(x,y):
    "Convert world coordinates to pixel coordinates."
    return x+320, y+240


def findzone(x1, y1, x2, y2):
    delx = x2 - x1 
    dely = y2 - y1

    if abs(delx) > abs(dely):
        if (delx>0 and dely>0):
            return 0
        if (delx<0 and dely>0):
            return 3
        if (delx<0 and dely<0):
            return 4
        if (delx>0 and dely<0):
            return 7
    else:
        if (delx>0 and dely>0):
            return 1
            
        if (delx<0 and dely>0):
            return 2
                
        if (delx<0 and dely<0):
            return 5
                
        if (delx>0 and dely<0):
            return 6

def findXY(x, y, zone):
    if zone ==0:
        return x,y, zone
        return x,y
    if zone ==1:
        temp = x
        x = y
        y = temp
        return x,y
    if zone ==2:
        temp = x
        x = y
        y = -temp
        return x,y
    if zone ==3:
        x = -x
        return x,y
    if zone ==4:
        x = -x
        y = -y
        return x,y
    if zone ==5:
        temp = x
        x = -y
        y = -temp
        return x,y
    if zone ==6:
        temp = x
        x = -y
        y = temp
        return x,y
    if zone ==7:
        y = -y
        return x,y

def findInitialZone(x, y, zone):
    if zone ==0:
        return x,y
    if zone ==1:
        temp = x
        x = y
        y = temp
        return x,y
    if zone ==2:
        temp = x
        x = -y
        y = temp
        return x,y
    if zone ==3:
        x = -x
        return x,y
    if zone ==4:
        x = -x
        y = -y
        return x,y
    if zone ==5:
        temp = x
        x = -y
        y = -temp
        return x,y
    if zone ==6:
        temp = x
        x = y
        y = -temp
        return x,y
    if zone ==7:
        y = -y
        return x,y



InitalZone = findzone(-10, -20, -20, 70 )
# InitalZone2 = findzone(-5, 100, 20, 135 )
# InitalZone3 = findzone(11, 9, 34, -9 )

# print (InitalZone, InitalZone2, InitalZone3 )

NewCord1 = findXY(-10, -20, InitalZone)
NewCord2 = findXY(-20, 70, InitalZone)
NewCoord1 = list(NewCord1)
NewCoord2 = list(NewCord2)

NewDelX = NewCoord2[0] - NewCoord1 [0]
NewDelY = NewCoord2[1] - NewCoord1 [1]
d = 2*NewDelY - NewDelX
# print(NewCoord1[0], NewCoord1[1], d,)

# init = findInitialZone(NewCoord1[0], NewCoord1[1], InitalZone)
# print (init)

while NewCoord1[0] !=  NewCoord2 [0]:
        
    if d <=0:
        EastIncrement = 2*NewDelY
        d = d + EastIncrement
        NewCoord1[0] += 1
        # print(NewCoord1[0], NewCoord1[1], d, "E")
        
    if d>0:
        NortEastIncrement = 2*NewDelY - 2*NewDelX
        d = d + NortEastIncrement
        NewCoord1[0] += 1
        NewCoord1[1] += 1
        # print(NewCoord1[0], NewCoord1[1], d, "NE")
        
    init = findInitialZone(NewCoord1[0], NewCoord1[1], InitalZone)
    presentation = coord (init[0], init[1])
    print (presentation)     
    





        
        

