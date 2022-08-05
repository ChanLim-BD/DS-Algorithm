from listStack import *

def parenBalance(s:str) -> bool:
    st = ListStack()

    line = s
    
    for l in line:
        if l == '(':
            st.push(l)
        elif l == ')':
            if st.isEmpty():
                return False
            st.pop()
        else:
            continue


    if st.isEmpty():
        return True
    else:
        return False

if __name__ == "__main__":
    s = input("input s: ")
    print(parenBalance(s))