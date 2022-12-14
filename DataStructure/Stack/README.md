![](https://velog.velcdn.com/images/chan9708/post/49ed90b9-4631-4653-b171-e378b5ba7e98/image.png)


# 스택

## LIFO
* **Last-In-First-Out**
* 즉, 후입선출
* 가장 뒤에 들어온 것이 가장 먼저 나가는 구조

## 개념과 원리

![](https://velog.velcdn.com/images/chan9708/post/1d4ef93e-aefd-4f36-b129-579414e1bc2a/image.png)

* `맨 위의 원소`만 접근 가능하다.
  * 맨 위의 원소 - `Top`
  * 새 원소를 삽입할 때 스택 탑 바로 윗자리에 원소를 저장하고 새 원소가 새로운 스택 탑이 되도록 한다.
  * 원소를 삭제할 때 무조건 탑에 있는 원소를 삭제한 후 바로 아래 원소가 새 스택 탑이 되도록 한다.

* 함수 호출 시 스택 사용

![](https://velog.velcdn.com/images/chan9708/post/a0b2439d-680f-409f-94db-4f29e313945b/image.png)
![](https://velog.velcdn.com/images/chan9708/post/a4bd330d-2c93-442b-92cf-b00e1c23525b/image.png)

  * 스택의 맨 위에는 현재 수행 중인 함수 정보가 저장되고, 이 함수를 호출한 함수는 바로 아랫 공간에 저장되어 있다.
  * 수행을 마친 함수가 스택 영역에서 지워지면 원래 함수로 돌아와 다시 시작할 수 있도록 호출했던 함수의 정보가 스택의 맨 위에 있게 됩니다.
  
## 추상 데이터 타입
>
* **맨 윗부분에 원소를 추가한다.**
* **맨 윗부분에 있는 원소를 알려준다.**
* **맨 윗부분에 있는 원소를 삭제하면서 알려준다.**
* **스택이 비어 있는지 확인한다.**
* **스택을 깨끗이 비운다.**

## 스택 구조
>
* **`__stack[]`** 🠔 **스택의 원소들이 저장되는 리스트** 

* **`push(x)`** 🠔 **맨 윗부분에 원소를 추가한다.**
* **`pop()`** 🠔 **맨 윗부분에 있는 원소를 알려준다.**
* **`top()`** 🠔 **맨 윗부분에 있는 원소를 삭제하면서 알려준다.**
* **`isEmpty()`** 🠔 **스택이 비어 있는지 확인한다.**
* **`popAll()`** 🠔 **스택을 깨끗이 비운다.**

