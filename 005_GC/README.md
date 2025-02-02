# 005_Computing GC Content
*Rosalind ID : GC

## 문제 이해 
### 문제 설명
- GC content란 : DNA 서열 속 염기인 G와 C의 비율
- the GC-content of "AGCTATAG" is 37.5%
- 아무래도 G는 C와, 그리고 C는 G와 상보적이기에, reverse complement of any DNA string has the same GC-content

### input, output
- input : FASTA 포맷
    - 꺽쇠(>) 다음에 나오는건 Rosalind_xxxx 형태로, ID를 뜻한다.
    - 그 아래 나오는건 최소 10 DNA strings

```
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
```

- output : 
    - 가장 GC content가 높은 DNA string의 ID와 
    - 그 GC content 비율
    *허용 오차범위는 0.001
```
Rosalind_0808
60.919540
```

### absolute error
- 컴퓨터는 소수점 이하 자릿수를 무한히 저장할 수 없기 때문에, 부동소수점 연산 시 오차가 발생할 수 있다.
- 그래서 Rosalind 문제에서는 0.001 이내의 절대 오차를 허용한다.
- 즉, 정답이 55.3333%일 때, 55.332, 55.333, 55.334 같이 0.001 이내로 차이나는 값은 모두 정답으로 인정한다는 뜻

### GC content로 생물을 빠르게 구별할 수 있다.
- 같은 종(species)의 개체들은 각기 다른 유전체(genome)를 가지고 있지만, 여전히 대부분의 DNA 서열을 공유하고 있다.
- 예를 들어, 인간 유전체(3.2억 개의 염기쌍) 중 99.9%는 거의 모든 인간이 공통적으로 가지는 부분이다.
- DNA는 **이중 가닥(double-stranded)**으로 이루어져 있으며, 구아닌(G)과 시토신(C)은 항상 동일한 양으로 존재한다는 점이 특징이다.
- 따라서, 어떤 DNA의 염기 빈도를 분석하여 데이터베이스와 비교하는 방법을 사용하면 그 생물의 정체를 빠르게 파악할 수 있다.
- 이를 위해 가장 많이 사용되는 지표가 바로 GC-content(구아닌과 시토신의 비율) 이다.
- 진핵생물(eukaryotes)의 GC 함량 ≈ 50%
- 원핵생물(prokaryotes)의 GC 함량 > 50% (대체로 더 높음)
- 유전체가 워낙 길기 때문에 작은 DNA 샘플만으로도 어떤 생물인지 식별 가능

## 파이썬 공부
### 코드에서 absolute error 고려하는 방법
1. 소수점 자리수 조절
    - 문제에서는 절대 오차 0.001을 허용하지만, 부동소수점 연산은 예상치 못한 미세한 오차를 발생시킬 수 있다. 
    - 따라서, 3자리만 반올림하면 일부 오차가 발생할 수도 있어서 6자리까지 유지하면 더 안전하다.
    - `round(gc_content, 3)` → 3번째 자리에서 반올림 (오차가 커질 가능성 있음)
    - `round(gc_content, 6)` → 6번째 자리까지 유지 후, 비교할 때 오차를 줄일 수 있음
    - 즉, 소수점 6자리까지 유지한 후, 출력할 때만 3자리로 포맷팅 `print(f"{gc_content:.3f}")` 하면 최적의 결과가 나온다!! 더 정확한 비교가 가능함.
2. 오차 범위 내에서 값 비교
    - `math.isclose()` 함수를 사용하면 abs(a - b) < 0.001을 자동으로 처리해준다.
    - 사용시 import math를 해야함.
    - `math.isclose(calculated_value, expected_value, abs_tol=0.001)`

### G와 C의 개수 구하기
- 문자열에서 `count('G')` + `count('C')`를 통해 구할 수 있음
- `GC% = (G 개수 + C 개수) / 전체 길이 × 100`

### 여러개의 DNA 서열을 저장하고 분석하기
- 딕셔너리 자료형인 `dict`를 활용하여 `{ID:GC 비율}` 형태로 저장하여 편리하게 분석가능.
- 즉 key가 ID, value가 GC비율
- 최대값 구할 때 `max()`쓰면 될 듯

*** 참고로 딕셔너리란? ***
- 딕셔너리는 리스트나 튜플처럼 순차적으로(sequential) 해당 요솟값을 구하지 않고 Key를 통해 Value를 얻는다는게 가장 큰 특징.
```{Key1: Value1, Key2: Value2, Key3: Value3, ...}```
```dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}```
-  각각의 요소는 Key: Value 형태로 이루어져 있고 쉼표(,)로 구분되어 있다.
*출처 : https://wikidocs.net/16

*** 딕셔너리 쌍 추가하기 ***
```
>>> a = {1: 'a'}
>>> a[2] = 'b'
>>> a
{1: 'a', 2: 'b'}
```
- {1: 'a'} 딕셔너리에 a[2] = 'b'와 같이 입력하면 딕셔너리 a에 Key와 Value가 각각 2와 'b'인 {2: 'b'} 딕셔너리 쌍이 추가된다.

*** 딕셔너리에서 key를 사용해 value 얻기 ***
```
>>> grade = {'pey': 10, 'julliet': 99}
>>> grade['pey']
10
>>> grade['julliet']
99
```
- 어떤 Key의 Value를 얻기 위해서는 '딕셔너리_변수_이름[Key]'를 사용

### Biopython 라이브러리의 Bio 패키지
- Bio 패키지를 이용해서 fasta파일 파싱하기.
- 파싱(Parsing)이란, 데이터를 특정한 형식에서 원하는 구조로 변환하는 과정을 의미
- 아래에서 FASTA 파일의 여러 서열(record)을 하나씩 Python 객체(seq_record)로 변환하는 과정이 파싱임.
- `pip install biopython`로 설치하고, 다음을 작성해서 fasta 파일을 파싱해보았다.

```
from Bio import SeqIO
for seq_record in SeqIO.parse("C:/Biopython/ROSALIND_BI_Stronghold/data/rosalind_test2.fasta", "fasta") :
    print(seq_record.id) #fasta ID
    print(repr(seq_record.seq)) #서열
    print(len(seq_record)) #길이
```
- 를 해보았더니 그 결과 다음이 출력되었다.
- 순서대로 fasta ID, 서열, 길이가 추출되었다.

```
Rosalind_6404
Seq('CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGC...AGG')
80
Rosalind_5959
Seq('CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGA...CGC')
84
Rosalind_0808
Seq('CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGC...AAT')
87
```


## 소감
- FASTA 파일의 형식을 이해하게 됨.
- 딕셔너리 형식에 대해 이해하게 됨.