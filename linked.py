class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList():
    def __init__(self):
        self.head=None

    def append(self,data):
        a=Node(data)
        temp=self.head
        if(self.head==None):
            self.head=a
        else:
            while(temp.next!=None):
                temp=temp.next
            temp.next=a
    def print(self):
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next
    def delete_particular(self,node):
        try:
            while(node.next!=None):
                node.data=node.next.data
                if(node.next.next==None):
                    node.next=None
                else:
                    node=node.next
        except:
            print("Error")

    def find_particular(self,n):
        temp=self.head
        while(n!=1):
            temp=temp.next
            n=n-1
        LinkedList.delete_particular(self,temp)
a=(int(input("")))
b=LinkedList()
for i in range(a):
    c=(int(input("")))
    b.append(c)
b.find_particular(3)
b.print()