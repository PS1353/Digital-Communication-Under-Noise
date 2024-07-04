
import numpy as np
import Reed_Solomon_Encoder as RSE
import Reed_Solomon_Decoder as RSD
import Modulation as MOD
import Demodulation as DEMOD
import matplotlib.pyplot as plt
import Channel

'''
enter the voice with microphone, read the file , encode and transmit it ,modulate it.
receive data , demolate , decode , play.
'''

#System Properties

bit_rate = 1000  # Bit rate in bits per second
c_freq = 2000  # Carrier frequency in Hertz
c_freq_2 = 6000  # Carrier frequency in Hertz
amp = 10  # Amplitude of the carrier signal
k = 100 # Samples per bit
SNR = 100 # Signal to Noise Ratio
ecc_symbols = 200 # No .of Error Correcting Code symbols for Reed Solomon Coding
mod_name = "ASK"
#'''
#'''

#'''Reading data

with open("source.txt","rb") as file :
    text_data_source = file.read()

#'''

#'''Reed Solomon Encoding and byte to binary conversion

encoded_binary_data = RSE.reed_solomon_encoder(text_data_source,ecc_symbols)
#'''

#'''Modulation #ASK #FSK # PSK

if mod_name == "ASK":
    t,line_code,carrier_signal,modulated_signal = MOD.modulation_ask(bit_rate,c_freq,amp,encoded_binary_data,k)
    MOD.plot_mod_ask(t,line_code,carrier_signal,modulated_signal)

elif mod_name == "FSK":
    t,line_code,carrier_signal,carrier_signal_2,modulated_signal = MOD.modulation_fsk(bit_rate,c_freq,c_freq_2,encoded_binary_data,k)
    MOD.plot_mod_fsk(t,line_code,carrier_signal,carrier_signal_2,modulated_signal)

elif mod_name == "PSK":
    t,line_code,carrier_signal,carrier_signal_2,modulated_signal = MOD.modulation_psk(bit_rate,c_freq,encoded_binary_data,k)
    MOD.plot_mod_psk(t,line_code,carrier_signal,carrier_signal_2,modulated_signal)
#'''

#'''Channel

transmitted_signal = Channel.awgn(modulated_signal,SNR)
Channel.plot_noise(t,modulated_signal,transmitted_signal)

#'''

#'''Demodulation  
if mod_name == "ASK":
    demodulated_line_code,demodulated_signal = DEMOD.demodulate_ask(t,transmitted_signal,k)
    DEMOD.plot_demod_ask(t,demodulated_line_code,transmitted_signal)

elif mod_name == "FSK":
    demodulated_line_code,demodulated_signal = DEMOD.demodulate_fsk(t,modulated_signal,k,c_freq,c_freq_2,bit_rate)
    DEMOD.plot_demod_fsk(t,demodulated_line_code,transmitted_signal)

elif mod_name == "PSK":
    demodulated_line_code,demodulated_signal = DEMOD.demodulate_psk(t,encoded_binary_data,modulated_signal,c_freq,k)
    DEMOD.plot_demod_psk(t,demodulated_line_code,transmitted_signal)
#'''

#'''Reed Solomon Decoding and binary to byte conversion
try:
    text_data_received= RSD.reed_solomon_decoder(demodulated_signal,ecc_symbols)
except Exception as e:
    print(f"Too many errors : {e}")
#print(len(text_data_received))

#print(F"Decoding data... Time Elapsed  = {elapsed_time} seconds")
#'''

#'''Writing data

with open("Received_Data.txt ","wb") as file :
     file.write(text_data_received)

print("Done")

#'''