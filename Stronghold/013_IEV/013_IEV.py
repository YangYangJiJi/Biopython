with open ('../data/rosalind_iev.txt') as input :
    data = list(map(int, input.read().split()))

def expected_dominant_offspring(data):
    """
    주어진 유전자형 조합의 부모 쌍 개수를 입력받아,
    기대되는 우성 표현형 자손의 수를 반환하는 함수.
    """
    # 각 유전자형 조합이 우성 표현형을 가질 확률
    dominant_prob = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]

    # 기대값 계산 (각 부모 쌍 개수 × 2 × 우성 표현형 확률)
    expected_offspring = sum(2 * count * prob for count, prob in zip(data, dominant_prob))
    
    return expected_offspring


result = expected_dominant_offspring(data)
print(result)

# 결과
# 140857.5