from reedsolo import RSCodec

def reed_solomon_encoder(text_data:bytearray,ecc_symbols:int)-> str:
    '''Reed-Solomon encoder with the specified number of error correction symbols (ecc_symbols)'''
    
    #Encoding the data
    rs = RSCodec(ecc_symbols)
    encoded_byte_data = rs.encode(text_data)
    
    #Converting bytearray to Binary String
    encoded_binary_data = []
    
    for byte in encoded_byte_data:
        encoded_binary_data.append(format(byte,'016b'))
    
    #print((encoded_binary_data),"before join")
    encoded_binary_data = ''.join(encoded_binary_data)
    
    return encoded_binary_data

'''Example  
with open("Source_Data.txt","rb") as file :
    text_data_source = file.read()

encoded_binary_data,ecc_symbols = reed_solomon_encoder(text_data_source)

print("Original Data:", len(text_data_source))
print("Encoded Binary Data:", ecc_symbols)

#'''


