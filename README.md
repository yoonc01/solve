## Top-Down (하향식 DP) 사용 근거
- **문제가 재귀적으로 정의될 수 있을 때**  
  → 예: `f(n) = f(n-1) + f(n-2)`  
- **모든 부분 문제를 계산할 필요가 없을 때**  
  → 필요한 경우에만 계산하므로 불필요한 연산이 줄어듦  
- **조건 분기(케이스)가 많을 때**  
  → if-else로 분기하면서 각각 다른 하위 호출을 처리하기 용이  
- **트리, 그래프, 분할정복 기반 문제일 때**  
  → DFS, 재귀 탐색 중 메모이제이션을 함께 적용하기 쉬움  

> 큰 문제를 작은 문제로 “쪼개서 재귀로 푸는 방식”.  
> 이미 계산한 값은 저장해두고 다시 호출하지 않음 (메모이제이션).  

### 구현 예시
```python
dp = {}

def fibo(n):
    if n <= 2:
        return 1
    if n not in dp:               # 아직 계산 안 한 경우만 재귀 호출
        dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]
````

[예제 문항](https://github.com/yoonc01/solve/tree/main/%EB%B0%B1%EC%A4%80/Silver/9184.%E2%80%85%EC%9E%AC%EA%B7%80%ED%95%A8%EC%88%98)

---

## Bottom-Up (상향식 DP) 사용 근거

* **점화식이 명확하고 순차적으로 계산 가능한 경우**
  → 예: `dp[i] = dp[i-1] + dp[i-2]`
* **모든 부분 문제를 반드시 계산해야 하는 경우**
  → 테이블을 한 번에 채우는 것이 효율적
* **입력 크기가 크거나 재귀 깊이 제한이 우려될 때**
  → 반복문 기반이라 스택 오버플로우 위험이 없음
* **순차 DP (LIS, Knapsack 등)**
  → 배열 순서대로 누적 갱신하는 문제에 적합

> 작은 문제의 결과부터 미리 계산해 두고,
> 그 결과를 사용해 더 큰 문제를 해결하는 “테이블 기반” 방식.

### 구현 예시

```python
dp = [0] * (n + 1)
dp[1], dp[2] = 1, 1

for i in range(3, n + 1):
    dp[i] = dp[i-1] + dp[i-2]
```


## dictionary로 갯수 세기
```python
d = {}

for _ in range(n):
    word = input().strip()
    d[word] = d.get(word, 0) + 1
```

## 최대공약수(GCD) 구하는 방법

- 두 수의 **최대공약수(GCD, Greatest Common Divisor)** 는 두 수를 **나누어떨어지게 하는 공약수 중 가장 큰 수**를 의미한다.  
- 대표적인 방법은 **유클리드 호제법(Euclidean Algorithm)** 으로, 다음 성질을 이용한다:

>  `gcd(a, b) = gcd(b, a % b)`  
> 단, `b == 0`이면 `a`가 최대공약수이다.

이 성질을 반복적으로 적용하면 빠르게 최대공약수를 구할 수 있다.  
시간 복잡도는 `O(log min(a, b))` 로 매우 효율적이다.

---

### 구현 예시 (반복문)

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
````

### 구현 예시 (재귀)

```python
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
```

## XOR 사용 근거
- 값이 짝수 번 반복되고
- 원하는 값은 홀수 번 등장하고
- 순서와 상관없이 비트 연산 가능할 떄
[예제 문항](https://github.com/yoonc01/solve/tree/main/%EB%B0%B1%EC%A4%80/Bronze/3009.%E2%80%85%EB%84%A4%E2%80%85%EB%B2%88%EC%A7%B8%E2%80%85%EC%A0%90)

## DP 접근 근거
- 중복이 많아 불필요한 연산을 수행할 때 [예제 문항](https://github.com/yoonc01/solve/tree/main/%EB%B0%B1%EC%A4%80/Gold/12852.%E2%80%851%EB%A1%9C%E2%80%85%EB%A7%8C%EB%93%A4%EA%B8%B0%E2%80%852)

## JavaScript

### 클로저를 활용해서 받은 입력 관리하기

#### 예시 코드:
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%EB%B0%B1%EC%A4%80/Bronze/32905.%E2%80%85RACI/RACI.js)

## while / for + else 사용 근거
- 반복문을 통해 **특정 조건을 만족하는 원소나 해답을 탐색**하고,  
  **`break` 없이 반복이 끝난 경우(= 조건을 만족하지 못한 경우)**에만 별도 처리를 해야 할 때 사용
- 일반적으로 `found` 같은 플래그 변수를 쓰는 대신,  
  **`else` 블록을 통해 ‘조건 미충족 시 실행할 로직’을 깔끔하게 작성**할 수 있음

#### 예시 상황:
- 소수를 찾기 위해 약수를 탐색하다가 나누어떨어지면 `break`, 끝까지 못 찾으면 `else`에서 소수 판정
- 탐색 문제에서 원하는 값을 찾으면 조기 종료(`break`), 찾지 못했을 때만 `else`에서 실패 처리
- 무게나 합계 조건 등 반복을 돌며 조건을 만족시키는 경우를 찾고, 끝까지 못 찾았을 때만 기본값 출력

[예제 문항](https://github.com/yoonc01/solve/tree/main/%EB%B0%B1%EC%A4%80/Silver/2839.%E2%80%85%EC%84%A4%ED%83%95%E2%80%85%EB%B0%B0%EB%8B%AC)

## 정렬 후 매핑 → 원래 순서 복원 패턴 사용 근거
- **정렬이 필요한 계산(순위 산출, 압축, 우선순위 매기기 등)**을 수행해야 하지만,  
  **최종 결과는 입력의 원래 순서대로 출력해야 할 때** 활용

```python
arr = [50, 10, 30]

# 1. 중복 제거 + 정렬
sorted_arr = sorted(set(arr))  # [10, 30, 50]

# 2. 정렬된 값 -> 압축 인덱스 매핑
mapping = {val: idx for idx, val in enumerate(sorted_arr)}

# 3. 원래 순서대로 결과 복원
result = [mapping[val] for val in arr]


# 1. 원래 인덱스를 같이 저장
indexed = list(enumerate(arr))  # [(0, 50), (1, 10), (2, 30)]

# 2. 값 기준으로 정렬
indexed.sort(key=lambda x: x[1])  # [(1, 10), (2, 30), (0, 50)]

# 3. 정렬된 순서(예: 순위)를 원래 위치에 다시 기록
result = [0] * len(arr)
for rank, (original_idx, _) in enumerate(indexed):
    result[original_idx] = rank
```

[예제 문항](https://github.com/yoonc01/solve/tree/main/%EB%B0%B1%EC%A4%80/Silver/18870.%E2%80%85%EC%A2%8C%ED%91%9C%E2%80%85%EC%95%95%EC%B6%95)

---

## SQL

### 1. 특정 범위의 값 가져오기  
✅ **사용되는 SQL 함수**  
- `BETWEEN a AND b` : 특정 범위 내의 값 조회  

✅ **설명**  
`BETWEEN` 연산자를 사용하여 특정 값이 주어진 범위에 속하는지 확인할 수 있습니다.  

✅ **예시 코드**  
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/1/131535.%E2%80%85%EC%A1%B0%EA%B1%B4%EC%97%90%E2%80%85%EB%A7%9E%EB%8A%94%E2%80%85%ED%9A%8C%EC%9B%90%EC%88%98%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0/%EC%A1%B0%EA%B1%B4%EC%97%90%E2%80%85%EB%A7%9E%EB%8A%94%E2%80%85%ED%9A%8C%EC%9B%90%EC%88%98%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0.sql)  

---

### 2. 특정 문자열 검색  
✅ **사용되는 SQL 함수**  
- `LIKE` : 특정 문자열이 포함된 데이터 검색  

✅ **설명**  
`LIKE` 연산자를 사용하여 특정 문자열이 포함된 데이터를 조회할 수 있습니다.  
- `%` : 0개 이상의 문자를 의미  
- `_` : 정확히 한 개의 문자를 의미  

✅ **예시 코드**  
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/1/131112.%E2%80%85%EA%B0%95%EC%9B%90%EB%8F%84%EC%97%90%E2%80%85%EC%9C%84%EC%B9%98%ED%95%9C%E2%80%85%EC%83%9D%EC%82%B0%EA%B3%B5%EC%9E%A5%E2%80%85%EB%AA%A9%EB%A1%9D%E2%80%85%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0/%EA%B0%95%EC%9B%90%EB%8F%84%EC%97%90%E2%80%85%EC%9C%84%EC%B9%98%ED%95%9C%E2%80%85%EC%83%9D%EC%82%B0%EA%B3%B5%EC%9E%A5%E2%80%85%EB%AA%A9%EB%A1%9D%E2%80%85%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0.sql)  

---

### 3. NULL 값 처리  
✅ **사용되는 SQL 함수**  
- `IFNULL(x, y)` : NULL 값을 특정 값으로 대체 (MySQL 전용)  

✅ **설명**  
NULL 값을 처리할 때 `IFNULL`을 사용하여 대체 값을 설정할 수 있습니다.  

✅ **예시 코드**  
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/1/132201.%E2%80%8512%EC%84%B8%E2%80%85%EC%9D%B4%ED%95%98%EC%9D%B8%E2%80%85%EC%97%AC%EC%9E%90%E2%80%85%ED%99%98%EC%9E%90%E2%80%85%EB%AA%A9%EB%A1%9D%E2%80%85%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0/12%EC%84%B8%E2%80%85%EC%9D%B4%ED%95%98%EC%9D%B8%E2%80%85%EC%97%AC%EC%9E%90%E2%80%85%ED%99%98%EC%9E%90%E2%80%85%EB%AA%A9%EB%A1%9D%E2%80%85%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0.sql)  

---

### 4. 날짜 포맷 변경  
✅ **사용되는 SQL 함수**  
- `DATE_FORMAT(x, format)` : 날짜를 특정 형식으로 변환  

✅ **설명**  
날짜 데이터를 특정 형식(`YYYY-MM-DD`)으로 변환할 때 사용됩니다.  

✅ **예시 코드**  
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/1/132203.%E2%80%85%ED%9D%89%EB%B6%80%EC%99%B8%EA%B3%BC%E2%80%85%EB%98%90%EB%8A%94%E2%80%85%EC%9D%BC%EB%B0%98%EC%99%B8%EA%B3%BC%E2%80%85%EC%9D%98%EC%82%AC%E2%80%85%EB%AA%A9%EB%A1%9D%E2%80%85%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0/%ED%9D%89%EB%B6%80%EC%99%B8%EA%B3%BC%E2%80%85%EB%98%90%EB%8A%94%E2%80%85%EC%9D%BC%EB%B0%98%EC%99%B8%EA%B3%BC%E2%80%85%EC%9D%98%EC%82%AC%E2%80%85%EB%AA%A9%EB%A1%9D%E2%80%85%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0.sql)  

---

### 5. 특정 개수만큼 데이터 가져오기  
✅ **사용되는 SQL 함수**  
- `LIMIT n` : 상위 `n`개 데이터 조회  
- `LIMIT n OFFSET x` : `x`번째부터 `n`개 조회  

✅ **설명**  
테이블에서 특정 개수만큼 데이터를 조회할 때 사용됩니다.  

✅ **예시 코드**  
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/1/59405.%E2%80%85%EC%83%81%EC%9C%84%E2%80%85n%EA%B0%9C%E2%80%85%EB%A0%88%EC%BD%94%EB%93%9C/%EC%83%81%EC%9C%84%E2%80%85n%EA%B0%9C%E2%80%85%EB%A0%88%EC%BD%94%EB%93%9C.sql)  

---

### 6. 특정 열에 특정 문자열 포함 여부 확인  
✅ **사용되는 SQL 함수**  
- `IN (x, y, z)` : 특정 값이 열의 여러 값 중 하나인지 확인  

✅ **설명**  
특정 문자열이 여러 열 중 하나에 포함되어 있는지 확인할 때 사용됩니다.  

✅ **예시 코드**  
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/1/276013.%E2%80%85Python%E2%80%85%EA%B0%9C%EB%B0%9C%EC%9E%90%E2%80%85%EC%B0%BE%EA%B8%B0/Python%E2%80%85%EA%B0%9C%EB%B0%9C%EC%9E%90%E2%80%85%EC%B0%BE%EA%B8%B0.sql)  

---
### 7. NULL 값 필터링 (`IS NULL` / `IS NOT NULL`)  
✅ **사용되는 SQL 함수**  
- `IS NULL` : 해당 열이 `NULL`인 데이터만 조회  
- `IS NOT NULL` : 해당 열이 `NULL이 아닌 값`을 가진 데이터 조회  

✅ **설명**  
NULL 값을 포함한 데이터를 필터링할 때 `IS NULL` 또는 `IS NOT NULL`을 사용합니다.  
- `IS NULL`을 사용하면 특정 열이 `NULL`인 행만 조회됩니다.  
- `IS NOT NULL`을 사용하면 `NULL이 아닌 값`을 가진 행만 조회됩니다.  

✅ **예시 코드**  
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/1/293258.%E2%80%85%EC%9E%94%EC%B1%99%EC%9D%B4%E2%80%85%EC%9E%A1%EC%9D%80%E2%80%85%EC%88%98%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0/%EC%9E%94%EC%B1%99%EC%9D%B4%E2%80%85%EC%9E%A1%EC%9D%80%E2%80%85%EC%88%98%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0.sql)  

---

### 8. 평균값 계산 및 NULL 값 대체  
✅ **사용되는 SQL 함수**  
- `AVG(x)` : 평균값 계산  
- `COALESCE(x, y, ...)` : NULL이 아닌 첫 번째 값 반환  
- `ROUND(x, n)` : 소수점 `n`자리 반올림  

✅ **설명**  
NULL 값을 특정 값(예: `10`)으로 대체한 후, 평균값을 계산하고 소수점 두 자리까지 반올림하여 출력합니다.  

✅ **예시 코드**  
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/1/293259.%E2%80%85%EC%9E%A1%EC%9D%80%E2%80%85%EB%AC%BC%EA%B3%A0%EA%B8%B0%EC%9D%98%E2%80%85%ED%8F%89%EA%B7%A0%E2%80%85%EA%B8%B8%EC%9D%B4%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0/%EC%9E%A1%EC%9D%80%E2%80%85%EB%AC%BC%EA%B3%A0%EA%B8%B0%EC%9D%98%E2%80%85%ED%8F%89%EA%B7%A0%E2%80%85%EA%B8%B8%EC%9D%B4%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0.sql)  

---

### 9. 최댓값 구하기 (`MAX`)  
✅ **사용되는 SQL 함수**  
- `MAX(x)` : 특정 열에서 가장 큰 값 조회  

✅ **설명**  
`MAX` 함수를 사용하여 데이터에서 가장 큰 값을 찾습니다.  

✅ **예시 코드**  
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/1/131697.%E2%80%85%EA%B0%80%EC%9E%A5%E2%80%85%EB%B9%84%EC%8B%BC%E2%80%85%EC%83%81%ED%92%88%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0/%EA%B0%80%EC%9E%A5%E2%80%85%EB%B9%84%EC%8B%BC%E2%80%85%EC%83%81%ED%92%88%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0.sql)  

---

### 10. 최댓값에 단위 문자열 추가  
✅ **사용되는 SQL 함수**  
- `MAX(x)` : 최댓값 조회  
- `CONCAT(x, y)` : 문자열 연결  

✅ **설명**  
최댓값을 구한 후, `CONCAT` 함수를 사용하여 특정 단위를 붙여서 출력합니다.  

✅ **예시 코드**  
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/1/298515.%E2%80%85%EC%9E%A1%EC%9D%80%E2%80%85%EB%AC%BC%EA%B3%A0%EA%B8%B0%E2%80%85%EC%A4%91%E2%80%85%EA%B0%80%EC%9E%A5%E2%80%85%ED%81%B0%E2%80%85%EB%AC%BC%EA%B3%A0%EA%B8%B0%EC%9D%98%E2%80%85%EA%B8%B8%EC%9D%B4%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0/%EC%9E%A1%EC%9D%80%E2%80%85%EB%AC%BC%EA%B3%A0%EA%B8%B0%E2%80%85%EC%A4%91%E2%80%85%EA%B0%80%EC%9E%A5%E2%80%85%ED%81%B0%E2%80%85%EB%AC%BC%EA%B3%A0%EA%B8%B0%EC%9D%98%E2%80%85%EA%B8%B8%EC%9D%B4%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0.sql)  

---

### 11. 최댓값 조회 및 서브쿼리를 이용한 특정 값 필터링  
✅ **사용되는 SQL 함수**  
- `MAX(x)` : 최댓값 조회  
- `WHERE x = (SELECT MAX(y) FROM table)` : **서브쿼리**를 이용한 특정 값 필터링  

✅ **서브쿼리(서브쿼리, Subquery)란?**  
- **서브쿼리**는 SQL문 내부에 포함된 또 다른 **SELECT 문**을 의미합니다.  
- 보통 `WHERE`, `FROM`, `SELECT` 절에서 사용되며, 특정 값을 동적으로 조회할 때 유용합니다.  

✅ **서브쿼리 활용 예시**  
1️⃣ **최댓값 조회 후 해당 행 찾기**  
```sql
SELECT *
FROM FOOD_PRODUCT
WHERE PRICE = (SELECT MAX(PRICE) FROM FOOD_PRODUCT);
```
- `SELECT MAX(PRICE) FROM FOOD_PRODUCT` : 가장 비싼 가격을 찾음  
- `WHERE PRICE = (서브쿼리 결과)` : 그 가격을 가진 행을 조회  

2️⃣ **특정 카테고리에 속하는 제품 중 최소 가격 조회**  
```sql
SELECT *
FROM FOOD_PRODUCT
WHERE PRICE = (SELECT MIN(PRICE) FROM FOOD_PRODUCT WHERE CATEGORY = '식용유');
```
- `SELECT MIN(PRICE) ... WHERE CATEGORY = '식용유'` : 식용유 중 가장 저렴한 가격 조회  
- `WHERE PRICE = (서브쿼리 결과)` : 그 가격을 가진 제품 조회  

✅ **설명**  
`MAX(PRICE)`를 사용하여 가장 비싼 식품의 가격을 찾고, 해당 가격을 가진 식품의 정보를 조회합니다.  
이때, **서브쿼리**를 활용하여 최댓값을 동적으로 가져오고, `WHERE` 절에서 그 값을 필터링합니다.  

✅ **예시 코드**  
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/2/131115.%E2%80%85%EA%B0%80%EA%B2%A9%EC%9D%B4%E2%80%85%EC%A0%9C%EC%9D%BC%E2%80%85%EB%B9%84%EC%8B%BC%E2%80%85%EC%8B%9D%ED%92%88%EC%9D%98%E2%80%85%EC%A0%95%EB%B3%B4%E2%80%85%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0/%EA%B0%80%EA%B2%A9%EC%9D%B4%E2%80%85%EC%A0%9C%EC%9D%BC%E2%80%85%EB%B9%84%EC%8B%BC%E2%80%85%EC%8B%9D%ED%92%88%EC%9D%98%E2%80%85%EC%A0%95%EB%B3%B4%E2%80%85%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0.sql)  

---

### 12. 최댓값 구하기 (`MAX`)  
✅ **사용되는 SQL 함수**  
- `MIN(x)` : 특정 열에서 가장 작은 값 조회  

✅ **설명**  
`MIN` 함수를 사용하여 데이터에서 가장 작은 값을 찾습니다.  

✅ **예시 코드**  
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/2/59038.%E2%80%85%EC%B5%9C%EC%86%9F%EA%B0%92%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0/%EC%B5%9C%EC%86%9F%EA%B0%92%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0.sql)

---

### 13. 그룹화와 조건 필터링을 이용한 조회  
✅ **사용되는 SQL 함수**  
- `GROUP BY x, y` : 특정 컬럼 조합으로 그룹화  
- `HAVING COUNT(z) > n` : 그룹별 개수가 특정 값 이상인 데이터 필터링  
- `ORDER BY x ASC, y DESC` : 정렬 기준 설정  

✅ **설명**  
동일한 회원(`USER_ID`)이 동일한 상품(`PRODUCT_ID`)을 **두 번 이상 구매한 경우**를 찾기 위해,  
- `GROUP BY USER_ID, PRODUCT_ID`를 사용하여 **회원-상품 조합별로 그룹화**  
- `HAVING COUNT(ONLINE_SALE_ID) > 1`을 사용하여 **재구매(2회 이상 구매)한 조합 필터링**  
- `ORDER BY USER_ID ASC, PRODUCT_ID DESC`로 정렬하여 **회원 ID 오름차순, 상품 ID 내림차순 출력**  

✅ **예시 코드**  
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/2/131536.%E2%80%85%EC%9E%AC%EA%B5%AC%EB%A7%A4%EA%B0%80%E2%80%85%EC%9D%BC%EC%96%B4%EB%82%9C%E2%80%85%EC%83%81%ED%92%88%EA%B3%BC%E2%80%85%ED%9A%8C%EC%9B%90%E2%80%85%EB%A6%AC%EC%8A%A4%ED%8A%B8%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0/%EC%9E%AC%EA%B5%AC%EB%A7%A4%EA%B0%80%E2%80%85%EC%9D%BC%EC%96%B4%EB%82%9C%E2%80%85%EC%83%81%ED%92%88%EA%B3%BC%E2%80%85%ED%9A%8C%EC%9B%90%E2%80%85%EB%A6%AC%EC%8A%A4%ED%8A%B8%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0.sql)  

---

### 14. 윈도우 함수(OVER)를 이용한 연도별 편차 계산  
✅ **사용되는 SQL 함수**  
- `YEAR(x)` : 날짜에서 연도 추출  
- `MAX(x) OVER (PARTITION BY y)` : **윈도우 함수**를 사용하여 그룹별 최댓값 계산  

✅ **윈도우 함수(OVER)란?**  
윈도우 함수(OVER)는 **일반적인 GROUP BY와 달리 집계 결과를 각 행에 유지하면서 계산하는 방식**입니다.  
즉, **데이터를 그룹화하면서도 개별 행의 정보는 그대로 유지**할 수 있습니다.  

💡 **윈도우 함수의 주요 특징**  
1️⃣ **GROUP BY 없이도 그룹별 값 계산 가능**  
   - `OVER (PARTITION BY ...)`을 사용하면 각 그룹별로 계산된 값을 각 행에 추가할 수 있음  
2️⃣ **원본 데이터 유지**  
   - 일반적인 집계 함수(`MAX`, `SUM`, `AVG` 등)와 달리, **원본 테이블의 모든 행을 유지한 채 연산 수행**  
3️⃣ **다른 열과 함께 활용 가능**  
   - 서브쿼리를 사용하지 않고도 **원본 데이터와 집계 데이터를 함께 조회할 수 있음**  

✅ **설명**  
1️⃣ `YEAR(DIFFERENTIATION_DATE) AS YEAR` : **분화된 연도**를 추출  
2️⃣ `MAX(SIZE_OF_COLONY) OVER (PARTITION BY YEAR(DIFFERENTIATION_DATE)) AS MAX_SIZE`  
   - **각 연도별로 가장 큰 대장균의 크기**를 구함  
   - **윈도우 함수(OVER)를 사용하여 연도별 MAX 값을 각 행에 추가**  
3️⃣ `(MAX_SIZE - SIZE_OF_COLONY) AS YEAR_DEV`  
   - **해당 연도의 최댓값에서 개별 대장균의 크기를 뺀 값(편차) 계산**  


✅ **예시 코드**  
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/2/299310.%E2%80%85%EC%97%B0%EB%8F%84%EB%B3%84%E2%80%85%EB%8C%80%EC%9E%A5%EA%B7%A0%E2%80%85%ED%81%AC%EA%B8%B0%EC%9D%98%E2%80%85%ED%8E%B8%EC%B0%A8%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0/%EC%97%B0%EB%8F%84%EB%B3%84%E2%80%85%EB%8C%80%EC%9E%A5%EA%B7%A0%E2%80%85%ED%81%AC%EA%B8%B0%EC%9D%98%E2%80%85%ED%8E%B8%EC%B0%A8%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0.sql)  

---

### 15. 서브쿼리와 JOIN을 활용한 물고기 종류별 최대 길이 조회  
✅ **사용되는 SQL 함수**  
- `JOIN ON x = y` : 두 테이블을 연결하여 관련 데이터 조회  
- `MAX(x)` : 특정 그룹에서 최댓값 계산  
- `GROUP BY x` : 그룹별 집계 연산 수행  
- `WHERE (x, y) IN (서브쿼리)` : 서브쿼리를 활용한 다중 조건 필터링  

✅ **설명**  
1️⃣ `JOIN FISH_NAME_INFO ON FISH_INFO.FISH_TYPE = FISH_NAME_INFO.FISH_TYPE`  
   - **FISH_INFO 테이블과 FISH_NAME_INFO 테이블을 조인**하여 물고기 종류별 이름을 가져옴  
2️⃣ `MAX(LENGTH) OVER (PARTITION BY FISH_TYPE)`  
   - **물고기 종류별 가장 큰 길이를 찾음**  
3️⃣ `WHERE (FISH_TYPE, LENGTH) IN (서브쿼리)`  
   - **각 물고기 종류별로 최댓값을 가진 행만 필터링**  
4️⃣ `ORDER BY ID ASC`  
   - **물고기 ID 기준 오름차순 정렬**  

✅ **예시 코드**  
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/3/293261.%E2%80%85%EB%AC%BC%EA%B3%A0%EA%B8%B0%E2%80%85%EC%A2%85%EB%A5%98%E2%80%85%EB%B3%84%E2%80%85%EB%8C%80%EC%96%B4%E2%80%85%EC%B0%BE%EA%B8%B0/%EB%AC%BC%EA%B3%A0%EA%B8%B0%E2%80%85%EC%A2%85%EB%A5%98%E2%80%85%EB%B3%84%E2%80%85%EB%8C%80%EC%96%B4%E2%80%85%EC%B0%BE%EA%B8%B0.sql)  

---

### 16. JOIN과 GROUP BY를 활용한 상품코드별 오프라인 매출액 계산  
✅ **사용되는 SQL 함수**  
- `JOIN ON x = y` : 두 테이블을 연결하여 관련 데이터 조회  
- `SUM(x * y)` : 총 매출액 계산 (판매량 * 판매가)  
- `GROUP BY x` : 그룹별 집계 연산 수행  
- `ORDER BY x DESC, y ASC` : 내림차순 및 오름차순 정렬  

✅ **설명**  
1️⃣ `JOIN OFFLINE_SALE ON PRODUCT.PRODUCT_ID = OFFLINE_SALE.PRODUCT_ID`  
   - **상품 정보(PRODUCT)와 판매 정보(OFFLINE_SALE)를 연결하여 상품별 판매 내역을 가져옴**  
2️⃣ `SUM(SALES_AMOUNT * PRICE) AS SALES`  
   - **판매량 * 판매가를 합산하여 상품코드별 총 매출액을 계산**  
3️⃣ `GROUP BY PRODUCT_CODE`  
   - **상품 코드(PRODUCT_CODE)별로 그룹화하여 매출액 집계**  
4️⃣ `ORDER BY SALES DESC, PRODUCT_CODE ASC`  
   - **매출액이 높은 순으로 정렬하고, 매출액이 같다면 상품 코드를 오름차순 정렬**  


✅ **예시 코드**  
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/2/131533.%E2%80%85%EC%83%81%ED%92%88%E2%80%85%EB%B3%84%E2%80%85%EC%98%A4%ED%94%84%EB%9D%BC%EC%9D%B8%E2%80%85%EB%A7%A4%EC%B6%9C%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0/%EC%83%81%ED%92%88%E2%80%85%EB%B3%84%E2%80%85%EC%98%A4%ED%94%84%EB%9D%BC%EC%9D%B8%E2%80%85%EB%A7%A4%EC%B6%9C%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0.sql)  

---
### 17. LEFT JOIN과 NULL 필터링을 이용한 유실된 입양 기록 조회  
✅ **사용되는 SQL 함수**  
- `LEFT JOIN ON x = y` : **왼쪽 테이블(기준 테이블)의 모든 데이터를 가져오고, 오른쪽 테이블에서 일치하는 데이터만 가져오는 방식**  
- `WHERE x IS NULL` : 특정 컬럼이 NULL인 데이터 필터링  

✅ **LEFT JOIN이란?**  
`LEFT JOIN`은 **두 개의 테이블을 조인할 때, 왼쪽 테이블(기준 테이블)의 모든 데이터를 가져오고, 오른쪽 테이블에서 일치하는 데이터만 가져오는 방식**이야.  
- 만약 오른쪽 테이블에 일치하는 데이터가 없으면, 해당 컬럼에 **NULL이 들어감**  
- 이를 활용하면 **어떤 데이터가 없는지 쉽게 찾을 수 있어!**  

💡 **LEFT JOIN의 작동 방식 예시**  

| ANIMAL_OUTS (왼쪽 테이블) | ANIMAL_INS (오른쪽 테이블) | 조인 결과 |
|----------------|----------------|-----------|
| A349733, Allie | NULL | A349733, Allie (유실 데이터) |
| A352713, Gia | A352713, Gia | 제외됨 (데이터 존재) |
| A349990, Spice | NULL | A349990, Spice (유실 데이터) |

✅ **설명**  
1️⃣ `LEFT JOIN ANIMAL_INS ON ANIMAL_OUTS.ANIMAL_ID = ANIMAL_INS.ANIMAL_ID`  
   - **입양된 동물(ANIMAL_OUTS)을 기준**으로 보호소에 들어온 기록(ANIMAL_INS)을 조인  
   - **입양 기록은 있지만 보호소 기록이 없는 경우 NULL 값이 들어감**  
2️⃣ `WHERE ANIMAL_INS.ANIMAL_ID IS NULL`  
   - **NULL인 데이터를 필터링하여 보호소 기록이 없는 유실 데이터를 찾음**  
3️⃣ `ORDER BY ANIMAL_ID ASC`  
   - **ID 순으로 정렬하여 결과 출력**  

✅ **예시 코드**  
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/3/59042.%E2%80%85%EC%97%86%EC%96%B4%EC%A7%84%E2%80%85%EA%B8%B0%EB%A1%9D%E2%80%85%EC%B0%BE%EA%B8%B0/%EC%97%86%EC%96%B4%EC%A7%84%E2%80%85%EA%B8%B0%EB%A1%9D%E2%80%85%EC%B0%BE%EA%B8%B0.sql)  

---

### 18. GROUP BY와 CASE를 활용한 동물 보호소의 고양이·개 개수 조회  
✅ **사용되는 SQL 함수**  
- `GROUP BY x` : 특정 열을 기준으로 그룹화하여 집계 연산 수행  
- `COUNT(*)` : 각 그룹별 데이터 개수 계산  
- `HAVING x IN (y, z)` : 특정 값만 필터링  
- `ORDER BY CASE WHEN x THEN y ELSE z END` : 특정 순서로 정렬

```sql
ORDER BY 
    CASE 
        WHEN ANIMAL_TYPE = 'Cat' THEN 1
        WHEN ANIMAL_TYPE = 'Dog' THEN 2
        WHEN ANIMAL_TYPE = 'Rabbit' THEN 3
        ELSE 4 -- 그 외 동물은 마지막 정렬
    END;
```
✅ **HAVING vs. WHERE 차이점**  
| 비교 항목 | WHERE | HAVING |
|-----------|-------------|----------------|
| **적용 시점** | **GROUP BY 이전** (행 필터링) | **GROUP BY 이후** (그룹 필터링) |
| **대상** | 개별 행 | 그룹(집계 함수 적용 후) |
| **사용 가능 연산** | `=`, `LIKE`, `IN`, `BETWEEN`, `NULL` 체크 등 | `COUNT()`, `SUM()`, `MAX()` 같은 집계 함수 사용 가능 |
| **예시** | `WHERE ANIMAL_TYPE = 'Cat'` → 고양이 행만 조회 | `HAVING COUNT(*) > 1` → 2마리 이상인 그룹만 조회 |

💡 **WHERE은 개별 행을 걸러내고, HAVING은 그룹화된 결과를 걸러낸다!**  

✅ **설명**  
1️⃣ `GROUP BY ANIMAL_TYPE`  
   - **ANIMAL_TYPE(동물 종)별로 그룹화하여 개수를 계산**  
2️⃣ `COUNT(*) AS count`  
   - **각 그룹(고양이, 개)의 개수를 계산**  
3️⃣ `HAVING ANIMAL_TYPE IN ('Cat', 'Dog')`  
   - **고양이(Cat)와 개(Dog)만 필터링** (`HAVING`을 사용한 이유: GROUP BY 이후 필터링이 필요하기 때문!)  
4️⃣ `ORDER BY CASE WHEN ANIMAL_TYPE = 'Cat' THEN 1 ELSE 2 END`  
   - **고양이를 먼저, 개를 나중에 정렬**  

✅ **예시 코드**  
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/2/59040.%E2%80%85%EA%B3%A0%EC%96%91%EC%9D%B4%EC%99%80%E2%80%85%EA%B0%9C%EB%8A%94%E2%80%85%EB%AA%87%E2%80%85%EB%A7%88%EB%A6%AC%E2%80%85%EC%9E%88%EC%9D%84%EA%B9%8C/%EA%B3%A0%EC%96%91%EC%9D%B4%EC%99%80%E2%80%85%EA%B0%9C%EB%8A%94%E2%80%85%EB%AA%87%E2%80%85%EB%A7%88%EB%A6%AC%E2%80%85%EC%9E%88%EC%9D%84%EA%B9%8C.sql)  

---
### 19. CASE와 GROUP BY를 활용한 자동차 대여 상태 조회  
✅ **사용되는 SQL 함수**  
- `CASE WHEN x THEN y ELSE z END` : 조건에 따라 값 반환  
- `BETWEEN x AND y` : 특정 범위 내 데이터 조회  
- `SUM(CASE WHEN condition THEN 1 ELSE 0 END)` : 조건을 만족하는 개수 계산  
- `GROUP BY x` : 특정 열을 기준으로 그룹화  
- `ORDER BY x DESC` : 내림차순 정렬  

✅ **설명**  
1️⃣ `SUM(CASE WHEN '2022-10-16' BETWEEN START_DATE AND END_DATE THEN 1 ELSE 0 END) > 0`  
   - **대여 시작일(START_DATE)과 반납일(END_DATE) 사이에 '2022-10-16'이 포함되면 1을 반환**  
   - `SUM()`을 사용하여 **해당 자동차가 2022-10-16에 대여된 횟수를 계산**  
2️⃣ `CASE WHEN SUM(...) > 0 THEN '대여중' ELSE '대여 가능' END`  
   - **대여 횟수가 1 이상이면 '대여중', 그렇지 않으면 '대여 가능'으로 설정**  
3️⃣ `GROUP BY CAR_ID`  
   - **자동차 ID별로 그룹화하여 상태를 결정**  
4️⃣ `ORDER BY CAR_ID DESC`  
   - **자동차 ID를 기준으로 내림차순 정렬**  

✅ **예시 코드**  
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/3/157340.%E2%80%85%EC%9E%90%EB%8F%99%EC%B0%A8%E2%80%85%EB%8C%80%EC%97%AC%E2%80%85%EA%B8%B0%EB%A1%9D%EC%97%90%EC%84%9C%E2%80%85%EB%8C%80%EC%97%AC%EC%A4%91%E2%80%85%EF%BC%8F%E2%80%85%EB%8C%80%EC%97%AC%E2%80%85%EA%B0%80%EB%8A%A5%E2%80%85%EC%97%AC%EB%B6%80%E2%80%85%EA%B5%AC%EB%B6%84%ED%95%98%EA%B8%B0/%EC%9E%90%EB%8F%99%EC%B0%A8%E2%80%85%EB%8C%80%EC%97%AC%E2%80%85%EA%B8%B0%EB%A1%9D%EC%97%90%EC%84%9C%E2%80%85%EB%8C%80%EC%97%AC%EC%A4%91%E2%80%85%EF%BC%8F%E2%80%85%EB%8C%80%EC%97%AC%E2%80%85%EA%B0%80%EB%8A%A5%E2%80%85%EC%97%AC%EB%B6%80%E2%80%85%EA%B5%AC%EB%B6%84%ED%95%98%EA%B8%B0.sql)

---
### 20. LEFT JOIN과 COUNT를 활용한 대장균 개체의 자식 수 조회  
✅ **사용되는 SQL 함수**  
- `LEFT JOIN ON x = y` : 한 테이블을 자기 자신과 조인하여 부모-자식 관계 매칭  
- `COUNT(x)` : 특정 그룹 내 개수 계산  
- `GROUP BY x` : 특정 열을 기준으로 그룹화  
- `ORDER BY x ASC` : 오름차순 정렬  

✅ **설명**  
1️⃣ `LEFT JOIN ECOLI_DATA C ON E.ID = C.PARENT_ID`  
   - **ECOLI_DATA 테이블을 자기 자신과 조인하여 부모-자식 관계 형성**  
   - `E.ID`는 부모 개체, `C.PARENT_ID`는 해당 부모 개체에서 분화된 자식 개체  
2️⃣ `COUNT(C.PARENT_ID) AS CHILD_COUNT`  
   - **부모 개체별로 자식 개체 개수를 계산**  
   - `LEFT JOIN`을 사용했기 때문에 자식이 없는 경우 `NULL`이 되고, `COUNT(NULL)`은 0이 됨  
3️⃣ `GROUP BY E.ID`  
   - **각 부모 개체 ID별로 자식 개체 개수 집계**  
4️⃣ `ORDER BY E.ID`  
   - **개체 ID 기준 오름차순 정렬**  

✅ **예시 코드**  
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/3/299305.%E2%80%85%EB%8C%80%EC%9E%A5%EA%B7%A0%EB%93%A4%EC%9D%98%E2%80%85%EC%9E%90%EC%8B%9D%EC%9D%98%E2%80%85%EC%88%98%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0/%EB%8C%80%EC%9E%A5%EA%B7%A0%EB%93%A4%EC%9D%98%E2%80%85%EC%9E%90%EC%8B%9D%EC%9D%98%E2%80%85%EC%88%98%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0.sql)  

---
### 21. CASE를 활용한 대장균 개체 크기 분류  
✅ **사용되는 SQL 함수**  
- `CASE WHEN x THEN y ELSE z END` : 특정 조건에 따라 값 반환  
- `ORDER BY x ASC` : 오름차순 정렬  

✅ **설명**  
1️⃣ `CASE`를 사용하여 크기 범위별로 분류  
   - `SIZE_OF_COLONY <= 100` → `'LOW'`  
   - `SIZE_OF_COLONY > 1000` → `'HIGH'`  
   - 나머지 (`100 < SIZE_OF_COLONY <= 1000`) → `'MEDIUM'`  
2️⃣ `ORDER BY ID`  
   - **개체 ID를 기준으로 오름차순 정렬**  

✅ **예제 SQL**  
```sql
SELECT ID, 
       CASE 
           WHEN SIZE_OF_COLONY <= 100 THEN 'LOW'
           WHEN SIZE_OF_COLONY > 1000 THEN 'HIGH'
           ELSE 'MEDIUM'
       END AS SIZE
FROM ECOLI_DATA
ORDER BY ID;
```

✅ **예시 코드**  
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/3/299307.%E2%80%85%EB%8C%80%EC%9E%A5%EA%B7%A0%EC%9D%98%E2%80%85%ED%81%AC%EA%B8%B0%EC%97%90%E2%80%85%EB%94%B0%EB%9D%BC%E2%80%85%EB%B6%84%EB%A5%98%ED%95%98%EA%B8%B0%E2%80%851/%EB%8C%80%EC%9E%A5%EA%B7%A0%EC%9D%98%E2%80%85%ED%81%AC%EA%B8%B0%EC%97%90%E2%80%85%EB%94%B0%EB%9D%BC%E2%80%85%EB%B6%84%EB%A5%98%ED%95%98%EA%B8%B0%E2%80%851.sql)  

---

### 22. WITH과 PERCENT_RANK를 활용한 대장균 크기별 분류  
✅ **사용되는 SQL 함수**  
- `WITH x AS (...)` : **공통 테이블 표현식(CTE)**, 서브쿼리를 간결하게 작성  
- `PERCENT_RANK() OVER (ORDER BY x DESC)` : **백분위 순위 계산**  
- `CASE WHEN x THEN y ELSE z END` : 특정 조건에 따라 값 반환  
- `ORDER BY x ASC` : 오름차순 정렬  


✅ **WITH(공통 테이블 표현식, CTE)란?**  
`WITH` 문법은 **하나의 서브쿼리를 임시 테이블처럼 사용**하여 쿼리를 더 간결하고 읽기 쉽게 만들어줘!  
- **장점**  
  - 복잡한 쿼리를 분리하여 가독성 향상  
  - 동일한 서브쿼리를 여러 번 사용할 때 성능 최적화 가능  

💡 **CTE 예제**  
```sql
WITH TEMP_TABLE AS (
    SELECT ID, SIZE_OF_COLONY
    FROM ECOLI_DATA
)
SELECT * FROM TEMP_TABLE;
```
위 코드는 `ECOLI_DATA` 테이블에서 ID와 크기만 포함하는 `TEMP_TABLE`을 만든 후, 이를 조회하는 방식이야!


✅ **PERCENT_RANK()란?**  
`PERCENT_RANK()`는 **데이터의 순위를 백분율(0~1)로 계산**하는 윈도우 함수야.  
- 가장 큰 값은 `0`, 가장 작은 값은 `1`에 가까운 값이 돼  
- `(순위 - 1) / (총 행 개수 - 1)` 공식을 사용  

💡 **PERCENT_RANK 예제**  
```sql
SELECT ID, SIZE_OF_COLONY, 
       PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY DESC) AS PCT
FROM ECOLI_DATA;
```
위 쿼리는 대장균 크기를 내림차순으로 정렬한 후, 각 개체의 백분위 순위를 계산해!


✅ **설명**  
1️⃣ `WITH RANKED_ECOLI AS (...)`  
   - **PERCENT_RANK()를 사용해 크기별 백분위 순위를 계산한 임시 테이블 생성**  
2️⃣ `CASE WHEN PCT <= 0.25 THEN 'CRITICAL' ... ELSE 'LOW' END`  
   - **백분위 순위에 따라 그룹을 나눠 COLONY_NAME 부여**  
3️⃣ `ORDER BY ID`  
   - **개체 ID 기준으로 오름차순 정렬**  

✅ **예제 SQL**  
```sql
WITH RANKED_ECOLI AS (
    SELECT ID, SIZE_OF_COLONY,
           PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY DESC) AS PCT
    FROM ECOLI_DATA
)
SELECT ID, 
       CASE 
           WHEN PCT <= 0.25 THEN 'CRITICAL'
           WHEN PCT <= 0.50 THEN 'HIGH'
           WHEN PCT <= 0.75 THEN 'MEDIUM'
           ELSE 'LOW'
       END AS COLONY_NAME
FROM RANKED_ECOLI
ORDER BY ID;
```

✅ **예시 코드**  
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/3/301649.%E2%80%85%EB%8C%80%EC%9E%A5%EA%B7%A0%EC%9D%98%E2%80%85%ED%81%AC%EA%B8%B0%EC%97%90%E2%80%85%EB%94%B0%EB%9D%BC%E2%80%85%EB%B6%84%EB%A5%98%ED%95%98%EA%B8%B0%E2%80%852/%EB%8C%80%EC%9E%A5%EA%B7%A0%EC%9D%98%E2%80%85%ED%81%AC%EA%B8%B0%EC%97%90%E2%80%85%EB%94%B0%EB%9D%BC%E2%80%85%EB%B6%84%EB%A5%98%ED%95%98%EA%B8%B0%E2%80%852.sql)  

---
### 23. UNION과 UNION ALL을 활용한 온라인/오프라인 판매 데이터 통합  
✅ **사용되는 SQL 함수**  
- `UNION` : 두 개 이상의 쿼리 결과를 **합치면서 중복을 제거**  
- `UNION ALL` : 두 개 이상의 쿼리 결과를 **그대로 합치고 중복을 유지**  
- `DATE_FORMAT(x, '%Y-%m-%d')` : 날짜 형식을 `YYYY-MM-DD`로 변환  
- `YEAR(x)`, `MONTH(x)` : 날짜에서 연도 및 월 추출  
- `ORDER BY x, y, z` : 다중 기준으로 정렬  

✅ **UNION vs. UNION ALL 차이점**  
| 연산자 | 중복 제거 | 성능 | 사용 예시 |
|--------|----------|------|----------|
| `UNION` | **O** (중복된 행 제거) | **느림** (중복 제거 과정 필요) | 고객 정보 중복 제거 후 조회 |
| `UNION ALL` | **X** (중복된 행 포함) | **빠름** (있는 그대로 합침) | 로그 데이터 합치기, 중복 포함한 데이터 분석 |

💡 **UNION 예제 (중복 제거)**  
```sql
SELECT USER_ID FROM ONLINE_SALE
UNION
SELECT USER_ID FROM OFFLINE_SALE;
```
→ 온라인과 오프라인에서 **중복 없이** 사용자 ID를 조회  

💡 **UNION ALL 예제 (중복 포함)**  
```sql
SELECT USER_ID FROM ONLINE_SALE
UNION ALL
SELECT USER_ID FROM OFFLINE_SALE;
```
→ 온라인과 오프라인에서 **중복 포함하여** 사용자 ID를 조회  

✅ **설명**  
1️⃣ `SELECT ... FROM ONLINE_SALE WHERE YEAR(SALES_DATE) = 2022 AND MONTH(SALES_DATE) = 3`  
   - **2022년 3월의 온라인 판매 데이터 조회**  
2️⃣ `SELECT ... FROM OFFLINE_SALE WHERE YEAR(SALES_DATE) = 2022 AND MONTH(SALES_DATE) = 3`  
   - **2022년 3월의 오프라인 판매 데이터 조회**  
   - `USER_ID`가 없기 때문에 `NULL`로 설정  
3️⃣ `UNION ALL`  
   - **두 개의 결과를 중복 포함하여 합침**  
4️⃣ `ORDER BY SALES_DATE, PRODUCT_ID, USER_ID`  
   - **판매일 → 상품 ID → 유저 ID 순으로 정렬**  

✅ **예제 SQL**  
```sql
SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, 
       PRODUCT_ID, 
       USER_ID, 
       SALES_AMOUNT
FROM ONLINE_SALE
WHERE YEAR(SALES_DATE) = 2022 AND MONTH(SALES_DATE) = 3

UNION ALL

SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, 
       PRODUCT_ID, 
       NULL AS USER_ID, 
       SALES_AMOUNT
FROM OFFLINE_SALE
WHERE YEAR(SALES_DATE) = 2022 AND MONTH(SALES_DATE) = 3

ORDER BY SALES_DATE, PRODUCT_ID, USER_ID;
```

✅ **예시 코드**  
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/4/131537.%E2%80%85%EC%98%A4%ED%94%84%EB%9D%BC%EC%9D%B8%EF%BC%8F%EC%98%A8%EB%9D%BC%EC%9D%B8%E2%80%85%ED%8C%90%EB%A7%A4%E2%80%85%EB%8D%B0%EC%9D%B4%ED%84%B0%E2%80%85%ED%86%B5%ED%95%A9%ED%95%98%EA%B8%B0/%EC%98%A4%ED%94%84%EB%9D%BC%EC%9D%B8%EF%BC%8F%EC%98%A8%EB%9D%BC%EC%9D%B8%E2%80%85%ED%8C%90%EB%A7%A4%E2%80%85%EB%8D%B0%EC%9D%B4%ED%84%B0%E2%80%85%ED%86%B5%ED%95%A9%ED%95%98%EA%B8%B0.sql)  

