# Implementation of AES in Python


`key_expansion.py` - 128 bits key expansion/scheduling, 11 round keys / 44 round words

`aes_encrypt_pure` - 128-aes, one state

`sha256` - Secure Hash Algorithm 256 bits, supports >512 bits

`aes_decrypt.py` and `aes_encrypt.py` use the `PyCryptodome` package as a comparison. <br>
```python
from aes_utils import show_state, show_state_dec
from key_expansion import expand_key_128_bits
from aes_encrypt_pure import aes_128

input_block = [0x32, 0x43, 0xf6, 0xa8, 0x88, 0x5a, 0x30, 0x8d, 0x31, 0x31, 0x98, 0xa2, 0xe0, 0x37, 0x07, 0x34]
input_block = [[0x32, 0x43, 0xf6, 0xa8], [0x88, 0x5a, 0x30, 0x8d], [0x31, 0x31, 0x98, 0xa2], [0xe0, 0x37, 0x07, 0x34]]

# Key expansion
round_key_words = expand_key_128_bits(key)

# Block encryption
ciphertext = aes_128(input_block, key)

show_state(ciphertext, False)
show_state_dec(ciphertext)

# Hashing
print(f"sha-256 digest of 'SHA-256':\n{sha256('SHA-256')}")


```



```
  ┌column──major┐  ┌─── row-major ───┐
  │ 39 25 84 1d │  │ 57  37  132 29  │
  │ 02 dc 09 fb │  │  2  220  9  251 │
  │ dc 11 85 97 │  │ 220 17  133 151 │
  │ 19 6a 0b 32 │  │ 25  106 11  50  │
  └─────────────┘  └──── base10 ─────┘

  sha-256 digest of 'SHA-256': bbd07c4fc02c99b97124febf42c7b63b5011c0df28d409fbb486b5a9d2e615ea


```

### References
https://csrc.nist.gov/files/pubs/fips/197/final/docs/fips-197.pdf

https://en.wikipedia.org/wiki/Advanced_Encryption_Standard

https://en.wikipedia.org/wiki/AES_key_schedule

https://en.wikipedia.org/wiki/SHA-2
