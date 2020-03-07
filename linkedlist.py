class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        #self.temp = None
        
class linkedlist:
    def __init__(self):
        self.head = None
        #self.temp = None
if __name__ == "__main__":
    llist = linkedlist()
    def insert(element,llist,temp):
        if(llist.head==None):
            llist.head = node(element)
            temp = llist.head
            print(llist.head)
        else:
            #llist.temp = node(element)
            #llist.temp = node(element)
            #tempo = node(element)
            #temp = tempo
                
            while(temp.next==None):
                temp.next = node(element)
                temp = temp.next
                break
        return temp
    condition =True
    while(condition == True):
        print("1.Insert\n2.Delete\n3.Print\n4.Exit")
        option = int(input())
        if(option ==1):
            element = int(input())
            if(llist.head==None):
                #llist.head = node(element)
                x=insert(element,llist,temp=None)
            else:
                x = insert(element,llist,x)
        if(option ==2):
            element = int(input())
            delete(element)
        elif(option == 3):
            printlist()
        elif(option == 4):
            condition = False
        
