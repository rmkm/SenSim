import sys
import base64

input_path = sys.argv[1]
output_path = sys.argv[2]

with open(input_path, 'rt') as f:
    dec_binary = base64.b64decode(f.read())

with open(output_path, 'wb') as f:
    f.write(dec_binary)
