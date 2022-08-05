from linkedStack import *

def test1() -> bool:
    st2 = LinkedStack()
    ls1 = []

    ch = input("input ch: ")
    if '$' in ch:
        ch2 = ch.split('$')
    else:
        exit()

    ls2 = list(ch2[0])

    for x in ch2[1]:
        st2.push(x)

    for x in ch2[1]:
        ls1.append(st2.pop())

    if ls1 == ls2:
        return print(True)
    else:
        return print(False)

if __name__ == "__main__":
    test1()
    
