#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#                                   Question Number 1

# Calculate  the  sum  of  each  column  in  the  given  8x3  matrix,
# find  the  difference  between  each  pair  of  column  sums,
# and  store  the  differences  in  a  new  array.

#     Input:                 Output:          
                                           
                                           
#     matrix = [             [ 30  17 167]            Sum of four col = [234 264 281 448]
#     [46, 74, 10, 29]                         
#     [78, 58, 39, 88]                                Now the diff 264 - 234 = 30
#     [13, 94, 44, 45]                                             281 - 264 = 17
#     [99, 19, 68, 18]                                             448 - 281 = 167
#     [9, 6, 52, 97]
#     [43, 83, 13, 78]
#     ]


# In[7]:


import numpy as np

def findDiff(matrix):
    
    lengthCol=len(matrix[0])
    lengthRow=len(matrix)
    sumAry=np.array([0]*lengthCol)
    finalArry=np.array([0]*(lengthCol-1))
    sum1=0
    index=0
    
    for i in range (lengthCol):
        for y in range (lengthRow):
            sum1+=matrix[y][i]
        sumAry[index]=sum1
        index+=1
        sum1=0
        
    index=0
    for z in range (1,len(sumAry)):
        finalArry[index]=(sumAry[z]-sumAry[z-1])
        index+=1
    
    return finalArry


matrix = [
    [25, 13, 47, 62],
    [81, 38, 52, 96],
    [17, 64, 33, 75],
    [42, 55, 29, 88],
    [19, 73, 36, 68],
    [50, 21, 84, 59]
]

result = findDiff(matrix)
print(result)


# In[ ]:


#                                   Question Number 2

# Given  a  singly  linked  list  'head'  and  a  target  value,
# check  if  there  exists  a  pair  of  nodes  in  the  list  whose
# values  sum  up  to  the  target.  Return  True  if  such  a  pair  exists,
# otherwise  return  False.  If  the  list  has  only  one  node,  return  False.

#            INPUT:                    OUTPUT:
    
#     2-->4-->6-->8-->3-->5            True                Here two pair (6,5) and (8,3) are sum 
#                                                          of 11 finding any one pair is enough
#     11                                                   and return True


# In[5]:


# =================================================================================================
# NOTE:  Take into account the class node that has already been created for the student.
# =================================================================================================
import numpy as np
class Node:
    def __init__(self,elem,next = None):
        self.elem,self.next = elem,next

def createList(arr):
    head = Node(arr[0])
    tail = head
    for i in range(1,len(arr)):
        newNode = Node(arr[i])
        tail.next = newNode
        tail = newNode
    return head

def printLinkedList(head):
    temp = head
    while temp != None:
        if temp.next != None:
            print(temp.elem, end = '-->')
        else:
            print(temp.elem)
        temp = temp.next
    print()

# =================================================================================================
# NOTE:  Take into account the class node that has already been created for the student.
# ==================================================================================================


def findTheMatch(head,target):
    if head.next==None:
        return False
    else:
        temp=head
        temp2=head.next
        
    while temp.next!=None:
        while temp2!=None:
            if target==(temp.elem+temp2.elem):
                return True
            temp2=temp2.next
        temp=temp.next
        temp2=temp.next
    return False
    
    
    
    
    
#==============TEST ONE==================
print("==============TEST ONE==================")
Node1=createList(np.array([2,4,6,8,3,5]))
print("Given List:")
printLinkedList(Node1)
result=findTheMatch(Node1,11)
print("Result:",result)
print()
#==============TEST TWO==================
print("==============TEST TWO==================")
Node2=createList(np.array([11]))
print("Given List:")
printLinkedList(Node2)
result=findTheMatch(Node2,11)
print("Result:",result)
print()
#==============TEST THREE==================
print("==============TEST THREE==================")
Node3=createList(np.array([2,4,6,8,3,5]))
print("Given List:")
printLinkedList(Node3)
result=findTheMatch(Node3,1)
print("Result:",result)


# In[ ]:


#                                   Question Number 3
# Consider the following Python code snippet, which defines classes Node, Stack, and Queue, 
# along with a function checkPair(st). The checkPair function takes a stack st as input and 
# checks for pairs of male and female elements in the stack. If a pair is found, it prints 
# the pair. If not, it enqueues the unmatched elements until a matching pair is found. 
# Study the code carefully and answer the following questions:


# In[19]:


# =================================================================================================
# NOTE:Take into account the class Stack and Queue that has already been created for the student.
# =================================================================================================
class Node:
    def __init__(self,elem=None,next=None):
        self.elem = elem
        self.next = next

class Stack:
    def __init__(self):
        self.__top = None

    def push(self,elem):
        nn = Node(elem,self.__top)
        self.__top = nn

    def pop(self):
        if self.__top == None:
            #print('Stack Underflow')
            return None
        e = self.__top
        self.__top = self.__top.next
        return e.elem

    def peek(self):
        if self.__top == None:
          #print('Stack Underflow')
            return None
        return self.__top.elem

    def isEmpty(self):
        if self.__top == None:
            return True
        else:
            return False
        
class Queue:
    def __init__(self):
        self.__queue=[]
        self.__rare=-1
        self.__front=0
    def isEmpty(self):
        if self.__rare>-1:
            return True
        else:
            return False
    def Enqueue(self,data):
        self.__queue.append(data)
        self.__rare+=1
    def Dequeue(self):
        keep=self.__queue[self.__front]
        if self.isEmpty():
            self.__queue.pop(self.__front)
            self.__rare-=1
            return keep
        else:
            return
    def printQueue(self):
        if self.isEmpty():
             for i in range ((self.__rare),-1,-1):
                if i==0:
                    print(self.__queue[i],end="")
                else:
                    print(self.__queue[i],end=",")
        else:
            return
# =================================================================================================
# NOTE:Take into account the class Stack and Queue that has already been created for the student.
# =================================================================================================
def checkPair(st):
    
    q=Queue()
    temp=""
    temp2=""
    
    while st.isEmpty()!=True:
        temp=st.pop()
        temp2=st.pop()
        if (temp[0]=="M" and temp2[0]=="F") or (temp[0]=="F" and temp2[0]=="M"):
            print(temp[2:]+ " and "+temp2[2:]+" are a pair")
            temp=""
            temp2=""
        else:
            if temp[0]=="M":
                if q.isEmpty()==True:
                    temp2=q.Dequeue()
                    print(temp[2:]+ " and "+temp2[2:]+" are a pair")
                    temp=""
                    st.push(temp2)
                    temp2=""
                else:
                    temp=""
                    st.push(temp2)
                    temp2=""
            else:
                q.Enqueue(temp)
                temp=""
                st.push(temp2)
                temp2=""



st = Stack()
st.push("M_52")
st.push("F_62")
st.push("F_82")
st.push("M_42")
st.push("M_12")
st.push("F_22")
st.push("F_31")
st.push("F_21")
st.push("M_22")
checkPair(st)

