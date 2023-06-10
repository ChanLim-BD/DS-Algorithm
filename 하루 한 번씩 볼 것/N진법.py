def to_nbase(num, n):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mod_dict = {i: chars[i] for i in range(len(chars))}
    s = ""
    while num != 0:
        s = mod_dict[num%n] + s
        num //= n
    return s

def nbase_to_dec(num, n):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mod_dict = {chars[i]: i for i in range(len(chars))}
    digits = []
    for i, c in enumerate(num[::-1]):
        digits.append(mod_dict[c] * n**i)
    return sum(digits)

print("12 -> {}".format(to_nbase(12, 16)))
print("255 -> {}".format(to_nbase(255, 16)))

print(nbase_to_dec("142", 6))