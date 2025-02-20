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
