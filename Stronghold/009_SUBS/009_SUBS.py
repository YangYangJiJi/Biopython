with open('../data/rosalind_subs.txt') as input_data :
    lines = input_data.read().splitlines() # 줄 단위로 읽어 리스트로 반환
    seq = lines[0] #첫번재 줄을 seq에 저장
    motif = lines[1] #두번째 줄을 motif에 저장

def find_motif_id(dna_seq, dna_motif) :
    position = []
    for i in range(len(dna_seq)-len(dna_motif)+1) : #서열에서 어차피 맨 마지막 모티프만큼의 길이는 안봐도 되기에, 효율성을 위해 세는 길이를 뺌.
        if seq[i:i+len(dna_motif)] == dna_motif :
            position.append(i+1) #인덱스 값이 나옴. (파이썬은 0부터 세기에 1을 더함)
    #map을 이용해 리스트인 position을 string으로 변환.
            result = " ".join(map(str, position))
    return result

print(find_motif_id(seq, motif))

'''output : 
40 64 81 120 188 208 301 308 362 369 416 551 558 573 612 647 654 690 793 800 828 843 850 857'''

