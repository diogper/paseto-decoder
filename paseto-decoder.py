import base64
import sys

V1_PUBLIC_BYTES = 256
V2_PUBLIC_BYTES = 64
V3_PUBLIC_BYTES = 96
V4_PUBLIC_BYTES = 64

def base64url_to_bytes(base64url_str):
    """Convert a Base64 URL encoded string to raw bytes."""
    # Base64 URL uses '-' and '_' instead of '+' and '/'
    base64url_str = base64url_str.replace('-', '+').replace('_', '/')
    # Pad to ensure it has proper padding
    padding_needed = len(base64url_str) % 4
    if padding_needed != 0:
        base64url_str += '=' * (4 - padding_needed)
    return base64.b64decode(base64url_str)

def bytes_to_base64url(byte_data):
    """Convert raw bytes to a Base64 URL encoded string."""
    # First, encode to Base64
    base64_str = base64.b64encode(byte_data).decode('utf-8')
    # Replace '+' with '-', and '/' with '_'
    base64url_str = base64_str.replace('+', '-').replace('/', '_')
    # Remove the padding '=' for Base64 URL encoding
    base64url_str = base64url_str.rstrip('=')
    return base64url_str

def decode_paseto_public_token(prefix, token, VX_BYTES):
    """Decode PASETO vX.public Token"""
    # Step 1: Decode from base64url to raw binary (bytes)
    payload = base64url_to_bytes(token)

    # Step 2: Split the payload:
    # The last 64 bytes are the signature (s)
    signature = payload[-VX_BYTES:]
    # The rest of the bytes before the signature are the message (m)
    message = payload[:-VX_BYTES].decode('utf-8')

    print_paseto_token(prefix, message, signature)
    

def print_paseto_token(prefix, message, signature):
    """Print decoded token."""
    print(f"[+] Header:      {prefix}")
    print(f"[+] Payload:     {message}")
    print(f"[+] Signature:   {signature}")

if __name__ == "__main__":
    # Check if the token is passed as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python paseto-decoder.py <public_paseto_token>")
        sys.exit(1)

    # The token is passed as the first argument
    token = sys.argv[1]

    try:
        print("\n[!] Decoding PASETO Token")
        # Step 1: Check if the token starts with 'v3.public.'
        if token.startswith('v1.public.'):
            decode_paseto_public_token('v1.public.', token[len('v1.public.'):], V1_PUBLIC_BYTES)
        elif token.startswith('v2.public.'):
            decode_paseto_public_token('v2.public.', token[len('v2.public.'):], V2_PUBLIC_BYTES)
        elif token.startswith('v3.public.'):
            decode_paseto_public_token('v3.public.', token[len('v3.public.'):], V3_PUBLIC_BYTES)
        elif token.startswith('v4.public.'):
            decode_paseto_public_token('v4.public.', token[len('v4.public.'):], V4_PUBLIC_BYTES)


    except Exception as e:
        print(f"Error: {e}")