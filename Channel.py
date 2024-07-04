import numpy as np
import matplotlib.pyplot as plt
import Modulation as MOD 
import Demodulation as DEMOD

def awgn(modulated_signal:str,SNR:int)-> list:

    # Calculate the noise power based on the SNR
    noise_power = 10**(-SNR / 10)

    noise = np.random.normal(0, np.sqrt(noise_power), len(modulated_signal))
    
    # Transmitted signal after passing through the AWGN channel
    transmitted_signal = modulated_signal + noise

    return transmitted_signal

def plot_noise(t,modulated_signal,transmitted_signal):
    x = len(t)
    if x> 10000:
        x = x//4
    plt.figure(figsize=(10, 6))

    #Plotting the Modulated Signal
    plt.subplot(2,1,1)
    plt.plot(t[0:x], modulated_signal[0:x])
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title(f"ASK - Modulated Signal ")
    plt.xlim((0,0.026))
    
    # Plot the transmitted signal
    plt.subplot(2,1,2)
    plt.plot(t[0:x], transmitted_signal[0:x])
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title("Transmitted Signal (AWGN Channel)")
    plt.xlim((0,0.026))
    
    plt.tight_layout()
    plt.grid(True)
    plt.show()


#Example usage:
'''Parameters
bit_rate = 1000 # Bit rate in bits per second
carrier_frequency = 5000  # Carrier frequency in Hertz
amplitude = 5  # Amplitude of the carrier signal
data = "10101010 10010101 10101010"  # Binary data to modulate
SNR = 10
mod_name = "ASK"
k = 100

#Example

#Modulation
t,line_code,carrier_signal,modulated_signal = MOD.modulation_ask(bit_rate,carrier_frequency,amplitude,data,k)
MOD.plot_mod_ask(t,line_code,carrier_signal,modulated_signal)

#Channel
transmitted_signal = awgn(modulated_signal,SNR)
plot_noise(t,modulated_signal,transmitted_signal)

#Demodulation
demodulated_line_code,demodulated_signal = DEMOD.demodulate_ask(t,modulated_signal,k)
DEMOD.plot_demod(t,demodulated_line_code,transmitted_signal)

#'''
