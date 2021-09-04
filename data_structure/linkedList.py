


class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None


class linked_list:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert(self,value,location):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node

        else:
            if location==0:
                new_node.next=self.head
                self.head=new_node
            elif location==1:
                new_node.next=None
                self.tail.next=new_node
                self.tail=new_node

            else:
                temp=self.head
                index=0
                while index< location - 1:
                    temp=temp.next
                    index+=1
                next_node=temp.next
                temp.next=new_node
                new_node.next=next_node
                if temp==self.tail:
                    self.tail=new_node
                




if __name__=="__main__":
   linked=linked_list()
   print(linked.insert(4,1))
   
   




 
            

       
     
