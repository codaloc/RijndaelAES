from aes_utils import show_state, show_state_dec
from key_expansion import expand_key_128_bits
from aes_encrypt_pure import aes_128
from sha256 import sha256


key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]
input_block = [[0x32, 0x43, 0xf6, 0xa8], [0x88, 0x5a, 0x30, 0x8d], [0x31, 0x31, 0x98, 0xa2], [0xe0, 0x37, 0x07, 0x34]]
round_key_words = expand_key_128_bits(key)
ciphertext = aes_128(input_block, key)
show_state(ciphertext, False)
show_state_dec(ciphertext)
print(f"sha-256 digest of 'SHA-256':\n{sha256('SHA-256')}")