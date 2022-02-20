class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beg(self,data):
        node= Node(data,self.head)
        self.head = node
        
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
        
    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    def print(self):
        if self.head is None:
            print("LinkedList is blank")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr = llstr + "-->" + str(itr.data)
            itr = itr.next
        print(llstr)
    def get_length(self):
        count =0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("invalid index")
        if index ==0:
            self.head = self.head.next
            return
        count =0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count = count +1
    def insert_at(self,index,data):
        if index<0 or index>=self.get_length():
            raise Exception("invalid index")
        if index ==0:
            self.insert_at_beg(data)
            return
        count =0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count = count+1
        return
    def remove_by_value(self,data):
        itr = self.head
        count =0
        while itr.next:
            if (itr.next).data == data:
                count =1
                itr.next = itr.next.next
                return
            itr = itr.next
        print("Value is not available in the LinkedList")     
         
            


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["mango","black grapes","pineapple"])
    ll.insert_at_end(20)
    ll.insert_at_beg(5)
    ll.insert_at_beg(10)
    ll.insert_at_end(340)
    #ll.print()
    ll.insert_at(2,"apple")
    ll.print()
    ll.remove_at(2)
    ll.print()
    ll.remove_by_value("apple")
    ll.print()
    ll.remove_by_value("mango")
    ll.print()
    #print(ll.get_length())
