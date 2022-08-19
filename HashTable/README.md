![](https://velog.velcdn.com/images/chan9708/post/74a775f8-c24a-4df8-b3d5-8404955fe936/image.jpg)

# 해시 테이블

![](https://velog.velcdn.com/images/chan9708/post/9e66a649-8966-4c36-8bef-8dc7fc893da7/image.png)

- **키가 저장될 자리를 키의 `값`으로 결정하는 자료구조**
  - 즉, 저장된 자료와 비교하여 자리를 찾지 않고 단 한 번 계산하여 자기 자리를 찾는 것을 목표로 한다.
- 해시 테이블은 **자료를 검색, 삽입, 삭제하는데 평균 Θ(1)시간 즉, 상수 시간이 가능하다.**
- 즉, 데이터의 저장, 검색에서 극단적인 효율을 추구하는 자료구조이다.
- **`성질`**
  - 입력 원소가 해시 테이블 전체에 고루 저장되어야 한다.
  - 해시값 계산이 간단해야 한다.
- **`충돌`**
  - 해시 테이블의 장애물이며, 입력이 같은 해싯값으로 들어올 때를 말한다.
  - **`충돌 처리`**는 해시 테이블 이론의 핵심이며, 해결 방법이 여러가지이다.
- **`적재율`**
  - 해시 테이블에 원소가 차 있는 비율이다.
  - 해시 테이블의 성능에 매우 중요한 영향을 미친다.
  - 해시 테이블의 크기 : m, 저장된 키의 총 수 : n
    - n/m : 적재율 , 보통 α로 표기

## 해시 테이블의 객체 구조

>

- **`__table[]`** 🠔 해시 테이블로 사용하는 배열
- **`__numItems`** 🠔 해시 테이블의 원소 개수
  <br>
- **`search(x)`** 🠔 해시 테이블에서 원소 x를 검색한다.
- **`insert(x)`** 🠔 해시 테이블에 원소 x를 삽입한다.
- **`delete(x)`** 🠔 해시 테이블에서 원소 x를 삭제한다.
- **`isEmpty()`** 🠔 해시 테이블이 빈 상태인지 알려준다.
- **`clear()`** 🠔 해시 테이블을 깨끗이 청소한다.

---

# 해시 함수

- **`해시 함수`**
  - 킷값을 입력으로 받아 해시 테이블상의 주소로 리턴한다.
- <span style="font-size: 30px">**`입력 키를 해시 테이블 전체에 고루 분산시켜 저장해야 한다.`**</span>
- 두 키가 상대적으로 비슷하다고 해서 다른 키들보다 상대적으로 해싯값이 더 비슷하지 않아야 한다.

## 나누기 방법

- **나누기 방법은 해시 테이블 크기보다 큰 값을 해시 테이블 크기의 범위에 들어오도록 수축시키는 방식이다.**
- **`h(x) = x % m`**
- `m` : 해시 테이블의 크기
- `x` : 삽입할 원소의 Key
- **해시 테이블의 크기 m은 `2의 멱수`에 가깝지 않은 소수`를 택하는 것이 좋다.**
- m = 2ᵖ가 된다면, 입력 원소의 Key값의 하위 p-bits에 의해 해시 값이 결정되어 해시 값을 분산시키기가 어려워진다.

## 곱하기 방법

- **곱하기 방법은 입력값을 0과 1사이의 소수(Fraction)에 대응시킨 후 m을 곱하여 0부터 m−1사이의 값으로 팽창시키는 방식이다.**
- **`h(x)=⌊m(xA%1)⌋`**
- `m` : 해시 테이블의 크기
- `x` : 삽입할 원소의 Key
- `A` : 해시 함수의 특성값 (0<A<1)
  - A 는 입력값은 소수에 대응시키기 위한, 해당 해시함수만의 부동소수점 상수이다.
- xA값의 소수부만을 취하여 거기에 m을 곱한 값의 정수부가 x의 해시값이다.
- 해시 값 분포는 상수 A의 값에 영향을 받는다.
- 곱하기 방법에서는 m을 아무렇게나 잡아도 상관없다.
  <br>
- Donald Knuth가 제안한 상수 A의 값 = √5−1/2 = 0.6180339887 ⋯

---

# 충돌 해결

> Hash Table Structure의 고질병인 Colision을 해결하는데에는
> 크게 `Chaining(체이닝)`과 `Open Addressing(개방 주소)`방법이 있다.

## 체이닝 (Chaining)

![](https://velog.velcdn.com/images/chan9708/post/a5f7d732-9260-4218-9920-783e88fe4f9c/image.png)

>

```python
chainedHashInsert(T[], x) {
    // T: 해시 테이블
    // x: 삽입 원소
>
    리스트 T[h(x)]의 맨 앞에 x를 삽입
}
chainedHashSearch(T[], x) {
    // T: 해시 테이블
    // x: 검색 원소
>
    리스트 T[h(x)]에서 x값을 가진 원소를 검색
}
chainedHashDelete(T[], x) {
    // T: 해시 테이블
    // x: 삭제 원소
>
    리스트 T[h(x)]에서 x의 노드를 삭제
}
```

- 해시 테이블의 각 주소가 리스트의 헤더 역할을 하고, 여기에 들어오는 원소들이 Linked List로 매달리게 된다.
  (즉, 추가 공간을 사용하여 충돌을 해결하는 방식이다.)
- 같은 주소로 해싱되는 모든 원소를 하나의 Linked List에 보관한다.
- 해시 테이블의 크기가 m이면, 최대 m개의 Linked List Head가 존재할 수 있다.

* **체이닝은 적재율(α)이 1을 넘어도 사용할 수 있다.**

---

## 개방 주소 방법 (Open Addressing)

- 체이닝과 달리, 어떻게든 **`해시 테이블 내에서 충돌을 해결한다.`** (추가 공간을 허용하지 않는다.)
- 개방 주소 방법에서는 i번째 해싱 시 해당 공간에 원소가 차있는 경우를 대비하여  
  i+1 번째 해싱을 위한 해시 함수가 준비되어 있다.
  (즉, 해시 함수가 순차적으로 구성되어 있다.)

* **개방 주소 방법을 채택한 해시 테이블에서는 모든 원소가 반드시 자신의 해시 값과 일치하는 주소에 저장된다는 보장이 없다.**
* 개방 주소 방법은 다시, `선형 탐색 방법`, `이차원 탐색`, `더블 해싱`으로 구분된다.
* 체이닝 방법과 달리, **개방 주소 방법은 `적재율(α)이 1`을 초과할 수 없다.**
* 적재율이 높아지면 효율이 급격히 떨어지므로, 적당한 `Threshold(임계점)`을 설정한 후,
  이를 초과하면 해시 테이블의 크기(m)를 두 배로 키우고 모든 원소를 다시 해싱하는 것이 일반적이다.

### 선형 탐색

![](https://velog.velcdn.com/images/chan9708/post/47983889-4858-4d8d-9d74-55656fe97192/image.png)

- **`hᵢ(x)=(h(x)+i)%m i=0,1,2,⋯`**
- 가장 간단한 충돌 해결 방법으로, 충돌이 발생한 바로 뒷자리에 저장을 시도하는 방법이다. (간단한 정의)
- 충돌이 발생한 자리에서 i에 관한 일차 함수의 보폭으로 점프한 자리에 저장을 시도하는 방법이다. (보다 엄밀한 정의)
- 즉, 선형 조사 방법에서 h\_{i}(x) : h(x)에서 i만큼 떨어진 자리를 리턴하는 해시 함수이다.
  (테이블의 경계를 초과하는 경우, 테이블의 맨 앞자리로 이동한다.)
- **`1차 군집`**이 발생될 수 있다는 단점이 있다.
  - 선형 조사 방식에서 원소가 특정 영역에 몰리는 현상을 의미한다.
  - 1차 군집은 선형 조사법에서 해싱 시 조사 횟수를 증가시켜 성능을 저해한다.
  - 1차 군집은 해시 테이블의 성능을 치명적으로 저해시키는, 선형 조사 방식의 고질적인 문제점이다.

### 이차원 탐색

![](https://velog.velcdn.com/images/chan9708/post/919deea9-cb88-422a-8d1c-8b93a6e40fbd/image.png)

- **`hᵢ(x)=(h(x)+i+c₁i²+c₂i)%m i=0,1,2,⋯`**
- 충돌이 발생한 자리에서 i에 관한 이차 함수의 보폭으로 점프한 자리에 저장을 시도하는 방법이다.
- 이차원 조사의 경우, 특정 영역에 원소가 몰려도, 그 영역을 빨리 벗어날 수 있다.
- **`2차 군집`**
  - `위의 예시 그림 오른쪽`
  - 이차원 조사 방식에서, 여러 원소가 동일한 초기 해시값을 갖게 되어 모두 같은 순서로 조사하게 되는 현상을 의미한다.
  - 최초의 해시 값이 같은 원소들들은 이차원 조사 방식의 이점을 누리지 못하게 되어 해시 테이블의 효율을 저해한다.

### 더블 해싱

![](https://velog.velcdn.com/images/chan9708/post/5d777dd3-6f2d-4949-91e3-f2aa5a56aa7c/image.png)

- **`hᵢ(x)=(h(x)+i*f(x))%m i=0,1,2,⋯`**
- `h(x)=x%m `
  - m: 해시 테이블의 크기
- `f(x)=1+(x%m′) `
  - m′:m보다 약간 작은 소수(Prime Number)

* 충돌이 발생해서 다음 주소를 계산할 때, 두 번째 해시(f(x))값만큼 점프한다.
* 첫 번째 해시값이 같더라도, 두 번째 해시값까지 같을 확률이 매우 적어 2차 군집 문제가 발생될 확률이 적다.

> ![](https://velog.velcdn.com/images/chan9708/post/754d1bc8-10e8-4af0-86f1-1661060831b1/image.png)

### 개방 주소 방법에서의 원소 삭제

![](https://velog.velcdn.com/images/chan9708/post/04385e0a-8460-4222-9b9f-d42e884cdb43/image.png)

- 특정 원소를 삭제할 때, **해당 공간에 원소가 삭제되었음을 알리는 표식(그림의 `DELETED`)을 남겨서 위와 같은 현상을 예방한다.**
- 삽입과정에서 DELETED 표식을 만나게 되면,
  **해당 위치에 원소를 삽입하는 방법을 통해 DELETED 표식으로 인한 해시 테이블 공간 낭비를 방지할 수 있다.**

---

# 성능

- 체이닝 방법을 이용하는 해싱에서 적재율이 α일 때,
  **실패하는 검색에서의 조사 횟수 기대치는 α에 비례한다.**

- 체이닝 방법을 이용하는 해싱에서 적재율이 α일 때,
  **성공하는 검색에서의 조사 횟수 기대치는 (1+α)/2 + α/2n이다.**

- **개방 주소 방법의 이론적인 성능은 체이닝 보다 못하다.**

  > 증명에 대해선 [여기서](https://dad-rock.tistory.com/358)

- **어느 경우에서든, 적재율이 높으면 해싱 효율을 저해하므로 적절하게 낮은 적재율을 유지해야 한다.**