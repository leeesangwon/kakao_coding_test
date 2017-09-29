def convert_input_to_proper_type(n, arr1, arr2):
    n = int(n)
    assert (arr1[0] == '[') & (arr1[-1] == ']')
    assert (arr2[0] == '[') & (arr2[-1] == ']')
    arr1 = list(map(int, ''.join(arr1[1:-1].split()).split(',')))
    arr2 = list(map(int, ''.join(arr2[1:-1].split()).split(',')))
    return n, arr1, arr2


def validate_input(arr, n):
    assert len(arr) == n, ("Size of array(%d) does not match n(%d)" % (len(arr), n))
    for a in arr:
        assert (a < 2**n) & (a >= 0), "Component of arrary is out of boundary"


def dec_to_bin_array(in_dec):
    return bin(in_dec)[2:]


def component_wise_or(a, b):
    assert len(a) == len(b), "Size of each input should be same"
    c = str()
    for i in range(len(a)):
        c += (str(int(a[i]) | int(b[i])))

    return c


N = input("n: ")
ARR1 = input("arr1: ")
ARR2 = input("arr2: ")

N, ARR1, ARR2 = convert_input_to_proper_type(N, ARR1, ARR2)

validate_input(ARR1, N)
validate_input(ARR2, N)

for i in range(N):
    a1 = ARR1[i]
    a2 = ARR2[i]
    bin_a1 = dec_to_bin_array(a1).zfill(N)
    bin_a2 = dec_to_bin_array(a2).zfill(N)
    bin_a3 = component_wise_or(bin_a1, bin_a2)
    print(bin_a3.replace('1', '#').replace('0', ' '))
