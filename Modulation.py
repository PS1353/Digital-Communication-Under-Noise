import numpy as np
import matplotlib.pyplot as plt

def modulation_ask(bit_rate:int,carrier_frequency:int,amp:int,encoded_binary_data:list,k:int)-> list:
     
    #Time values
    t = np.linspace(0, len(encoded_binary_data)/bit_rate, len(encoded_binary_data)*k)

    #Initializing Binary Line Codde
    line_code = np.zeros_like(t)
    
    #Creating the carrier signal
    carrier_signal = np.sin(2*np.pi*carrier_frequency*t)
    
    #Creating Binary Line Code
    for i,bit in enumerate(encoded_binary_data):
        
        if bit == "1":
            line_code[i *k:(i + 1) *k] = 1
        else:
            line_code[i * k:(i + 1) * k] = 0
    
    #Modulating the signal
    modulated_signal = line_code*amp*carrier_signal

    return t,line_code,carrier_signal,modulated_signal

def plot_mod_ask(t,line_code,carrier_signal,modulated_signal):
    x = len(t)
    if x> 10000:
        x = x//4
             
    # Plotting the Binary Signal , Carrier and ASK-modulated signal
    plt.figure(figsize=(10, 6))

    plt.subplot(3, 1, 1)
    plt.plot(t[0:x], line_code[0:x])
    plt.title('Binary Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.xlim((0,0.026))

    # Plotting the Carrier Signal
    plt.subplot(3, 1, 2)
    plt.plot(t[0:x], carrier_signal[0:x])
    plt.title('Carrier Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.xlim((0,0.026))

    # Plotting the Modulated signal
    plt.subplot(3, 1, 3)
    plt.plot(t[0:x], modulated_signal[0:x])
    plt.title(F'ASK-Modulated Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.xlim((0,0.026))

    plt.tight_layout()
    plt.show()

def modulation_fsk(bit_rate:int,carrier_frequency:int,carrier_frequency_2:int,encoded_binary_data:list,k:int):
    
    #Time values
    t = np.linspace(0, len(encoded_binary_data)/bit_rate, len(encoded_binary_data)*k)

    # Initializing Binary Line Code
    line_code = np.zeros_like(t)
    
    # Creating the carrier signal
    carrier_signal = np.sin(2*np.pi*carrier_frequency*t)
    carrier_signal_2 = np.sin(2*np.pi*carrier_frequency_2*t)
    
    #Creating Binary Line Code
    for i,bit in enumerate(encoded_binary_data):
    
        if bit == "1":
            line_code[i * k:(i + 1) * k] = 1
        else:
            line_code[i * k:(i + 1) * k] = 0

    #Modulation the signal
    modulated_signal = np.zeros_like(t)

    for i, bit in enumerate(encoded_binary_data):
        if bit == '0':
            modulated_signal[i*k:(i + 1)*k] = np.sin(2*np.pi*carrier_frequency*t[i*k:(i + 1) *k])
        elif bit == '1':
            modulated_signal[i*k:(i + 1)*k] = np.sin(2*np.pi*carrier_frequency_2*t[i*k:(i + 1)*k])

    return t,line_code,carrier_signal,carrier_signal_2,modulated_signal

def plot_mod_fsk(t,line_code,carrier_signal,carrier_signal_2,modulated_signal):
    x = len(t)
    if x> 10000:
        x = x//4
    plt.figure(figsize=(10, 6))

    # Plotting the Carrier Signal
    plt.subplot(4, 1, 1)
    plt.plot(t[0:x], carrier_signal[0:x])
    plt.title('Carrier Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.xlim((0,0.026))

    plt.subplot(4, 1, 2)
    plt.plot(t[0:x], carrier_signal_2[0:x])
    plt.title('Carrier Signal 2')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.xlim((0,0.026))

    # Plotting the Binary Signal
    plt.subplot(4, 1, 3)
    plt.plot(t[0:x], line_code[0:x])
    plt.title('Binary Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.xlim((0,0.026))

    # Plotting the Modulated signal
    plt.subplot(4, 1, 4)
    plt.plot(t, modulated_signal)
    plt.title(F'FSK-Modulated Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.xlim((0,0.026))

    plt.tight_layout()
    plt.show()

def modulation_psk(bit_rate:int,carrier_frequency:int,encoded_binary_data:list,k:int):
    
    #Time values
    t = np.linspace(0, len(encoded_binary_data)/bit_rate, len(encoded_binary_data)*k)

    # Initializing Binary Line Code
    line_code = np.zeros_like(t)
    
    # Creating the carrier signal
    carrier_signal = np.sin(2*np.pi*carrier_frequency*t)
    carrier_signal_2 = np.cos(2*np.pi*carrier_frequency*t)
    
    #Creating Binary Line Code
    for i,bit in enumerate(encoded_binary_data):
    
        if bit == "1":
            line_code[i * k:(i + 1) * k] = 1
        else:
            line_code[i * k:(i + 1) * k] = 0

    #Modulation the signal
    modulated_signal = np.zeros_like(t)

    for i, bit in enumerate(encoded_binary_data):
        if bit == '0':
            modulated_signal[i*k:(i + 1)*k] = np.sin(2*np.pi*carrier_frequency*t[i*k:(i + 1) *k])
        elif bit == '1':
            modulated_signal[i*k:(i + 1)*k] = np.cos(2*np.pi*carrier_frequency*t[i*k:(i + 1)*k])

    return t,line_code,carrier_signal,carrier_signal_2,modulated_signal

def plot_mod_psk(t,line_code,carrier_signal,carrier_signal_2,modulated_signal):
    x = len(t)
    if x> 10000:
        x = x//4
    plt.figure(figsize=(10, 6))

    # Plotting the Carrier Signal
    plt.subplot(4, 1, 1)
    plt.plot(t[0:x], carrier_signal[0:x])
    plt.title('Carrier Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.xlim((0,0.026))

    plt.subplot(4, 1, 2)
    plt.plot(t[0:x], carrier_signal_2[0:x])
    plt.title('Carrier Signal 2')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.xlim((0,0.026))

    # Plotting the Binary Signal
    plt.subplot(4, 1, 3)
    plt.plot(t[0:x], line_code[0:x])
    plt.title('Binary Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.xlim((0,0.026))

    # Plotting the Modulated signal
    plt.subplot(4, 1, 4)
    plt.plot(t, modulated_signal)
    plt.title(F'PSK-Modulated Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.xlim((0,0.026))

    plt.tight_layout()
    plt.show()



'''Parameters
bit_rate = 1000 # Bit rate in bits per second
amplitude = 5  # Amplitude of the carrier signal
data = "10101010101010101010101010"  # Binary data to modulate
carrier_frequency_1 = 3000  # Frequency for binary '0'
carrier_frequency_2 = 4000  # Frequency for binary '1'
k = 100

#Example
t,line_code,carrier_signal,carrier_signal_2,modulated_signal = modulation_psk(bit_rate,carrier_frequency_1,data,k)
#plot_mod_ask(t,line_code,carrier_signal,modulated_signal)
plot_mod_psk(t,line_code,carrier_signal,carrier_signal_2,modulated_signal)
#'''
