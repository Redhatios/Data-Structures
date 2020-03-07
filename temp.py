class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        #self.temp = None
        
class linkedlist:
    def __init__(self):
        self.head = None
        #self.temp = None
        
    def insert(self,element,temp=None):
        if(self.head==None):
            self.head = node(element)
        else:
            if(temp==None):
                temp = self.head
            while(temp.next is None):
                #y = node(element)
                temp.next = node(element)
                temp = temp.next
                break
        return temp
        
    def printList(self): 
        temp = self.head 
        while (temp): 
            print(temp.data,end=" ") 
            temp = temp.next
        
    def deletefirst(self):
        temp = self.head.next
        self.head = self.head.next 
            
    def deletelast(self,x):
        temp = self.head
        while(temp.next!=None):
            y = temp
            temp = temp.next
            
        y.next = None
        x = y
        return x
        
    def deletemiddle(self,position):
        dcount = 0
        
        temp =self.head
        while(temp):
            
            dcount-=-1
            if(dcount==position-1):
                tempf = temp 
            if(dcount==position+1):
                temph = temp
                tempf.next = temph
                break
            temp =temp.next
    def reverse(self):
        temp = self.head
        while(temp):
            if(newnode.head==None):
               x = temp.data
               newnode.head = node(x)
            else:
                tempy = newnode.head
                x = temp.data
                newnode.head = node(x)
                newnode.head.next = tempy
            temp=temp.next  
        return newnode    
                
    def splitreverse(self,key):
        dcount =0
        temp = self.head
        while(temp):
            dcount -=-1
            if(dcount != key):
                if(newnode.head==None):
                   x = temp.data
                   newnode.head = node(x)
                else:
                    tempy = newnode.head
                    x = temp.data
                    newnode.head = node(x)
                    newnode.head.next = tempy
                
            else:
                    tempy = temp
                    x = temp.data
                    newnode.temp = node(x)
                    newnode.temp.next = tempy
                    
            temp=temp.next      
        return newnode    
        
        
        
if __name__ == "__main__":
    llist = linkedlist()
    #DRIVER FUNCTION
    condition =True
    while(condition == True):
        print("\n1.Insert\n2.Delete\n3.Print\n4.Exit\n5.Reverse")
        option = int(input())
        if(option ==1):
            element = int(input())
            if(llist.head==None):
                x = llist.insert(element,temp =None)
            else:
                x=llist.insert(element,x)
        elif(option ==2):
            print("\n1.Delete First\n2.Delete Middle\n3.Delete Last")
            op = int(input())
            #elementd = int(input())
            if(op == 1):
                llist.deletefirst()
            elif(op==2):
                position = int(input())
                llist.deletemiddle(position)
            elif(op==3):
                x = llist.deletelast(x)
        elif(option == 3):
            #continue
            llist.printList()
        elif(option == 4):
            condition = False
        elif(option == 5):
            newnode = linkedlist()
            x = llist.reverse()
            newnode.printList()
        elif(option==6):
            newnode = linkedlist()
            key = int(input())
            x = llist.splitreverse(key)
            newnode.printList()
