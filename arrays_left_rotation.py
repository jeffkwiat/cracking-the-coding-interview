# Find all permutations of s in b.

if __name__ == '__main__':
    s = 'xacxzaa'
    b = 'fxaazxacaaxzoecazxaxaz'

    permutations = get_permutations(s)
    for permutation in permutations:
        if permutation in b:
            print(permutation)