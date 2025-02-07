with open('../data/rosalind_fib.txt') as input_data :
    n, k = map(int, input_data.read().split())

def count_rabbit(n, k) :
    if n<3 :
        return 1 # 첫 두 달은 토끼 쌍이 1쌍밖에 없다.
    else :
        return count_rabbit(n-1, k) + k * count_rabbit(n-2, k)

print(count_rabbit(n, k))

    
