

import c4d

def main():
    
    obj = doc.GetActiveObject()

    sum = 0
    found = 0

    maxEl = obj.getPointCount()
    bs = obj.GetPointS()

    for index, selected in enumerate(bs.GetAll(maxEl)):
        if not selected: continue
            
        else:
            p = obj.GetPoint(index)
            sum = sum + p.y
            found = found + 1

    newy = sum / found

    for index, selected in enumerate(bs.GetAll(maxEl)):
        if not selected: continue
            
        else:
            p = obj.GetPoint(index)
            obj.SetPoint(index, c4d.Vector(p.x, newy, p.z))


    obj.Message(c4d.MSG_UPDATE)

    c4d.EventAdd()

