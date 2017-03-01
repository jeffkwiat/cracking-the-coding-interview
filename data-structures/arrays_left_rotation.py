# Find all permutations of s in b.
def array_left_rotation(a, n, k):
    return a[k:] + a[:k]

if __name__ == '__main__':
    n, k = map(int, input().strip().split(' '))
    a = list(map(int, input().strip().split(' ')))
    answer = array_left_rotation(a, n, k)
    print(*answer, sep='w ')