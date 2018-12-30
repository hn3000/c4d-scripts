

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
            sum = sum + p.x
            found = found + 1

    newx = sum / found

    for index, selected in enumerate(bs.GetAll(maxEl)):
        if not selected: continue
            
        else:
            p = obj.GetPoint(index)
            obj.SetPoint(index, c4d.Vector(newx, p.y, p.z))




