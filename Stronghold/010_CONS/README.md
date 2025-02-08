# 010_Consensus and Profile 
*rosalind id : CONS

## 문제이해
### 문제 목표
- 10개의 DNA 서열에서 consensus sequence 구하기
- consensus sequence : 각 위치에서 가장 많이 등장한 염기로 구성된 서열
- profile matirx : A, C, G, T가 각 위치에서 몇 번 등장했는지 기록한 표

### input, output
**input data**
fasta 포맷의 10개의 DNA 서열
```
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
```
**output data**
consensus 서열과, 그 아래에는 각 서열별로 A, C, G, T가 몇개씩 있었는지를 matrix 형태로 나타냄.
```
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
```
*참고로 여러개의 가능한 consensus sequence가 있다면 그 중 아무거나 출력

### biology : 가장 가능성이 높은 공통 조상을 찾기
- "Point Mutation 개수 세기" 문제에서는 두 개의 동일한 길이의 DNA 서열 간 최소한의 불일치 개수를 계산하여, 진화 과정에서 두 상동 DNA 서열 사이에 발생한 최소한의 점 돌연변이 수를 모델링함.
- 그러나 여러 개의 **상동 서열(homologous strands)**을 동시에 분석하려는 경우, 자연스럽게 발생하는 문제는 주어진 서열들의 가장 가능성이 높은 공통 조상을 대표하는 평균적인 서열을 찾는 것이다.
- 즉 쉽게 말하면 서열들의 평균구해서 대표 서열 구하기!

## 코드
### FASTA 파일 읽기
- FASTA 파일에서 DNA 서열만 저장하는 코드 작성
- '>'로 시작하는 줄은 서열ID이므로 제외
- 서열만 dna_sequence 리스트에 저장

### 각 위치별 염기개수 세고, consensus 서열 구하기
- 2D 리스트를 만들어 각 위치에서 A, C, G, T 개수 저장
- 각 인덱스별로 염기개수 중 가장 큰 염기 선택


## 파이썬 공부
### 파이썬에서 괄호
- 소괄호() : 튜플, 함수, 연산자 우선순위에 사용
- 중괄호{} : 세트(Set), 딕셔너리(Dictionary), 집합 표현식에 사용
- 대괄호[] : 리스트(List), 문자열(String), 인덱싱, 슬라이싱 등에 사용


### 딕셔너리의 편리함
1. profile을 리스트로 만들었을 때 
```
profile = [ 
    [0] * dna_length, 
    [0] * dna_length,
    [0] * dna_length,
    [0] * dna_length
] 

for seq in dna_sequence:
    for i in range(dna_length):
        base = seq[i] 
        if base == 'A' :
            profile[0][i] += 1 #base가 A이면, 첫번째 칸에 채워라. 그리고 그 다음 열로 넘어가기 .
        elif base == 'C' :
            profile[1][i] += 1
        elif base == 'G' :
            profile[2][i] += 1
        elif base == 'T' :
            profile[3][i] += 1
```
이런식으로 염기를 if문으로 비교해야함.

2. profile을 딕셔너리로 만들었을 때 
```
profile = {
    'A' : [0] * dna_length, 
    'C' : [0] * dna_length,
    'G' : [0] * dna_length,
    'T' : [0] * dna_length
}

for sequence in dna_sequence:
    for i, base in enumerate(sequence):
        profile[base][i] += 1
```
base를 key로 비교하니까 더 간결해짐.

### enumerate(sequence)
- **enumerate(sequence)** : 리스트나 문자열 같은 반복 가능한(iterable) 객체를 순회하면서, 각 요소와 함께 해당 요소의 인덱스(index)도 제공하는 함수
- 기본동작
```
sequence = "ATGC"

for i, base in enumerate(sequence):
    print(f"Index: {i}, Base: {base}")
```
- 출력결과
```
Index: 0, Base: A
Index: 1, Base: T
Index: 2, Base: G
Index: 3, Base: C
```
- enumerate(sequence)는 sequence를 순회하면서,
    - i에는 **현재 문자의 위치(인덱스)**가 들어가고,
    - base에는 현재 문자가 들어감.
- 장점
    - 반복문에서 i(인덱스)와 값(base)을 동시에 가져올 수 있음!
    - range(len(sequence)) 같은 복잡한 코드 없이 깔끔하게 작성 가능

### profile matrix 출력 포맷 맞추기
```
for base in "ACGT" :
    print(f"{base} : {' '.join(map(str, profile[base]))}")
```
**profile[base]**
- base = "A"일 때, profile[base]는 [5, 1, 0, 0, 5, 5, 0, 0]
- base = "C"일 때, profile[base]는 [0, 0, 1, 4, 2, 0, 6, 1]
- 이런 방식으로 각 염기의 빈도수를 가져옴.
**' '.join(map(str, profile[base]))**
- 이 부분은 profile[base] 리스트를 문자열로 변환해서 출력하는 역할
- `map(str, profile[base])` : profile[base] 리스트의 모든 숫자를 문자열로 변환
- `' '.join(...)` : 리스트의 문자열 요소들을 공백 " "으로 연결