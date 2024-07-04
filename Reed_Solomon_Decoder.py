from reedsolo import RSCodec
import Reed_Solomon_Encoder as RSE
import numpy as np


def reed_solomon_decoder(demodulated_signal:list,ecc_symbols:int) -> bytearray:
    '''Reed-Solomon decoder with the specified number of error correction symbols (ecc_symbol)'''
    
    #Converting list to Binary String
    encoded_binary_data = ''.join(map(str, demodulated_signal))
    
    # Initialize an empty list to store byte chunks
    byte_chunks = []

    #''' Split the binary string into 16-bit chunks (bytes)
    for i in range(0, len(encoded_binary_data), 16):
        chunk = encoded_binary_data[i:i + 16]
        byte_chunks.append(chunk)
    #'''

    # Initialize an empty bytearray to store the binary data    
    byte_data=[] 
    
    #'''Convert each 16-bit chunk to an integer and then to a byte
    for chunk in byte_chunks:
        byte_value = int(chunk, 2)
        byte_data.append(byte_value)
    #'''

    # Decoding the data
    rs = RSCodec(ecc_symbols)
    decoded_byte_data = rs.decode(byte_data)
    
    # decoded_data = array('i',decoded_byte_data[0])
    # original_data = ''.join(chr(i) for i in decoded_data)
    
    return decoded_byte_data[0]




'''Example
with open("Source_Data.txt","rb") as file :
    text_data_source = file.read()

encoded_byte_data,ecc_symbols, = encoder(text_data_source)
text_data_received = decoder(encoded_byte_data, ecc_symbols)

#print("Original Data:", text_data_source)
#print(encoded_byte_data)
#print("Decoded Data:", decoded_byte_data)

with open("Received_Data_4.txt ","wb") as file :
     file.write(text_data_received[0])

#'''