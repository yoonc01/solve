## ✅ **재귀 CTE란?**
SQL에서 **재귀(Common Table Expression, CTE)**는 **자기 자신을 반복 호출하여 계층적인 데이터를 탐색**하는 기법입니다.  
예를 들어, **트리 구조(부모-자식 관계)나 계층 구조를 분석할 때 사용**됩니다.

---

## ✅ **문제 분석**
우리는 대장균들의 세대를 구해야 해요.
- `PARENT_ID`가 **NULL**인 개체는 **1세대**입니다.
- `PARENT_ID`가 **1세대 개체의 `ID`**인 경우, **2세대**입니다.
- `PARENT_ID`가 **2세대 개체의 `ID`**인 경우, **3세대**입니다.
- **이런 방식으로 부모-자식 관계를 따라가며 세대를 계산해야 합니다.**  
  → 이런 구조에서는 **재귀 CTE**를 사용하면 편리합니다.

---

## ✅ **재귀 CTE 기본 구조**
재귀 CTE는 3부분으로 구성됩니다:

1. **기본 쿼리 (Anchor Query)**  
   - 재귀를 시작할 최초의 데이터를 찾습니다.  
   - 여기서는 `PARENT_ID IS NULL`인 개체(= 1세대)를 찾습니다.

2. **재귀 쿼리 (Recursive Query)**  
   - 기본 쿼리에서 얻은 결과를 기반으로 **부모-자식 관계를 따라가며 재귀적으로 데이터를 확장**합니다.  
   - 여기서는 **이전 세대 개체의 `ID`를 부모(`PARENT_ID`)로 가진 개체들을 찾아서 세대를 +1** 합니다.

3. **종료 조건**  
   - **재귀 쿼리는 데이터가 더 이상 확장되지 않으면 자동으로 종료**됩니다.  
   - 즉, 부모(`PARENT_ID`)가 존재하지 않는 개체가 없을 때 멈춥니다.

---

## ✅ **재귀 CTE로 세대 찾기**

```sql
WITH RECURSIVE GENERATION_DATA AS (
    -- 1️⃣ [기본 쿼리] 1세대 찾기 (부모가 없는 개체)
    SELECT ID, 1 AS GENERATION
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL

    UNION ALL

    -- 2️⃣ [재귀 쿼리] 이전 세대(GENERATION_DATA)의 ID를 PARENT_ID로 가지는 개체 찾기
    SELECT e.ID, g.GENERATION + 1
    FROM ECOLI_DATA e
    JOIN GENERATION_DATA g ON e.PARENT_ID = g.ID
)
-- 3️⃣ [출력] 세대별 자식이 없는 개체 수 집계
SELECT COUNT(g.ID) AS COUNT, g.GENERATION
FROM GENERATION_DATA g
LEFT JOIN ECOLI_DATA e ON g.ID = e.PARENT_ID  -- 자식이 없는 개체 찾기
WHERE e.PARENT_ID IS NULL  -- 자식이 없는 개체만 선택
GROUP BY g.GENERATION
ORDER BY g.GENERATION;
```

---

## ✅ **쿼리 동작 과정**
### 1️⃣ **기본 쿼리 실행** (`PARENT_ID IS NULL` → 1세대)
먼저 `PARENT_ID IS NULL`인 개체를 찾고, `GENERATION = 1`로 설정합니다.

| ID  | GENERATION |
|----|-----------|
| 1  | 1         |
| 2  | 1         |

---

### 2️⃣ **재귀 쿼리 실행 (2세대 찾기)**
- `1세대`의 `ID`를 `PARENT_ID`로 가지는 개체를 찾고, `GENERATION + 1`을 적용합니다.

| ID  | GENERATION |
|----|-----------|
| 3  | 2         |
| 4  | 2         |
| 5  | 2         |

---

### 3️⃣ **재귀 쿼리 실행 (3세대 찾기)**
- `2세대`의 `ID`를 `PARENT_ID`로 가지는 개체를 찾고, `GENERATION + 1`을 적용합니다.

| ID  | GENERATION |
|----|-----------|
| 6  | 3         |
| 7  | 3         |

---

### 4️⃣ **재귀 쿼리 실행 (4세대 찾기)**
- `3세대`의 `ID`를 `PARENT_ID`로 가지는 개체를 찾고, `GENERATION + 1`을 적용합니다.

| ID  | GENERATION |
|----|-----------|
| 8  | 4         |

---

### 5️⃣ **LEFT JOIN을 사용하여 자식이 없는 개체 찾기**
이제 `LEFT JOIN`을 사용하여 **자식이 없는 개체만 필터링**합니다.

| ID  | GENERATION |
|----|-----------|
| 1  | 1         |
| 3  | 2         |
| 5  | 2         |
| 7  | 3         |
| 8  | 4         |

---

### 6️⃣ **세대별 개체 수 집계**
마지막으로 `COUNT(*)`를 사용해 **세대별 자식이 없는 개체 수**를 구합니다.

| COUNT | GENERATION |
|-------|-----------|
| 1     | 1         |
| 2     | 2         |
| 1     | 3         |
| 1     | 4         |

---

## ✅ **결론**
1. **재귀 CTE**를 사용해서 각 개체의 **세대(GENERATION)**를 구했습니다.
2. **LEFT JOIN**을 사용해 **자식이 없는 개체만 필터링**했습니다.
3. **GROUP BY GENERATION**을 사용해 **세대별 자식이 없는 개체 수를 집계**했습니다.

---

## 🎯 **요약**
- **재귀 CTE (`WITH RECURSIVE`)**는 계층적인 관계(부모-자식)를 처리하는 데 유용합니다.
- `UNION ALL`을 사용하여 **반복적으로 데이터를 확장**합니다.
- `LEFT JOIN`을 이용하여 **자식이 없는 개체만 필터링**했습니다.
- `GROUP BY`로 세대별 개체 수를 **집계**했습니다.


# [level 5] 멸종위기의 대장균 찾기 - 301651 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/301651) 

### 성능 요약

메모리: undefined, 시간: 

### 구분

코딩테스트 연습 > SELECT

### 채점결과

합계: 100.0 / 100.0

### 제출 일자

2025년 02월 21일 22:22:53

### 문제 설명

<p>대장균들은 일정 주기로 분화하며, 분화를 시작한 개체를 부모 개체, 분화가 되어 나온 개체를 자식 개체라고 합니다.<br>
다음은 실험실에서 배양한 대장균들의 정보를 담은 <code>ECOLI_DATA</code> 테이블입니다. <code>ECOLI_DATA</code> 테이블의 구조는 다음과 같으며,  <code>ID</code>, <code>PARENT_ID</code>, <code>SIZE_OF_COLONY</code>, <code>DIFFERENTIATION_DATE</code>, <code>GENOTYPE</code> 은 각각 대장균 개체의 ID, 부모 개체의 ID, 개체의 크기, 분화되어 나온 날짜, 개체의 형질을 나타냅니다.</p>
<table class="table">
        <thead><tr>
<th>Column name</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead>
        <tbody><tr>
<td>ID</td>
<td>INTEGER</td>
<td>FALSE</td>
</tr>
<tr>
<td>PARENT_ID</td>
<td>INTEGER</td>
<td>TRUE</td>
</tr>
<tr>
<td>SIZE_OF_COLONY</td>
<td>INTEGER</td>
<td>FALSE</td>
</tr>
<tr>
<td>DIFFERENTIATION_DATE</td>
<td>DATE</td>
<td>FALSE</td>
</tr>
<tr>
<td>GENOTYPE</td>
<td>INTEGER</td>
<td>FALSE</td>
</tr>
</tbody>
      </table>
<p>최초의 대장균 개체의 <code>PARENT_ID</code> 는 NULL 값입니다.</p>

<hr>

<h5>문제</h5>

<p>각 세대별 자식이 없는 개체의 수(<code>COUNT</code>)와 세대(<code>GENERATION</code>)를 출력하는 SQL문을 작성해주세요. 이때 결과는 세대에 대해 오름차순 정렬해주세요. 단, 모든 세대에는 자식이 없는 개체가 적어도 1개체는 존재합니다.</p>

<hr>

<h5>예시</h5>

<p>예를 들어 <code>ECOLI_DATA</code> 테이블이 다음과 같다면</p>
<table class="table">
        <thead><tr>
<th>ID</th>
<th>PARENT_ID</th>
<th>SIZE_OF_COLONY</th>
<th>DIFFERENTIATION_DATE</th>
<th>GENOTYPE</th>
</tr>
</thead>
        <tbody><tr>
<td>1</td>
<td>NULL</td>
<td>10</td>
<td>2019/01/01</td>
<td>5</td>
</tr>
<tr>
<td>2</td>
<td>NULL</td>
<td>2</td>
<td>2019/01/01</td>
<td>3</td>
</tr>
<tr>
<td>3</td>
<td>2</td>
<td>100</td>
<td>2020/01/01</td>
<td>4</td>
</tr>
<tr>
<td>4</td>
<td>2</td>
<td>16</td>
<td>2020/01/01</td>
<td>4</td>
</tr>
<tr>
<td>5</td>
<td>2</td>
<td>17</td>
<td>2020/01/01</td>
<td>6</td>
</tr>
<tr>
<td>6</td>
<td>4</td>
<td>101</td>
<td>2021/01/01</td>
<td>22</td>
</tr>
<tr>
<td>7</td>
<td>4</td>
<td>101</td>
<td>2022/01/01</td>
<td>23</td>
</tr>
<tr>
<td>8</td>
<td>6</td>
<td>1</td>
<td>2022/01/01</td>
<td>27</td>
</tr>
</tbody>
      </table>
<p>각 세대별 대장균의 ID는 다음과 같습니다.</p>

<p>1 세대 : ID 1, ID 2<br>
2 세대 : ID 3, ID 4, ID 5<br>
3 세대 : ID 6, ID 7<br>
4 세대 : ID 8</p>

<p>이 때 각 세대별 자식이 없는 대장균의 ID는 다음과 같습니다.</p>

<p>1 세대 : ID 1<br>
2 세대 : ID 3, ID 5<br>
3 세대 : ID 7<br>
4 세대 : ID 8</p>

<p>따라서 결과를 세대에 대해 오름차순 정렬하면 다음과 같아야 합니다.</p>
<table class="table">
        <thead><tr>
<th>COUNT</th>
<th>GENERATION</th>
</tr>
</thead>
        <tbody><tr>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td>1</td>
<td>4</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
