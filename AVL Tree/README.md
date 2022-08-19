![](https://velog.velcdn.com/images/chan9708/post/ce54b6c0-6d41-47ae-b698-5701f1fd4be4/image.jpg)

# 이어서

>

- [이진 검색 트리](https://velog.io/@chan9708/%EC%9D%B4%EC%A7%84-%EA%B2%80%EC%83%89-%ED%8A%B8%EB%A6%AC)는 검색과 삽입, 삭제에 평균 `Θ(logn)` 시간이 소요되지만 운이 나쁘면 트리 모양이 균형을 이루지 못합니다.
- 균형이 많이 깨지면 다음과 같은 트리가 나타납니다.
  ![](https://velog.velcdn.com/images/chan9708/post/1b97b057-506f-4ed2-b5d6-a2007e63899c/image.png)
  - 이와 같은 경우는 검색과 삽입, 삭제에 평균 `Θ(n)` 시간이 소요됩니다.

# 균형 검색 트리

- <span style="font-size: 25px">**`균형 검색 트리`**</span>는 `최악의 경우`에도 이진 트리의 균형이 맞도록 유지해서 작업들이 항상 `O(logn)` 시간을 보장합니다.
- `이진 검색 트리`에서는 분기할 때 최대 2개로 제한되는데 이보다 더 많이 분기할 수 있는 트리들도 있다. **🠔 다진 검색 트리**
  - **`다진 검색 트리`**에서는 `균형`이 더 중요하다.

---

## AVL 트리

![](https://velog.velcdn.com/images/chan9708/post/48578f5e-17eb-48e2-a920-39ee19aa52f4/image.png)

- **`AVL 트리`**
  - Adelson-Velskii와 Landis 두 사람이 고안한 트리
  - 이진 검색 트리가 항상 균형을 유지하도록 운영하는 예시
  - <span style="background-color: yellow">**AVL 트리는 트리 내의 어떤 노드도 좌서브 트리와 우서브 트리의 높이 차가 1보다 크지 않은 상태로 유지되는 이진 검색 트리**</span>이다.

---

### 균형이 깨진 AVL 트리의 수선

- **AVL 트리의 균형이 깨지면 즉시 수선 과정에 들어간다.**
- 수선 시, 다음과 같은 회전 알고리즘을 통해 수선한다.

>

```python
좌회전(t): 🠔 t: 회전의 중심 노드
	RChild 🠔 t.right
    RLChild 🠔 RChild.left
    RChild.left 🠔 t
    t.right 🠔 RLChild
    t.height 🠔 max(t.right.height, t.left.height) + 1
    RChild.height 🠔 max(RChild.right.height, RChild.left.height) + 1
```

>

```python
우회전(t): 🠔 t: 회전의 중심 노드
	LChild 🠔 t.left
    LRChild 🠔 LChild.left
    LChild.left 🠔 t
    t.left 🠔 LRChild
    t.height 🠔 max(t.left.height, t.right.height) + 1
    LChild.height 🠔 max(LChild.right.height, LChild.left.height) + 1
```

> EX) 좌회전으로 두 곳의 불균형을 해결하는 예
>
> ![](https://velog.velcdn.com/images/chan9708/post/60a593d4-8d87-49ea-8f83-9866a5a74b12/image.png)

- 하지만, 다음과 같이 **한 번의 회전**으로 불균형을 해소되지 않을 수가 있다.

![](https://velog.velcdn.com/images/chan9708/post/b1d49180-1517-471e-83cf-b82356483e04/image.png)

- 이러한 상황을 해결하기 위해 **t를 루트로 하는 트리 수선 작업은 t의 네 손자 서브 트리 중 가장 깊은 것**에 따라 네 가지 유형으로 나뉜다.
  - **`LL`**
    - t.left.left가 가장 깊음
  - ![](https://velog.velcdn.com/images/chan9708/post/3399f671-f8c0-4532-b3c4-b3698d236bf1/image.png)
  - **`LR`**
    - t.left.right가 가장 깊음
  - ![](https://velog.velcdn.com/images/chan9708/post/50f341da-ae7e-4988-849e-9d25add8afa7/image.jpg)
  - **`RR`**
    - t.right.right가 가장 깊음
  - ![](https://velog.velcdn.com/images/chan9708/post/0996068c-4f84-4618-8920-f8fdcf4a9be2/image.png)
  - **`RL`**
    - t.right.left가 가장 깊음
  - ![](https://velog.velcdn.com/images/chan9708/post/d4476aae-ddab-46b9-b450-b519cd0c5414/image.png)

>

```python
balanceAVL(t, type):
  switch type:
    case LL: 우회전(t)
    case LR: 좌회전(t.left)
    		balanceAVL(t, LL)
    case RR: 좌회전(t)
    case RL: 우회전(t.right)
    		balanceAVL(t, RR)
```
