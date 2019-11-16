print("------------------------")
file = 'test.txt'
print("------------------------")
input("Tekan enter untuk melanjutkan.. (kembali ke menu sebelumnya)")
global a_, b_, j
line = []
a = []
b = []
with open(file, 'r') as r:
    for l in r:
        line.append(l)