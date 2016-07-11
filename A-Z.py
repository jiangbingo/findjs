
def getKey(index):
    colCode = ""
    key='A'
    loop = int(index/26)
    if loop>0 :
        colCode += getKey(loop-1)

    key =key+index%26
    colCode += key

index = 'sss'
getKey(index)