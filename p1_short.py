def component_wise_or(a, b):
    c = str()
    for i in range(len(a)):
        c += (str(int(a[i]) | int(b[i])))

    return c


N = int(input("n: "))
ARR1 = list(map(int, input("arr1: ")[1:-1].split(',')))
ARR2 = list(map(int, input("arr2: ")[1:-1].split(',')))

for i in range(N):
    a1 = ARR1[i]
    a2 = ARR2[i]
    bin_a1 = bin(a1)[2:].zfill(N)
    bin_a2 = bin(a2)[2:].zfill(N)
    bin_a3 = component_wise_or(bin_a1, bin_a2)
    print(bin_a3.replace('1', '#').replace('0', ' '))
