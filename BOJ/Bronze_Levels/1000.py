a, b = map(int, input().split())
c = a + b
print(c)


"""
원리는 input에서 받은 값을 split()에서 공백을 기준으로 나누어 리스트에 값을

나누어서 반환하여 ['3', '5'] 처럼 자료가 들어있게되고,

 

map 함수에서 위 리스트에 int 자료형으로 바꾸는 함수를 mapping하면

정수형 3과 5의 값이 두 개의 값에 들어간 결과가 반환되게 됩니다.

 

만일 공백이 아니라 쉼표 등 다른 문자로 나누고 싶다면 split(',') 처럼

split 함수에 해당하는 부분을 바꿔주시면 됩니다.
"""