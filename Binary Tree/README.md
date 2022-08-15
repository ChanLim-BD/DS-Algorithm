![](https://velog.velcdn.com/images/chan9708/post/423b93fb-c3ee-4378-9e28-6335220d14e4/image.png)

# 검색 트리

![](https://velog.velcdn.com/images/chan9708/post/cafdbbbb-4580-4659-a087-67664611a9c1/image.png)

- **`노드`**
  - 값을 가진 개체
- **`루트`**
  - 맨 위에 있는 노드
  - 뿌리
- **`이진 검색 트리`**
  - 한 분기점에서 최대 2개까지만 분기할 수 있는 트리
- **`다진 검색 트리`**
  - `K진 검색 트리`라고도 하며 K개로 분기가 가능하다.
    <br>
- **저장되는 장소에 따라**
  - `내장 검색 트리`
    - 검색 트리가 메인 메모리 내에 존재하는 것
  - `외장 검색 트리`
    - 검색 트리가 외부(주로 디스크)에 존재하는 것

## 이진 검색 트리

- **각 노드는 킷값을 하나씩 갖는다.**
- **각 노드의 킷값은 모두 다르다.**
- **최상위 레벨에 루트 노드가 있다.**
- **각 노드는 최대 2개의 자식 노드를 갖는다.**
- **임의 노드의 킷값은 자신의 왼쪽 아래에 있는 모든 노드의 킷값보다 크다.**
- **오른쪽 아래에 있는 모든 노드의 킷값보다 작다.**
  <br>
- **`서브 트리`**
  - 검색 트리 내에 존재하는 부분적인 트리들

## 노드 객체의 구조

![](https://velog.velcdn.com/images/chan9708/post/61fcf7d0-2bf3-4c4c-9d99-8c93cf9fdc5d/image.png)

>

- **`__root`** 🠔 이진 검색 트리의 루트 노드
  <br>
- **`search(x)`** 🠔 이진 검색 트리에서 원소 x를 검색한다.
- **`insert(x)`** 🠔 이진 검색 트리에 원소 x를 삽입한다.
- **`delete(x)`** 🠔 이진 검색 트리에서 원소 x를 삭제한다.
- **`isEmpty()`** 🠔 이진 검색 트리에 키가 하나도 없이 비어 있는가?
- **`clear()`** 🠔 이진 검색 트리를 깨끗이 비운다.

---

### 검색

![](https://velog.velcdn.com/images/chan9708/post/f6712a71-2126-458e-a1c6-f1d63dd9a8b6/image.png)

>

```python
search(t, x):
   🠔 t: (서브) 트리의 루트 노드 레퍼런스, x: 검색하고자 하는 키
   if (t = null || t.item = x)
       return t
   else if (x < t.item)
       return search(t.left, x)  🠔  t.left: t의 왼자식
   else
       return search(t.right, x)  🠔  t.right: t의 오른자식
```

### 삽입

>

```
insertSketch(t, x):
   🠔 t: (서브) 트리의 루트 노드 레퍼런스, x: 검색하고자 하는 키
   if (t = null)
       x를 키로 하는 노드를 t의 부모 밑에 매달고 끝낸다.
   else if (x < t.item)
       insertSketch(t.left, x)
   else
       insertSketch(t.right, x)
```

### 삭제

>

```
deleteSketch(r):
   🠔 r: 삭제하고자 하는 노드
   if (r이 리프 노드)
       그냥 r을 버린다.
   else if (r의 자식이 하나만 있음)
       r의 부모가 r의 자식을 직접 가리키도록 한다.
   else
	   r의 오른쪽 서브 트리의 최소 원소 노드 s를 찾는다.
       s를 r자리로 복사하고 s를 삭제한다.
```

---

## 이진 검색 트리의 성질

**1. 정수 h≥1에 대해, 높이 h인 포화 이진 트리의 리프 노드의 총 수 l(h)는 2ᵸ⁻¹이다. 2. 정수 h≥0에 대해, 높이 h인 포화 이진 트리의 총 노드 수 n(h)는 2ᵸ⁻¹이다. 3. 정수 h≥0에 대해, 높이 h인 이진 트리는 2ᵸ⁻¹개 이하의 노드를 갖는다. 4. 총 n개의 노드를 가진 이진 트리의 높이는 적어도 h≥ ⌈log₂(n+1)⌉이다. 5. 총 n개의 노드를 가진 이진 트리의 최대 높이는 n이다. 6. 이진 검색 트리의 삽입에 드는 점근적 시간은 검색에 드는 시간과 동일하다. 7. n개의 노드를 가진 이진 검색 트리의 점근적 평균 검색 시간은 Θ(logn)이다.**

---

## 순회

![](https://velog.velcdn.com/images/chan9708/post/30995224-2c4f-4f08-b8fa-0035d1a809cd/image.png)

> **전위 순회**

```python
preOrder(r):
    if (r != null)
       r.visited = true
       preOrder(r.reft)
       preOrder(r.right)
```

> **중위 순회**

```python
inOrder(r):
    if (r != null)
       inOrder(r.reft)
       r.visited = true
       inOrder(r.right)
```

> **후위 순회**

```python
postOrder(r):
    if (r != null)
       postOrder(r.reft)
       postOrder(r.right)
       r.visited = true
```

---

# 출처

> [검색](https://www.techiedelight.com/ko/search-given-key-in-bst/)
