"""
- FASTA 형식의 데이터를 읽어서 ID와 서열을 저장
- 각 서열에 대해 마지막 3개 염기서열을 추출
- 모든 서열과 비교하면서 다른 서열의 처음 3개 염기서열과 일치하는지 확인
- 일치하면 방향성 간선(s → t)을 인접 리스트 형식으로 출력
"""

# fasta 서열 읽기
def read_fasta():
    sequences = {}
    with open('../data/rosalind_grph.txt', 'r') as file:
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


#overlap graph에서 edge 찾기.
def find_overlap_graph(sequences, k=3):
    adjacency_list = []

    seq_items = list(sequences.items()) #(ID, 서열)형태 리스트로 변환


    #이중 반복문을 사용해 모든 서열을 비교
    for i , (id1, seq1) in enumerate(seq_items) :
        suffix = seq1[-k:] #마지막 k글자

        for j, (id2, seq2) in enumerate(seq_items) :
            if i !=j : #자기 자신과 비교하지 않음
                prefix = seq2[:k] #처음 k글자 (prefix)

                #두 서열의 접미사와 접두사가 같다면 엣지를 추가
                if suffix == prefix : #overlap 조건 충족
                    adjacency_list.append((id1, id2))
    return adjacency_list

    
fasta_data = read_fasta()
overlap_graph = find_overlap_graph(fasta_data, k=3)

'''
for edge in overlap_graph :
    print(edge[0], edge[1])
'''

with open('../output/012_GRPH.txt','w') as output_data :
    for edge in overlap_graph :
        print(edge[0], edge[1])
        output_data.write(edge[0] + " " + edge[1] + "\n")



