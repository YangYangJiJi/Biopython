# 004_Rabbits and Recurrence Relations 🐰
- rosalind id : FIB <br>

## 문제 이해

### 문제설명
- 변형된 피보나치 수열(Fibonacci sequence) 문제 <br>
- 일반적인 피보나치 수열과 다른점은 매월 새로운 새끼 토끼를 낳을 때, 한 쌍이 1쌍이 아닌 k쌍을 낳는다는 점이다. <br>
- 즉, 토끼의 번식 패턴을 시뮬레이션하는 문제 <br>

### 토끼 번식 규칙
1. 처음에는 토끼 한 쌍(2마리)이 있음. <br>
2. 토끼 한 쌍이 2개월이 지나야 번식 가능함. <br>
3. 번식 가능한 토끼 한 쌍은 매월 새끼를 k 쌍(= 2 × k 마리) 낳음. <br>
4. 새끼들은 다음 달이 되면 어른이 되고, 다다음 달부터 번식 가능. <br>

### 용어 정리
- "토끼 한 쌍" = 토끼 2마리 <br>
- "새끼 쌍" = 번식 가능한 토끼 한 쌍이 매월 낳는 "새로운 토끼 쌍의 개수" <br>
즉, 번식하는 토끼 한 쌍이 매월 새로운 토끼 k 쌍을 낳는다는 뜻. <br>
예를 들어, k=3이면 한 쌍이 3쌍(6마리)을 낳음. <br>

### 토끼 수를 계산하는 공식
- Fn = F(n-1) + k x F(n-2) <br>
- F(n-1) : 지난달의 토끼 쌍 수 (그대로 살아있음) <br>
- k x F(n-2) : 두 달 전의 토끼들이 낳은 새로운 토끼 쌍 수 <br>

### 예제 쉽게 풀이 
input : 5 3 <br>
- 5개월 후의 총 토끼 쌍 수를 구해야 함. <br>
- 한 쌍의 토끼는 매월 3쌍(6마리)의 새끼를 낳음 <br>

| 달  | 기존 토끼 수 | 새끼(= k × 2달 전 토끼) | 총 토끼 쌍 |
|----|----------|----------------|---------|
| 1  | 1 쌍     | 0              | 1       |
| 2  | 1 쌍     | 0              | 1       |
| 3  | 1 쌍     | 3 × 1 = 3 쌍   | 4       |
| 4  | 4 쌍     | 3 × 1 = 3 쌍   | 7       |
| 5  | 7 쌍     | 3 × 4 = 12 쌍  | 19      |

**output: 19** (즉, 5개월 후 총 19쌍 = 38마리) <br>

### 해결방법
- Dynamic Programming (동적 계획법)을 사용하여 값을 순차적으로 계산 <br>
- Fn = F(n-1) + k x F(n-2) 를 이용하여 리스트(배열)로 저장하면서 값을 구함 <br>

### input, ouput 정리
입력 (n, k) <br>
- n (1 ≤ n ≤ 40): 개월 수 <br>
- k (1 ≤ k ≤ 5): 한 쌍의 토끼가 매월 낳는 새끼 쌍의 수 <br>
  
출력 <br>
- n개월 후의 총 토끼 쌍 수 <br>

***

## 파이썬 공부

### map() 메서드
map() : 반복 가능한(iterable) 데이터의 각 요소에 대해 특정 함수를 적용하고, 변환된 값을 반환하는 함수
  n, k = map(int, input().split())
- input() → 사용자 입력을 문자열로 받음
- .split() → 입력된 문자열을 공백을 기준으로 나누어 리스트로 변환
- map(int, ...) → 리스트의 각 요소를 int 타입으로 변환
- n, k = ... → 두 개의 정수를 각각 n, k 변수에 저장
<br>
<br>
<br>

## 코드 더 파고들기
- 각각의 `n` 값에서 `count_rabbit(n-1, k) + k * count_rabbit(n-2, k)`를 계산하는 과정을 더 집중적으로 작성해보겠다.
- 즉, 재귀 호출이 어떻게 이루어지는지 단계별로 추적해보겠다.

### 함수의 의미 정리
`
return count_rabbit(n-1, k) + k * count_rabbit(n-2, k)
`
- `count_rabbit(n-1, k)` → 지난달까지 살아있는 토끼 수
- `count_rabbit(n-2, k)` * k → 두 달 전에 태어난 토끼들이 이번 달에 새끼를 낳음
    - `count_rabbit(n-2, k)`: 두 달 전의 성체 토끼 수
    - `k * (두 달 전의 성체 토끼 수)`: 두 달 전에 태어난 토끼들이 매달 k 쌍씩 새끼를 낳음
<br>
<br>

- 아래부터는 n=5, k=3인 경우 함수 호출 과정이다.

### 1단계: `count_rabbit(5, 3)` 호출
`
count_rabbit(5, 3) = count_rabbit(4, 3) + 3 * count_rabbit(3, 3)
`
- `count_rabbit(4, 3)` → 지난달까지 살아 있는 토끼 수
- `3 * count_rabbit(3, 3)` → 두 달 전에 태어난 토끼들이 낳은 새끼 수

### 2단계: `count_rabbit(4, 3)`과 `count_rabbit(3, 3)` 계산
`count_rabbit(4, 3)` 계산:
`
count_rabbit(4, 3) = count_rabbit(3, 3) + 3 * count_rabbit(2, 3)
`
- `count_rabbit(3, 3)` → 3개월 차까지 살아 있는 토끼 수
- `3 * count_rabbit(2, 3)` → 두 달 전에 태어난 토끼들이 낳은 새끼 수  
<br>
`count_rabbit(3, 3)` 계산:
`
`count_rabbit(3, 3)` = `count_rabbit(2, 3)` + `3 * count_rabbit(1, 3)`
`
- `count_rabbit(2, 3) = 1` (첫 두 달은 기본적으로 1쌍)
- `count_rabbit(1, 3) = 1` (첫 두 달은 기본적으로 1쌍)
- `count_rabbit(3, 3) = 1 + 3 * 1 = 4`

### 3단계: `count_rabbit(4, 3)` 값 구하기
`
count_rabbit(4, 3) = count_rabbit(3, 3) + 3 * count_rabbit(2, 3)
`
- `count_rabbit(3, 3) = 4`  
- `count_rabbit(2, 3) = 1`  
`
count_rabbit(4, 3) = 4 + 3 * 1 = 7
`

###  4단계: `count_rabbit(5, 3)` 값 구하기
`
count_rabbit(5, 3) = count_rabbit(4, 3) + 3 * count_rabbit(3, 3)
`
- `count_rabbit(4, 3) = 7`  
- `count_rabbit(3, 3) = 4`  
`
count_rabbit(5, 3) = 7 + 3 * 4 = 7 + 12 = 19
`
- 최종 결과: `count_rabbit(5, 3) = 19`

