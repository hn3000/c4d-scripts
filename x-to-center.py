import c4d

def main():
    obj = doc.GetActiveObject()

    doc.StartUndo()
    sum = 0
    found = 0

    bs = obj.GetPointS()
    maxEl = obj.GetPointCount()

    for index, selected in enumerate(bs.GetAll(maxEl)):
        if not selected: continue
        else:
            p = obj.GetPoint(index)
            sum = sum + p.x
            found = found + 1

    newx = sum / found

    doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)

    for index, selected in enumerate(bs.GetAll(maxEl)):
        if not selected: continue
        else:
            p = obj.GetPoint(index)
            obj.SetPoint(index, c4d.Vector(newx, p.y, p.z))

    obj.Message(c4d.MSG_UPDATE)

    doc.EndUndo()
    c4d.EventAdd()

if __name__=='__main__':
    main()
