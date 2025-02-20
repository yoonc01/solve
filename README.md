## JavaScript

### 클로저를 활용해서 받은 입력 관리하기

#### 예시 코드:
[예제 코드 보기](https://github.com/yoonc01/solve/blob/main/%EB%B0%B1%EC%A4%80/Bronze/32905.%E2%80%85RACI/RACI.js)

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
