# FASTA 형식의 데이터를 읽어서 각 서열의 ID와 서열을 dictionary로 저장하는 Python 코드

def read_fasta(file_path):
    sequences = {}
    with open(file_path, 'r') as file:
        current_id = None
        current_seq = []
        
        for line in file:
            line = line.strip()
            if line.startswith(">"):  # FASTA 헤더 (서열 ID)
                if current_id is not None:
                    sequences[current_id] = "".join(current_seq)  # 이전 서열 저장
                current_id = line[1:]  # '>' 제거 후 ID 저장
                current_seq = []  # 새로운 서열 초기화
            else:
                current_seq.append(line)  # 서열 데이터 추가
        
        if current_id is not None:  # 마지막 서열 저장 (파일 마지막 서열은 for loop에서 자동저장되지 않음)
            sequences[current_id] = "".join(current_seq)
    
    return sequences







# 사용 예시
file_path = "example.fasta"  # FASTA 파일 경로
fasta_data = read_fasta(file_path)
for seq_id, sequence in fasta_data.items():
    print(f"{seq_id}: {sequence}")


#input
"""
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
"""

#output
'''
Rosalind_0498: AAATAAA
Rosalind_2391: AAATTTT
'''

