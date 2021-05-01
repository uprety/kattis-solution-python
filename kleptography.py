# I have no idea how this works. But this is what I have done using trial and error and took days.


def int_to_chr(integer):
    return chr(integer + 97  )

def chr_to_int(character):
    return ord(character) - 97


n, m = map(int, input().split())
key = input()
ciphertext = input()


plainText = ''
r_key, r_ciphertext = key[::-1], ciphertext[::-1]

for i in range(m-n):
    ai = int_to_chr((chr_to_int(r_ciphertext[i]) - chr_to_int(r_key[i])) % 26)
    r_key += ai
    plainText += ai


print(plainText[::-1] + key)


