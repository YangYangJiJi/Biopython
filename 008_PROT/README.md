# 008_Translating RNA into protein
*rosalind id : PROT

## 문제 이해
### 문제 설명
- RNA 코돈을 아미노산으로 번역하기.

### input, output data
- input data : mRNA 서열 (최대 10kbp)
`AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA`
- output data : mRNA로부터 번역된 아미노산 서열
`MAMAPRTEINSTRING`

### 핵심
- 코돈 표를 아미노산과 매칭
- mRNA서열을 3개씩 잘라서 인식시키기.

## 파이썬 공부

### strip()과 split() 차이
- strip() : 문자열 앞뒤의 공백 또는 특별한 문자 삭제
```
text = '####안녕####'
text = text.strip('#')
```
결과 : '안녕'
- split() : 문자열 내부에 있는 공백 또는 특별한 문자를 구분해서, 리스트 아이템으로 만듦.
```
text = '사과 배 포도 오렌지'
text = text.split()
```
결과 : ['사과', '배', '포도', '오렌지']
```
text[1]
```
결과 : 배

### 문자열 자르기 
- 변수[:x] // x번째까지만 잘라서 출력
- 변수[x:] // x번째부터 잘라서 출력
- 변수[x:y] // x번째부터 y번째까지만 출력
- 변수[:] // 복사 ( 원래 값 그대로 )

### 문자열 특정한 자리수로 나누기
```
string = "123456789"
result = [string[i:i+2] for i in range(0, len(string), 2)]
print(result)
```
결과 : ['12','34','56','78','9']

### codon_to_AA
- 코돈을 키, 아미노산을 값으로 하는 딕셔너리(codon_to_AA) 생성

### genetic_code.items()
- items()는 딕셔너리의 (키, 값) 쌍을 가져오는 역할
- items함수를 사용하면 딕셔너리의 값을 반복할때 키와 값을 접근하기가 매우 유용해짐.
- 보통 딕셔너리를 for key in dict: 형태로 순회하면 키(key)만 가져올 수 있음
- 하지만, .items()를 사용하면 키(아미노산)와 값(코돈 리스트)을 동시에 가져올 수 있음
- 이걸 활용하면 딕셔너리를 변형하거나 새로운 딕셔너리를 만들 때 유용

### def translate
- mRNA 코돈 리스트를 아미노산 서열로 변환하는 함수.
- Parameters:
    - mRNA_codons (list): 3개 염기로 이루어진 mRNA 코돈 리스트 (예: ["AUG", "GCC", "AUG"])
    - codon_table (dict): 코돈을 키로 하고, 아미노산을 값으로 하는 딕셔너리 (예: {"AUG": "M", "GCC": "A"})
- Returns:
    - str: 변환된 아미노산 서열 (STOP 코돈이 나오면 변환 중단)

### 레퍼런스
- https://com-king.tistory.com/29