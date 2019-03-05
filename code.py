import math
class Node:
    def __init__(self, d):
        self.data = d
        self.prv = None
        self.nxt = None

    # Endurkvæmt fall sem bætir aftast á listann.
    def append(self,d):
        if self.nxt:
            return self.nxt.append(d)
        else:
            curr = Node(d)
            self.nxt = curr
            curr.prv = self
            return True

    # Endurkvæmt fall sem og prentar listann.
    def printList(self):
        #Þinn kóði hér
        print(self.data)
        if self.nxt:
            self.nxt.printList()
        else:
            return True
    # Endurkvæmt fall sem og prentar listann frá Head til enda
    def find(self, d):
        # Þinn kóði hér
        if self.data == d:
            return True
        elif self.nxt:
            return self.nxt.find(d)
        else:
            return False
    # Endurkvæmt fall sem eyðir ákveðnum hnút úr lista
    def delete(self, d):
        # Þinn kóði hér
        if self.data == d:
            if self.nxt:
                self.prv.nxt = self.nxt
                self.nxt.prv = self.prv
                return True
            else:
                self.prv.nxt = None
                return True
        elif self.nxt:
            return self.nxt.delete(d)
        else:
            return False
class DLL: # DLL = Dobule Linked List
    def __init__(self):
        self.head = None

    # Bætir við fremst á listann, hnúturinn verður Head -> förum ekki í Node klasann.  Þú úrfærir fallið í þessum klasa
    def push(self,d):
        # Þinn kóði hér
        if self.head:
            curr = Node(d)
            self.head.prv = curr
            curr.nxt = self.head
            self.head = curr
            return True
        else:
            self.head = Node(d)
            return True

    # Bætir við aftast á listann -> kallar á endurkvæmnt fall í Node.  Fallið er þegar útfært í Node klasa
    def append(self, d):
        if self.head:
            return self.head.append(d)
        else:
            self.head = Node(d)
            return True

    # Prentar listann allan á skjá -> kallar á endurkvæmt fall í Node, þú útfærir printList í Node.  Notaðu endurkvæmni.
    def printList(self):
        if self.head:
            self.head.printList()
        else:
            print("Empty list!")

    # Kallar á endurkvæmt fall í Node klasanum, finnur ákveðinn hnút.  Þú útfærir fallið find í Node klasanum.  Notaðu endurkvæmni.
    def find(self, d):
        if self.head:
            return self.head.find(d)
        else:
            return False

    # Kallar á endurkvæmt fall í Node klasanum, finnur ákveðinn hnút og eyðir.  Þú útfærir fallið delete í Node klasanum.  Notaðu endurkvæmni.
    def delete(self, d):
        if self.head is None:
            return -1
        elif self.head.data == d:
            if self.head.nxt:
                self.head = self.head.nxt
                self.head.prv.nxt = None
                self.head.prv = None
                return True
            else:
                self.head = None
                return False
        else:
            return self.head.delete(d)

dbl = DLL()
dbl.append(5)           # 5
dbl.append(7)           # 5 7
dbl.push(1)             # 1 5 7
dbl.push(0)             # 0 1 5 7
dbl.append(10)          # 0 1 5 7 10
dbl.printList()
print()
print(dbl.delete(10))   # 0 1 5 7
dbl.printList()
print(dbl.find(5))      # True
print(dbl.find(6))     # False



class Vigur:

    # Smiður frumstillir x og y hnit vigurs eftir parametrum
    def __init__(self,x,y):
        # Þinn kóði hér
        self.x = x
        self.y = y

    # Fall sem skrifar hnit vigurs á skjá
    def prenta(self):
        # Þinn kóði hér
        print("x: "+ str(self.x) +" y: " + str(self.y))
    # Fall sem skilar lengd
    def lengd(self):
        # Þinn kóði hér
        return math.sqrt(self.x**2+self.y**2)

    # Fall sem skilar hallatölu
    def halli(self):
        # Þinn kóði hér
        return self.y/self.x

    # Fall sem skilar þvervigri
    def tvervigur(self):
        # Þinn kóði hér
        return Vigur(self.y*-1,self.x)

    # Fall sem skilar stefnuhorni
    def stefnuhorn(self):
        # Þinn kóði hér
        if self.x > 0:
            return math.degrees(math.atan(self.x/self.y))
        else:
            if self.y>0:
                return 180-abs(math.degrees(math.atan(self.x/self.y)))
            else:
                return (180-abs(math.degrees(math.atan(self.x/self.y))))*-1

    # Fall sem tekur vigur sem parameter og skilar horni milli vigra
    def horn(self,v):
        # Þinn kóði hér
        lengd1 = self.lengd()
        lengd2 = v.lengd()
        innfeldi = (self.x*v.x)+(self.y*v.y)
        return abs(math.degrees(math.acos(innfeldi/(lengd1*lengd2))))

    # Fall sem tekur vigur sem parameter og skilar summu vigri
    def summa(self,v):
        return Vigur(self.x+v.x,self.y+v.y)
# Keyrsluforrit
print("!!!!!!!!!!VIGUR!!!!!!!!!!")
v1 = Vigur(1,3)
v1.prenta()
print("Lengd: ", v1.lengd())
print("Halli: ", v1.halli())
vt = v1.tvervigur()
print("Þvervigur: " , end=" ")
vt.prenta()
print("Stefnuhorn: ", v1.stefnuhorn())
v2 = Vigur(-3,1)
print("Horn milli vigra: " , v2.horn(v1))
v3 = v1.summa(v2)
print("Summa: " , end=" ")
v3.prenta()
