class stackNode:
    def __init__(self,data):
        self.data = data
        self.next = None
class stack:
    def __init__(self):
        self.top = None
        self.brackets = {'}':'{',')':'(',']':'['}
    def push(self,data):
        newnode = stackNode(data)
        newnode.next = self.top
        self.top = newnode
    def pop(self):
        if(self.top.next !=None):
            self.top = self.top.next
        else:
            self.top = None
    def isempty(self):
        if(self.top==None):
            return True
    def check(self,x):
        for i in x:
            if x[0] in self.brackets.values() :
                if i in self.brackets.values():
                    obj.push(i)
                elif(self.top.data == self.brackets[i]):
                    obj.pop()
                else:
                    print('Not Balanced')
            else:
                obj.push()
                print('Not Balanced')
        if(isempty()):
            print("Balanced")
if __name__ == '__main__':
    obj = stack()
    x= input()
    obj.check(x)
        
