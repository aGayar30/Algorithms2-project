from math import ceil, floor
from mimetypes import init
from tempfile import tempdir


class pyramid:
    rowlist=[]
    rowlist2 =[]
    manipulatedrows=[]
    def __init__(self,total_rows):
        self.total_rows = total_rows
        for i in range(1,total_rows+1):
            self.rowlist.append(rows(i,total_rows))
        for i in range(1,total_rows):
            self.rowlist2.append(rows(i,total_rows))

    
    def no_of_iterations(self):
        coins_number = 0
        for i in range(1,(self.total_rows+1)):
            coins_number = coins_number+i
        iterations = int (floor(coins_number/3))
        return iterations
        """print("number of iterartions are: ")
        print(iterations)"""
    
    def showPyramid(self):
        temparr=[]
        for row in self.rowlist:
            for i in range(row.spaces):
                temparr.append("")    
                
            for i in range(row.no_of_coins) :
                temparr.append("1")    
            for i in range(row.spaces):
                temparr.append("") 
            for i in temparr:       
                 print(i, end =" ")
            print("\n")     
            temparr.clear()  

    def getmanipulated(self):
        self.manipulatedrows.append(self.rowlist[0])
        if (len(self.rowlist)%2 == 0):
            max=int((len(self.rowlist)/2)+1)
            for i in range(max,len(self.rowlist)):
                self.manipulatedrows.append(self.rowlist[i])
        else:
            self.manipulatedrows.append(self.rowlist[0])
            max= floor(int((len(self.rowlist)/2)+1))
            for i in range(max,len(self.rowlist)):
                self.manipulatedrows.append(self.rowlist[i]) 

    def updaterowlist(self):
        index = self.total_rows - 2
        s = 1 
        for k in range (len(self.rowlist2)):  
            
            for i in range (len(self.rowlist)-s):
                self.rowlist[i].removecoins(1)
            #self.showPyramid()   
            firstrow=self.rowlist2[index]
            self.rowlist.append(firstrow)
            self.showPyramid()
            index = index - 1
            s = s + 1
            


class rows:
     # init method or constructor   
    def __init__(self,no_of_coins,totalrows):  
        self.no_of_coins = no_of_coins
        self.spaces = totalrows - no_of_coins
        self.totalrows=totalrows
    def addcoins(self,addcoins):
        self.no_of_coins=self.no_of_coins+addcoins
        self.updatespaces()
    def removecoins(self,removeCoins):
        self.no_of_coins=self.no_of_coins-removeCoins
        self.updatespaces()
    def updatespaces(self):
        self.spaces=self.totalrows-self.no_of_coins




if __name__=="__main__":
    no_of_rows = int (input("Enter number of rows: "))
    mypyramid = pyramid(no_of_rows)
    mypyramid.showPyramid()
    mypyramid.getmanipulated()
    mypyramid.updaterowlist()
    print ('\n')
    print ("Final Result")
    mypyramid.showPyramid()
