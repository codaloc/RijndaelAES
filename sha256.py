from aes_utils import bit_pad


def rotate_right(value, shift):
    value = ((value >> shift) | (value << (32 - shift))) & 0xFFFFFFFF
    return value


def schedule(padded_message):
    schedule_list = [[] for i in range(64)]

    for i in range(0, 64, 4):
        schedule_list[int(i/4)] = padded_message[i:i+4]
    schedule_ints = [int.from_bytes(x,byteorder="big") for x in schedule_list]

    for i in range(16,64):
        s0 = rotate_right(schedule_ints[i-15], 7) ^ rotate_right(schedule_ints[i-15], 18) ^ (schedule_ints[i-15] >> 3)
        s1 = rotate_right(schedule_ints[i-2], 17) ^ rotate_right(schedule_ints[i-2], 19) ^ (schedule_ints[i-2] >> 10)
        schedule_ints[i] = (schedule_ints[i-16] + s0 + schedule_ints[i-7] + s1) & 0xFFFFFFFF

    return schedule_ints


def majority(b1, b2, b3):
    return (b1 & b2) ^ (b1 & b3) ^ (b2 & b3)


def process_block(block, h0, h1, h2, h3, h4, h5, h6, h7):
    # first 32 bits of the fractional parts of the cube roots of the first 64 primes 2..311
    k = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]
    schedule_ints = schedule(block)

    a, b, c, d, e, f, g, h = h0, h1, h2, h3, h4, h5, h6, h7
    for j in range(64):
        S1 = (e >> 6 | e << 26) ^ (e >> 11 | e << 21) ^ (e >> 25 | e << 7)
        ch = (e & f) ^ ((~e) & g)
        temp1 = h + S1 + ch + k[j] + schedule_ints[j]
        S0 = (a >> 2 | a << 30) ^ (a >> 13 | a << 19) ^ (a >> 22 | a << 10)

        temp2 = S0 + majority(a,b,c)

        h = g
        g = f
        f = e
        e = (d + temp1) & 0xFFFFFFFF
        d = c
        c = b
        b = a
        a = (temp1 + temp2) & 0xFFFFFFFF

    h0 = (h0 + a) & 0xFFFFFFFF
    h1 = (h1 + b) & 0xFFFFFFFF
    h2 = (h2 + c) & 0xFFFFFFFF
    h3 = (h3 + d) & 0xFFFFFFFF
    h4 = (h4 + e) & 0xFFFFFFFF
    h5 = (h5 + f) & 0xFFFFFFFF
    h6 = (h6 + g) & 0xFFFFFFFF
    h7 = (h7 + h) & 0xFFFFFFFF

    return h0,h1,h2,h3,h4,h5,h6,h7


def sha256(message):
    # first 32 bits of the fractional parts of the square roots of the first 8 primes 2..19
    h0 = 0x6a09e667
    h1 = 0xbb67ae85
    h2 = 0x3c6ef372
    h3 = 0xa54ff53a
    h4 = 0x510e527f
    h5 = 0x9b05688c
    h6 = 0x1f83d9ab
    h7 = 0x5be0cd19

    encoded_message = message.encode()
    padded_message = bit_pad(encoded_message)
    # print(f"Number of blocks: {len(padded_message*8)/512}")

    for first_word_in_block in range(0, len(padded_message), 64):
       block = padded_message[first_word_in_block:first_word_in_block+64]
       h0, h1, h2, h3, h4, h5, h6, h7 = process_block(block, h0, h1, h2, h3, h4, h5, h6, h7)

    hash_value = '{:08x}{:08x}{:08x}{:08x}{:08x}{:08x}{:08x}{:08x}'.format(h0, h1, h2, h3, h4, h5, h6, h7)
    return hash_value

if __name__ == "__main__":
    message = "SHA-256"
    print("String to digest : ")
    print(message)
    print(sha256(message))

