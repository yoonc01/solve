## JavaScript

### 1. 입력 받기 (클로저 활용)
클로저를 활용하여 입력을 받을 수 있습니다.

#### 예시 코드:
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%EB%B0%B1%EC%A4%80/Bronze/32905.%E2%80%85RACI/RACI.js)

---

## SQL

### 1. 특정 범위의 값 가져오기
`BETWEEN a AND b`를 사용하여 특정 범위 내의 값을 조회할 수 있습니다.

#### 예시 코드:
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/1/131535.%E2%80%85%EC%A1%B0%EA%B1%B4%EC%97%90%E2%80%85%EB%A7%9E%EB%8A%94%E2%80%85%ED%9A%8C%EC%9B%90%EC%88%98%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0/%EC%A1%B0%EA%B1%B4%EC%97%90%E2%80%85%EB%A7%9E%EB%8A%94%E2%80%85%ED%9A%8C%EC%9B%90%EC%88%98%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0.sql)

---

### 2. 특정 문자열 검색
`LIKE` 연산자를 사용하여 특정 문자열이 포함된 데이터를 검색할 수 있습니다.
- `%` : 0개 이상의 문자를 의미
- `_` : 정확히 한 개의 문자를 의미

#### 예시 코드:
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/1/131112.%E2%80%85%EA%B0%95%EC%9B%90%EB%8F%84%EC%97%90%E2%80%85%EC%9C%84%EC%B9%98%ED%95%9C%E2%80%85%EC%83%9D%EC%82%B0%EA%B3%B5%EC%9E%A5%E2%80%85%EB%AA%A9%EB%A1%9D%E2%80%85%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0/%EA%B0%95%EC%9B%90%EB%8F%84%EC%97%90%E2%80%85%EC%9C%84%EC%B9%98%ED%95%9C%E2%80%85%EC%83%9D%EC%82%B0%EA%B3%B5%EC%9E%A5%E2%80%85%EB%AA%A9%EB%A1%9D%E2%80%85%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0.sql)

---

### 3. NULL 값 처리
`IFNULL(COL, '대체')`를 사용하여 NULL 값을 다른 값으로 대체할 수 있습니다.

#### 예시 코드:
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/1/132201.%E2%80%8512%EC%84%B8%E2%80%85%EC%9D%B4%ED%95%98%EC%9D%B8%E2%80%85%EC%97%AC%EC%9E%90%E2%80%85%ED%99%98%EC%9E%90%E2%80%85%EB%AA%A9%EB%A1%9D%E2%80%85%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0/12%EC%84%B8%E2%80%85%EC%9D%B4%ED%95%98%EC%9D%B8%E2%80%85%EC%97%AC%EC%9E%90%E2%80%85%ED%99%98%EC%9E%90%E2%80%85%EB%AA%A9%EB%A1%9D%E2%80%85%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0.sql)

---

### 4. 날짜 포맷 변경
`DATE_FORMAT(HIRE_YMD, '%Y-%m-%d')`를 사용하여 날짜를 원하는 포맷으로 변환할 수 있습니다.

#### 예시 코드:
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/1/132203.%E2%80%85%ED%9D%89%EB%B6%80%EC%99%B8%EA%B3%BC%E2%80%85%EB%98%90%EB%8A%94%E2%80%85%EC%9D%BC%EB%B0%98%EC%99%B8%EA%B3%BC%E2%80%85%EC%9D%98%EC%82%AC%E2%80%85%EB%AA%A9%EB%A1%9D%E2%80%85%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0/%ED%9D%89%EB%B6%80%EC%99%B8%EA%B3%BC%E2%80%85%EB%98%90%EB%8A%94%E2%80%85%EC%9D%BC%EB%B0%98%EC%99%B8%EA%B3%BC%E2%80%85%EC%9D%98%EC%82%AC%E2%80%85%EB%AA%A9%EB%A1%9D%E2%80%85%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0.sql)

---

### 5. 특정 개수만큼 데이터 가져오기
- `LIMIT n` : 상위 `n`개 데이터를 가져옴
- `LIMIT n OFFSET offset` : `offset`부터 `n`개 가져옴

#### 예시 코드:
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/1/59405.%E2%80%85%EC%83%81%EC%9C%84%E2%80%85n%EA%B0%9C%E2%80%85%EB%A0%88%EC%BD%94%EB%93%9C/%EC%83%81%EC%9C%84%E2%80%85n%EA%B0%9C%E2%80%85%EB%A0%88%EC%BD%94%EB%93%9C.sql)

---

### 6. 특정 열에 특정 문자열 포함 여부 확인  
`IN` 연산자를 사용하여 특정 열이 특정 값을 포함하는지 확인할 수 있습니다.  

#### 예시 코드:  
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/1/276013.%E2%80%85Python%E2%80%85%EA%B0%9C%EB%B0%9C%EC%9E%90%E2%80%85%EC%B0%BE%EA%B8%B0/Python%E2%80%85%EA%B0%9C%EB%B0%9C%EC%9E%90%E2%80%85%EC%B0%BE%EA%B8%B0.sql)

---

### 7. NULL 값 필터링 (`IS NULL` / `IS NOT NULL`)  
NULL 값을 찾거나 제외할 때 `IS NULL` 또는 `IS NOT NULL`을 사용할 수 있습니다.  

- `IS NULL` : 해당 열이 `NULL`인 데이터만 조회  
- `IS NOT NULL` : 해당 열이 `NULL이 아닌 값`을 가진 데이터 조회  

#### 예시 코드:  
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/1/293258.%E2%80%85%EC%9E%94%EC%B1%99%EC%9D%B4%E2%80%85%EC%9E%A1%EC%9D%80%E2%80%85%EC%88%98%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0/%EC%9E%94%EC%B1%99%EC%9D%B4%E2%80%85%EC%9E%A1%EC%9D%80%E2%80%85%EC%88%98%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0.sql)

---

### 8. SQL에서 자주 쓰이는 연산 함수  
SQL에서는 데이터를 가공하고 분석할 때 **다양한 연산 함수**를 사용할 수 있습니다.  

#### ✅ **NULL 값 처리 연산 (`COALESCE`, `IFNULL`)**  
- `COALESCE(x, y, ...)` : **NULL이 아닌 첫 번째 값** 반환  
- `IFNULL(x, y)` : **MySQL 전용, NULL이면 대체 값 반환**  

```sql
SELECT COALESCE(NULL, NULL, 'Python', 'SQL'); -- 결과: 'Python'
SELECT IFNULL(SALARY, 0) FROM EMPLOYEES; -- MySQL 전용
```

#### ✅ **수학 연산 (`ROUND`, `CEIL`, `FLOOR`, `MOD`)**  
- `ROUND(x, n)` : 소수점 `n`자리 반올림  
- `CEIL(x)`, `FLOOR(x)` : 올림 / 내림  
- `MOD(x, y)` : 나머지 연산  

```sql
SELECT ROUND(3.14159, 2); -- 결과: 3.14
SELECT CEIL(2.1), FLOOR(2.9); -- 결과: 3, 2
SELECT MOD(10, 3); -- 결과: 1
```

#### ✅ **조건 연산 (`CASE`)**  
- 특정 조건에 따라 **다른 값 반환**  

```sql
SELECT ID, 
       CASE WHEN AGE < 18 THEN '미성년자'
            WHEN AGE >= 18 AND AGE < 60 THEN '성인'
            ELSE '노인' 
       END AS AGE_GROUP
FROM USERS;
```

#### ✅ **문자열 연산 (`CONCAT`, `SUBSTRING`, `REPLACE`)**  
- `CONCAT(x, y, ...)` : 문자열 연결  
- `SUBSTRING(x, start, len)` : 부분 문자열 추출  
- `REPLACE(x, old, new)` : 특정 문자열 변경  

```sql
SELECT CONCAT('Hello', ' ', 'World'); -- 결과: 'Hello World'
SELECT SUBSTRING('Database', 1, 4); -- 결과: 'Data'
SELECT REPLACE('I love Python', 'Python', 'SQL'); -- 결과: 'I love SQL'
```

#### ✅ **날짜 연산 (`DATE_ADD`, `DATEDIFF`)**  
- `DATE_ADD(x, INTERVAL y DAY)` : 날짜 더하기  
- `DATEDIFF(x, y)` : 두 날짜 차이 계산  

```sql
SELECT DATE_ADD('2024-02-18', INTERVAL 10 DAY); -- 결과: '2024-02-28'
SELECT DATEDIFF('2025-01-01', '2024-12-25'); -- 결과: 7
```

#### ✅ **비트 연산 (`&`, `|`, `^`)**  
- `&` (AND), `|` (OR), `^` (XOR) 사용 가능  

```sql
SELECT 5 & 3, 5 | 3, 5 ^ 3; -- 결과: 1, 7, 6
```

#### 예시 코드:  
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/1/293259.%E2%80%85%EC%9E%A1%EC%9D%80%E2%80%85%EB%AC%BC%EA%B3%A0%EA%B8%B0%EC%9D%98%E2%80%85%ED%8F%89%EA%B7%A0%E2%80%85%EA%B8%B8%EC%9D%B4%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0/%EC%9E%A1%EC%9D%80%E2%80%85%EB%AC%BC%EA%B3%A0%EA%B8%B0%EC%9D%98%E2%80%85%ED%8F%89%EA%B7%A0%E2%80%85%EA%B8%B8%EC%9D%B4%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0.sql)

---
