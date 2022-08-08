import sys
sys.path.insert(0, 'C:/Study/code/4-1/DataStructure/ch6')

from linkedStack import LinkedStack

class TwoStackQueue:
    def __init__(self):
        self.__s = LinkedStack()
        self.__ts = LinkedStack()

    def __move_elements(self, s, ts):
        while not s.isEmpty():
            ts.push(s.pop())
         
    def enqueue(self, x):
        self.__s.push(x)

    def dequeue(self):
        self.__move_elements(self.__s, self.__ts)
        self.__s.push(self.__ts.pop())

        return self.__s.pop()


if __name__ == "__main__":
    st = TwoStackQueue()
    st.enqueue(1)
    st.enqueue(2)
    st.enqueue(3)
    print(st.dequeue())
    print(st.dequeue())
    print(st.dequeue())
        