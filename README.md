# CryptographyEngineeringBenchmarks-
The provided code benchmarks the encryption performance of DES and AES algorithms using different block sizes and key sizes.

Encryption Algorithm Benchmark Results
--------------------------------------

1. DES, 64 bit block; AES-128, 128 bit block; AES-256, 256 bit block

- DES (64-bit block, 64-bit key): 20.184999999999786 μs
- AES-128 (128-bit block, 128-bit key): 17.734999999999832 μs
- AES-256 (256-bit block, 256-bit key): 18.905999999999924 μs

2. DES, 2x64 bit blocks; AES-128, 128 bit block; AES-256, 256 bit block

- DES (2x64-bit blocks, 64-bit key): 26.674999999999894 μs
- AES-128 (128-bit block, 128-bit key): 17.734999999999832 μs
- AES-256 (256-bit block, 256-bit key): 18.905999999999924 μs

3. DES, 4x64 bit blocks; AES-128, 2x128 bit blocks; AES-256, 256 bit block

- DES (4x64-bit blocks, 64-bit key): 24.520000000000095 μs
- AES-128 (2x128-bit blocks, 128-bit key): 16.988000000000003 μs
- AES-256 (256-bit block, 256-bit key): 18.905999999999924 μs

--------------------------------------
Summary:
- AES-128 consistently shows the fastest encryption times across all block sizes tested.
- DES performance varies with block size but is generally slower than AES-128 and AES-256.
- AES-256 provides a good balance of speed and security, though slightly slower than AES-128.

Note: These results are specific to the test environment and configurations used.


This was composed in 2020 for MSc in CS Security Engineering
