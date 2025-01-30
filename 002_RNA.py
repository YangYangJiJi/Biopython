"""
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u
"""

with open('data/rosalind_rna.txt') as input_data:
    dna = input_data.read().strip()

with open('output/002_RNA.txt', 'w') as output_data:
    output_data.write(dna.replace('T', 'U'))
    print (dna.replace('T', 'U'))

"""
'w' 모드는 파일이 없으면 새로 생성하고,
있으면 기존 내용을 덮어씁니다.
즉, Python 코드를 실행하면 002_RNA.txt가 자동으로 만들어짐!
파일이 이미 존재해도 실행할 때마다 덮어쓰기(overwrite) 됨.
"""    
