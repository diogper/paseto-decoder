# PASETO Token Decoder
This project provides a Python-based decoder for PASETO public tokens, capable of handling different versions (V1, V2, V3 and V4) of the PASETO format. It decodes PASETO tokens, extracts the payload, and prints a human-readable Payload with its Signature and Header.


## Instalation
```
git clone https://github.com/yourusername/paseto-token-decoder.git
cd paseto-token-decoder
```

## Usage
You can decode a PASETO token by running the script from the command line with the token passed as an argument.

```
python paseto-decoder.py v4.public.eyJ1c2VyIjoiYWxpY2UiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOiIyMDI1LTAzLTAzVDIzOjE3OjMwLjkyMFoifS-X7zXNNVRzgCA1bJEPOgrUE62VckpfdOOaWsu5KEg8axWCTc32Vvlr9CcS8z5y2oFHYKcnhRL6n81guHriKAg

[!] Decoding PASETO Token
[+] Header:      v4.public.
[+] Payload:     {"user":"alice","role":"admin","iat":"2025-03-03T23:17:30.920Z"}
[+] Signature:   b"/\x97\xef5\xcd5Ts\x80 5l\x91\x0f:\n\xd4\x13\xad\x95rJ_t\xe3\x9aZ\xcb\xb9(H<k\x15\x82M\xcd\xf6V\xf9k\xf4'\x12\xf3>r\xda\x81G`\xa7'\x85\x12\xfa\x9f\xcd`\xb8z\xe2(\x08"
```
