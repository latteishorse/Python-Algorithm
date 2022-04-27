# 12813

A = int(input(), 2)
B = int(input(), 2)

MASK = pow(2, 100000) - 1

print(bin(A & B)[2:].zfill(100000))
print(bin(A | B)[2:].zfill(100000))
print(bin(A ^ B)[2:].zfill(100000))
print(bin(A ^ MASK)[2:].zfill(100000))
print(bin(B ^ MASK)[2:].zfill(100000))
