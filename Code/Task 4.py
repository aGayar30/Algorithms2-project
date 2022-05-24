def donecheck(boxes):
    doneFlag= False
    for x in boxes:
        if x > 1 :
            doneFlag=True
            break
    return doneFlag


def maintask(boxes:list):
    index=0
    loop=True
    while (loop == True):
        if (boxes[index]>1):
            if (boxes[index]%2==0 ):
                boxes.append(0)
                boxes[index+1]=boxes[index]//2
                boxes[index]=0
                index=index+1
                loop = donecheck(boxes)
                print(boxes)
                continue
            elif (boxes[index]%2 != 0 ):
                boxes.append(0)
                boxes[index+1]=boxes[index]//2
                boxes[index]=1
                index=index+1
                loop = donecheck(boxes)
                print(boxes)
                continue


boxes = []
print("Enter Number of Pennies:")
n = input()
boxes.append(int(n))
print(boxes)
maintask(boxes)
