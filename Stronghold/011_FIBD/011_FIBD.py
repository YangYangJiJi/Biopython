#input_data : 80 18
with open('../data/rosalind_fibd.txt') as input_data :
    n, m = map(int, input_data.read().split())

#n (n개월 후의 총 토끼 수를 구해야 함)
#m (각 토끼는 m개월 후에 죽음)

# 너무 어려워요..
def mortal_rabbit(n, m):
    # DP 리스트를 생성 (각 월마다 연령별 토끼 개체 수를 저장)
    dp = [[0] * m for _ in range(n + 1)]
    
    # 첫 달에는 한 쌍의 토끼가 태어남
    # dp[i][j]는 i개월 차에서 j개월 된 토끼 수를 저장
    dp[1][0] = 1  #1개월 차에서 0개월 된 토끼 수가 1쌍이라는 뜻

    for i in range(2, n + 1):  # 2개월 차부터 계산 시작
        # 새끼를 낳는 토끼들은 (1개월 이상, m개월 미만)인 개체들
        newborn = sum(dp[i-1][1:m]) # 출산 가능한 토끼의 수 (1개월 이상)
        
        # 각 토끼들이 한 달씩 나이 먹음
        for j in range(1, m):
            # 이전 달의 j-1개월 토끼들이 j개월 차가 됨
            dp[i][j] = dp[i-1][j-1]  

        # 새로 태어난 토끼를 0개월째로 추가
        dp[i][0] = newborn

    # 마지막 달(n)에서 모든 나이의 토끼들을 합산하여 반환
    return sum(dp[n])

print(mortal_rabbit(n, m))
#답 : 23301260112637985