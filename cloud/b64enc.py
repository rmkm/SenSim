# -*- coding:utf-8 -*-import base64
import sys
import base64

input_path = sys.argv[1]
output_path = sys.argv[2]

with open(input_path, 'rb') as f:
    enc_txt = base64.b64encode(f.read())
    
with open(output_path, 'wb') as f:
    f.write(enc_txt)
