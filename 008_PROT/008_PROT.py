with open("../data/rosalind_prot.txt","r") as file :
    seq = file.read().strip()  #주의 : file은 파일 객체, seq변수가 문자열 


codon_list = [seq[i:i+3] for i in range(0, len(seq), 3)]


genetic_code = { 
    "F": ["UUU", "UUC"],
    "L": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"], 
    "S": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
    "Y": ["UAU", "UAC"],
    " ": ["UAA", "UAG", "UGA"],
    "C": ["UGU", "UGC"],
    "W": ["UGG"],
    "P": ["CCU", "CCC", "CCA", "CCG"],
    "H": ["CAU", "CAC"],
    "Q": ["CAA", "CAG"],
    "R": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
    "I": ["AUU", "AUC", "AUA"],
    "M": ["AUG"],
    "T": ["ACU", "ACC", "ACA", "ACG"],
    "N": ["AAU", "AAC"],
    "K": ["AAA", "AAG"],
    "V": ["GUU", "GUC", "GUA", "GUG"],
    "A": ["GCU", "GCC", "GCA", "GCG"],
    "D": ["GAU", "GAC"],
    "E": ["GAA", "GAG"],
    "G": ["GGU", "GGC", "GGA", "GGG"]
}


# 코돈을 키로 하는 딕셔너리 생성 (역방향 매핑)
codon_to_AA = {}
for AA, codons in genetic_code.items(): #(키,값) 쌍 가져오기
    for codon in codons: #코돈 리스트를 반복
        codon_to_AA[codon] = AA #코돈을 키로, 아미노산을 값으로 저장 

# 코돈을 아미노산으로 변환하는 함수
def translate(mRNA_codons, codon_table):
    protein = "" # 변환된 아미노산 서열을 저장할 문자열 
    for codon in mRNA_codons :
        if codon in codon_table : #현재 코돈이 코돈 테이블에 있는지 확인
            AA = codon_table[codon] #해당 코돈에 대응하는 아미노산 가져오기
            if AA == " ": #STOP 코돈이면 종료
                break
            protein += AA #번역된 아미노산을 protein 서열에 추가
    return protein #최종 변환된 단백질 서열 반환

protein_seq = translate(codon_list, codon_to_AA)

with open("../output/008_PROT.txt","w") as output_data :
    output_data.write(protein_seq)
    print(protein_seq)


# 코돈-아미노산 딕셔너리
# key는 아미노산, value는 코돈


