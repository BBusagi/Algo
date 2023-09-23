class MyCircularQueue:

    def __init__(self, k: int):
        self.size=k
        self.q=[0]*k
        self.front=-1
        self.rear=-1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front=self.rear=0
        else:
            self.rear=(self.rear+1)%self.size #To maintain the cyclic nature of the queue
        self.q[self.rear]=value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        item=self.q[self.front]
        if self.front==self.rear: #if there is only one element in the queue
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.size #To maintain the cyclic nature of the queue
        return True

    def Front(self) -> int:
        if self.front==-1:
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.rear==-1:
            return -1
        return self.q[self.rear]

    def isEmpty(self) -> bool:
        return self.front==-1

    def isFull(self) -> bool:
        if self.front==0 and self.rear==self.size-1: #if we don't write this condition then also second condition will manage everything
            return True
        if self.rear==(self.front-1)%(self.size):
            return True
        return False