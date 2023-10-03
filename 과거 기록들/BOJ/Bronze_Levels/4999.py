import sys

sp = sys.stdin.readline()
st = sys.stdin.readline()

if sp.count('a') >= st.count('a'):
    print('go')
else:
    print('no')
