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
