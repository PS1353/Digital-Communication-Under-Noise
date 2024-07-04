import numpy as np
import matplotlib.pyplot as plt
import Modulation as MOD 

def demodulate_ask(t:list,received_signal:list,k:int)->list:
    
    demodulated_line_code =  np.zeros_like(t)
    for i,amp in enumerate(received_signal[3::k]):
            if amp>2:
                demodulated_line_code[i * k:(i + 1) * k]  = 1
            else:
                demodulated_line_code[i * k:(i + 1) * k]  = 0
    
    demodulated_signal = []

    for idx,bit in enumerate(demodulated_line_code[::k]):
         demodulated_signal.append(int(bit))
    
    return demodulated_line_code,demodulated_signal

def plot_demod_ask(t:list,demodulated_line_code:list,transmitted_signal:list) -> None:
    x = len(t)
    if x> 10000:
        x = x//4
    plt.figure(figsize=(10, 6))

    # Plotting the Transmitted signal
    plt.subplot(2, 1, 1)
    plt.plot(t[0:x], transmitted_signal[0:x])
    plt.title(F'Transmitted Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.xlim((0,0.026))
    
    # Plotting the Demodulated signal
    plt.subplot(2, 1, 2)
    plt.plot(t[0:x], demodulated_line_code[0:x])
    plt.title('Demodulated Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.xlim((0,0.026))

    plt.tight_layout()
    plt.grid(True)
    plt.show()

def demodulate_fsk(t:list,modulated_signal:list,k:int,carrier_frequency:int,carrier_frequency_2:int,bit_rate) -> list:
    
    demodulated_signal = []
    demodulated_line_code = np.zeros_like(t)

    for i in range(0, len(modulated_signal), k):
        # Extract a chunk of the modulated signal for a single bit
        chunk = modulated_signal[i:i + k]
        
        # Compute the FFT of the chunk
        fft_chunk = np.fft.fft(chunk)
        
        # Find the frequency component with the highest magnitude
        frequency_component_index = np.argmax(np.abs(fft_chunk))
        
        if frequency_component_index == 98:
            frequency_component_index = 2
        elif frequency_component_index == 94:
            frequency_component_index =6
        
        # Determine the bit based on the detected frequency component
        if frequency_component_index == int(carrier_frequency/bit_rate ):
            demodulated_signal.append(0)
        elif frequency_component_index == int(carrier_frequency_2/bit_rate):
            demodulated_signal.append(1)

        for i,bit in enumerate(demodulated_signal):
            if bit == 1:
                demodulated_line_code[i * k:(i + 1) * k] = 1
            else:
                demodulated_line_code[i * k:(i + 1) * k] = 0
    
    return demodulated_line_code,demodulated_signal

def plot_demod_fsk(t:list,demodulated_line_code:list,transmitted_signal:list) -> None:
    x = len(t)
    if x> 10000:
        x = x//4
    plt.figure(figsize=(10, 6))

    # Plotting the Transmitted signal
    plt.subplot(2, 1, 1)
    plt.plot(t[0:x], transmitted_signal[0:x])
    plt.title(F'Transmitted Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.xlim((0,0.026))
    
    # Plotting the Demodulated signal
    plt.subplot(2, 1, 2)
    plt.plot(t[0:x], demodulated_line_code[0:x])
    plt.title('Demodulated Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.xlim((0,0.026))

    plt.tight_layout()
    plt.grid(True)
    plt.show()

def demodulate_psk(t,encoded_binary_data,modulated_signal,carrier_frequency,k):
    
    line_code = np.zeros_like(t)
    carrier_signal = np.cos(2*np.pi*carrier_frequency*t)
    
    for i,bit in enumerate(encoded_binary_data):
        
        if bit == "1":
            line_code[i *k:(i + 1) *k] = 1
        else:
            line_code[i * k:(i + 1) * k] = 0
    
    reference_signal = line_code*carrier_signal
    detector_signal  = modulated_signal-reference_signal
    
    demodulated_line_code =  np.zeros_like(t)
    for i,amp in enumerate(detector_signal[3::k]):
            if amp>0.25:
                demodulated_line_code[i * k:(i + 1) * k]  = 0
            else:
                demodulated_line_code[i * k:(i + 1) * k]  = 1
    
    demodulated_signal = []

    for idx,bit in enumerate(demodulated_line_code[::k]):
         demodulated_signal.append(int(bit))
    
    return demodulated_line_code,demodulated_signal

def plot_demod_psk(t:list,demodulated_line_code:list,transmitted_signal:list) -> None:
    x = len(t)
    if x> 10000:
        x = x//4
    plt.figure(figsize=(10, 6))

    # Plotting the Transmitted signal
    plt.subplot(2, 1, 1)
    plt.plot(t[0:x], transmitted_signal[0:x])
    plt.title(F'Transmitted Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.xlim((0,0.026))
    
    # Plotting the Demodulated signal
    plt.subplot(2, 1, 2)
    plt.plot(t[0:x], demodulated_line_code[0:x])
    plt.title('Demodulated Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.xlim((0,0.026))

    plt.tight_layout()
    plt.grid(True)
    plt.show()


#Example usage:

'''Parameters
bit_rate = 1000 # Bit rate in bits per second
carrier_frequency = 2000  # Carrier frequency in Hertz
carrier_frequency_2 = 6000  # Carrier frequency in Hertz
amplitude = 5  # Amplitude of the carrier signal
data = "10101010101010101010101010"  # Binary data to modulate
k =100

#Example

#t,line_code,carrier_signal,modulated_signal = MOD.modulation_ask(bit_rate,carrier_frequency,amplitude,data,k)
#MOD.plot_mod_ask(t,line_code,carrier_signal,modulated_signal)

#demodulated_line_code,demodulated_signal = demodulate_ask(t,modulated_signal,k)
#plot_demod_ask(t,demodulated_line_code,modulated_signal)


t,line_code,carrier_signal,carrier_signal_2,modulated_signal,data = MOD.modulation_psk(bit_rate,carrier_frequency,data,k)
MOD.plot_mod_psk(t,line_code,carrier_signal,carrier_signal_2,modulated_signal)
#
#demodulated_line_code,demodulated_signal = demodulate_fsk(t,modulated_signal,k,carrier_frequency,carrier_frequency_2,bit_rate)
#plot_demod_fsk(t,demodulated_line_code,modulated_signal)

demodulated_line_code,demodulated_signal = demodulate_psk(t,data,modulated_signal,carrier_frequency)
plot_demod_psk(t,demodulated_line_code,modulated_signal)
#'''