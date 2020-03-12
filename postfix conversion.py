class stackNode:
    def __init__(self,data):
        self.data = data
        self.next = None
class stack:
    def __init__(self):
        self.top = None
        self.operator = ['+','-','*','^','/']
        self.priority = {'/':3,'+':2,'-':1,'*':4,'^':5}
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
        
    def priorityfunc(self,char,temp):
        if(self.priority[char] <= self.priority[temp]):
            if(self.priority[char] < self.priority[temp]):
                print(self.top.data,end=" ")
                obj.pop()
                obj.push(char)
            elif(self.priority[char] == self.priority[temp]):
                print(char,end=" ")
                obj.pop()
                obj.push(char)
        else:
            obj.push(char)
            

    def evaluate(self,exp):
        for char in exp:
            if(char in self.operator):
                if(self.top==None):
                    obj.push(char)
                else:
                    value = self.top.data
                    #Down Oper
                    if(value in self.operator):
                        if(self.priority[char] <= self.priority[value]):
                            if(self.priority[char] < self.priority[value]):
                                print(self.top.data,end=" ")
                                obj.pop()
                                if(self.top!=None):
                                     while(True):
                                          if(self.top==None):
                                               break
                                          elif(self.priority[char] < self.priority[self.top.data]):
                                               print(self.top.data,end=" ")
                                               obj.pop()
                                          else:
                                               break
               
                                obj.push(char)
                            elif(self.priority[char] == self.priority[value]):
                                print(char,end=" ")
                                continue
                        else:
                            obj.push(char)
                    else:
                        print(self.top.data,end=" ")
                        obj.pop()
                        if(char not in self.operator):
                            obj.push(char)
                        else:
                            if(self.top==None):
                                obj.push(char)
                            else:
                                if self.top.data in self.operator:
                                    temp= self.top.data
                                    obj.priorityfunc(char,temp)
                                else:
                                    obj.push(char)
                                
            elif(char == '('):
                obj.push(char)
            elif(char.isalpha() or char.isdigit()):
                obj.push(char)
            elif(char == ')'):
                tempx = self.top
                while(tempx.data !='('):
                    print(tempx.data,end=" ")
                    obj.pop()
                    tempx = tempx.next
                obj.pop()
                tempx=None
        if(obj.isempty()!=True):
            tempx = self.top
            while(tempx):
                print(tempx.data,end=" ")
                obj.pop()
                tempx = tempx.next
            
        
            



if __name__ == '__main__':
    exp = '(a+b)*c-(d-e)*(f+g)'
    obj = stack()
    obj.evaluate(exp)
    
