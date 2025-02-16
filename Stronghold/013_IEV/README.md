# 013_Calculating Expected Offspring
*rosalind id : IEV

## 문제 이해
### 문제 이해
- 기대값(Expected Value) 개념을 사용하여 우성 표현형을 가질 것으로 예상되는 자손의 수를 계산해야함
- 일단 각 genotype을 가진 부모 쌍의 개수를 입력으로 받음
- 모든 부모 쌍은 각각 두 명의 자손을 낳음
- 주어진 유전자형 조합에서 우성 표현형을 가질 확률을 계산하여, 이를 이용해 기대값을 구함.

### input, output
**intput data**
- 여섯개의 정수가 주어지며, 각 정수는 해당 유전자형을 가진 부모 쌍의 수를 의미함.
- 유전자형 조합은 다음과 같다. : AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa
- 각 값은 최대 20,000까지 가능하며, 공백으로 구분됨
```
1 0 0 1 0 1
```
- 이 input 값은 다음과 같은 부모쌍의 개수를 의미함
    - AA-AA = 1쌍
    - AA-Aa = 0쌍
    - AA-aa = 0쌍
    - Aa-Aa = 1쌍
    - Aa-aa = 0쌍
    - aa-aa = 1쌍
**output data**
- 기대되는 우성 표현형을 가진 자손의 수를 출력
```
3.5
```
### 해결방법
1. 각 유전자형 조합에서 태어나는 자손이 우성 표현형을 가질 확률을 계산
2. 각 부모 쌍이 2명의 자손을 낳는다는 점을 고려하여 기대값을 구함
- 각 조합에서 자손이 우성 표현형을 가질 확률은 다음과 같음

| Genotype Pair | Probability of Dominant Phenotype |
|---------------|-----------------------------------|
| `AA-AA`      | 100% (`1.0`) |
| `AA-Aa`      | 100% (`1.0`) |
| `AA-aa`      | 100% (`1.0`) |
| `Aa-Aa`      | 75% (`0.75`) |
| `Aa-aa`      | 50% (`0.5`) |
| `aa-aa`      | 0% (`0.0`) |

3. 기댓값 공식
`E=(n1×2×1.0)+(n2×2×1.0)+(n3×2×1.0)+(n4×2×0.75)+(n5×2×0.5)+(n6×2×0.0)`  
여기서 ni는 각 유전자형 조합의 부모 쌍 개수이다.

### 풀이
- zip()을 활용하여 각 부모 쌍에 대해 2 × 개수 × 확률을 곱한 후 합산



## 파이썬 공부 

### zip() 함수
- zip() 함수는 여러 개의 iterable(리스트, 튜플 등)을 동시에 묶어주는 함수임.
- 같은 인덱스의 요소들을 튜플로 만들어 반환함.
```
a = [1, 2, 3]
b = ['a', 'b', 'c']
zipped = zip(a, b)
print(list(zipped))

# 결과
[(1, 'a'), (2, 'b'), (3, 'c')]
```
- 길이가 다른 iterable을 입력하면, 가장 짧은 길이에 맞춰짐.
- zip(*iterables) 형태로 사용하면 언패킹(unpacking) 기능을 수행할 수도 있음.
- 반복문과 함께 사용하면 두 개 이상의 리스트를 동시에 순회할 수 있음.
```
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

# 결과
Alice: 85
Bob: 90
Charlie: 78
```

### 한줄 for문
- 반복문을 간결하게 작성하는 방법
- 리스트, 딕셔너리, 셋 등을 만들 때 유용함.
- 기본구조 : `[표현식 for 변수 in iterable]`
- 리스트 생성
```
squares = [x**2 for x in range(5)]
print(squares)

#결과
[0, 1, 4, 9, 16]
```
- 조건문 포함
```
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

#결과
[0, 2, 4, 6, 8]
```
- 이중 반복문
```
pairs = [(x, y) for x in range(2) for y in range(3)]
print(pairs)

#결과
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
```
- 딕셔너리
```
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)

#결과
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```