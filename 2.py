klub_a = input('Klub A: ')
klub_b = input('Klub B: ')
arr = []
i = 1

def pertandingan(arr):
    i = 1
    while True:
        a, b = map(int, (input('Pertandingan {} : '.format(i))).split())
        if a < 0 or b < 0:
            break
        elif a > b:
            arr.append(klub_a)
            i += 1
        elif a < b:
            arr.append(klub_b)
            i += 1
        else:
            arr.append('Draw')
            i += 1

pertandingan(arr)

for klub in arr:
    print(f'Hasil {i} :',klub)
    i += 1

print('Pertandingan selesai')
