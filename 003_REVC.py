"""
problem title : Complementing a Strand of DNA
roslaind ID : REVC
rosalind # : 003
url : https://rosalind.info/problems/revc/


In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s,
then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Sample Dataset
AAAACCCGGT

Sample Output
ACCGGGTTTT


전략 : 일단 한번 뒤집고, 상보적으로 바꾸기
"""

with open('data/rosalind_revc.txt') as input_data:
    dna = input_data.read().strip()

original = "ATGC"
complement = "TACG"
reverse_dna = dna[::-1] #뒤집기
#상보적 염기로 바꾸기
reverse_complement_dna = reverse_dna.translate(str.maketrans(original, complement))

with open('output/003_REVC.txt','w') as output_data:
    output_data.write(reverse_complement_dna)
    print(reverse_complement_dna)


"""
★[::-1] 문자열 슬라이싱을 이용해서 파이썬 문자열 뒤집기
* 문자열[시작:끝:규칙]
* 규칙은 슬라이싱을 하는 규칙
    *1 (디폴트)이 들어가면 문자열을 앞에서부터 하나씩 잘라서 새로운 문자열 만듦
    *2가 들어가면 앞에서부터 한 칸씩 띄워서 2씩 잘라주어 새로운 문자열 만듦
     ([0], [2], [4] ..)
     *-1을 넣으면 뒤에서부터 잘라 문자열을 뒤집을 수 있음

★maketrans로 번역규칙 만들고, translate로 규칙에 맞게 번역하기.
"""
