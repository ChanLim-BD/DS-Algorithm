![](https://velog.velcdn.com/images/chan9708/post/389c0105-9377-4ab1-b47f-d175fde17783/image.jpg)

## 1

> **가장 비싼 상품 구하기**

```sql
SELECT MAX(PRICE) AS MAX_PRICE
FROM PRODUCT
```

## 2

> **가격이 제일 비싼 식품의 정보 출력**

```sql
SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE
FROM FOOD_PRODUCT
ORDER BY PRICE DESC
LIMIT 1
```

## 3

> **최댓값 구하기**

```sql
SELECT DATETIME AS 시간
FROM ANIMAL_INS
ORDER BY DATETIME DESC
LIMIT 1
```

## 4

> **최솟값 구하기**

```sql
SELECT DATETIME AS 시간
FROM ANIMAL_INS
ORDER BY DATETIME ASC
LIMIT 1
```

## 5

> **동물 수 구하기**

```sql
SELECT count(*) AS count
FROM ANIMAL_INS
```

## 6

> **중복 제거하기**

```sql
SELECT count(DISTINCT NAME)
FROM ANIMAL_INS
```
