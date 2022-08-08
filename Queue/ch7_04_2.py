from linkedQueue import LinkedQueue

class TwoQueueStack:
    def __init__(self):
        self.__q = LinkedQueue()
        self.__tq = LinkedQueue()

    def __move_elements(self, q, tq):
        while not q.isEmpty():
            tq.enqueue(q.dequeue())

    def __cmp_elements(self, q, tq):
        while q.front() < tq.front():
            tq.enqueue(q.dequeue())
            q.enqueue(tq.dequeue())
         
    def push(self, x):
        # self.__move_elements(self.__q, self.__tq)
        self.__q.enqueue(x)
        # self.__move_elements(self.__tq, self.__q)

    def pop(self):
        self.__move_elements(self.__q, self.__tq)
        self.__q.enqueue(self.__tq.dequeue())

        if not self.__tq.isEmpty():
            self.__cmp_elements(self.__q, self.__tq)

        return self.__q.dequeue()


if __name__ == "__main__":
    st = TwoQueueStack()
    st.push(1)
    st.push(2)
    st.push(3)
    print(st.pop())
    print(st.pop())
    print(st.pop())
        