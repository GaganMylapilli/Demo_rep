class node:
    def __init__(self,data):
        self.value=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.headnode=None
    def iterate(self):
        pointer =self.headnode
        while pointer:
            print(str(pointer.value)+"->",end="")
            pointer=pointer.next
        print("None")
        return 
demo_lnkd_list=linkedlist()
demo_lnkd_list.headnode=node(1)
node2=node(2)
node3=node(3)
demo_lnkd_list.headnode.next=node2
node2.next=node3
demo_lnkd_list.iterate()
print("test for pull through git bash")