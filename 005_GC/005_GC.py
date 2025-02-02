from Bio import SeqIO

gc_dic = {} #딕셔너리 선언 
for seq in SeqIO.parse("C:/Biopython/ROSALIND_BI_Stronghold/data/rosalind_gc.txt", "fasta") :
    gc_content = (seq.seq.count("G") + seq.seq.count("C")) / len(seq) * 100 #GC content 구하기
    gc_dic[seq.id] = gc_content #딕셔너리에 추가

highest_gc = max(gc_dic, key=gc_dic.get) #가장 큰 GC content가진 ID를 가진 변수

with open('../output/005_GC.txt', 'w') as output_data :
    output_data.write(f"{highest_gc}\n")  # ID 저장
    output_data.write(f"{round(gc_dic[highest_gc], 6)}\n")  # GC 비율 저장
    print(highest_gc)
    print(round(gc_dic[highest_gc],6))
