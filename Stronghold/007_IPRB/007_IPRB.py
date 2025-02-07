# k homozygous dominant
# m heterozygous recessive
# n homozygous recessive
with open('../data/rosalind_iprb.txt') as input_data :
    k, m, n = map(int, input_data.read().strip().split())

def prob_dominant(k,m,n):
    t = k + m + n #전체 개체 수
    total_pairs = t * (t -1) #두 개를 뽑는 경우의 수 

    #각 조합이 뽑힐 확률
    prob_AA_AA = (k/t) * ((k-1)/(t-1)) #AA x AA
    prob_AA_Aa = (k/t) * (m/(t-1)) + (m/t) * (k/(t-1)) #AA x Aa (순서 바뀐 경우도 고려)
    prob_AA_aa = (k/t) * (n/(t-1)) + (n/t) * (k/(t-1)) #AA x aa (순서 바뀐 경우도 고려)
    prob_Aa_Aa = (m/t) * ((m-1)/(t-1)) #Aa x Aa
    prob_Aa_aa = (m/t) * (n/(t-1)) + (n/t) * (m/(t-1)) # Aa x aa (순서 바뀐 경우도 고려)

    # 각 조합에서 우성 표현형이 나올 확률 곱하기
    dominant_prob = (
        prob_AA_AA * 1.0 + #100% 우성
        prob_AA_Aa * 1.0 + #100% 우성
        prob_AA_aa * 1.0 + #100% 우성
        prob_Aa_Aa * 0.75 + #75% 우성
        prob_Aa_aa * 0.5 #50% 우성
    )

    # 소수점 다섯째 자리까지 반올림하여 반환
    return round(dominant_prob, 5)

print(prob_dominant(k,m,n))

# input : 27 21 15
# output : 0.83871