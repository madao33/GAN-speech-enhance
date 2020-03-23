import wave
import numpy as np
import pylab as plt

clean_wav = wave.open('TIMIT/TEST/DR2/FDRD1/SA1_N.WAV', 'rb')
noise_wav = wave.open('NOISEX-92 8KHz/babble_8000.wav', 'rb')
# 读取格式信息
params = clean_wav.getparams()
print('纯净语音：', params)
nchannels, sampwidth, framerate, nframes = params[:4]

params2 = noise_wav.getparams()
print('噪音语音：', params2)
nchannels, sampwidth2, framrate2, nframws2 = params2[:4]

if nframes < nframws2:
    frames = nframes
else:
    frames = nframws2

# 读取波形数据
data1 = clean_wav.readframes(frames)
data2 = noise_wav.readframes(frames)
clean_wav.close()
noise_wav.close()

wave_data1 = np.fromstring(data1, dtype=np.short)
wave_data2 = np.fromstring(data2, dtype=np.short)


# 添加噪声函数
def Add_noise(s, n, SNR):
    P_s = np.mean(abs(s))
    P_n = np.mean(abs(n))
    fac = P_s/(10**(SNR/20))
    noise = n/P_n*fac
    noise_signal = s+noise
    return noise_signal


wave_data1 = wave_data1.T
wave_data2 = wave_data2.T
# wave_data1 = wave_data1/np.max(np.abs(wave_data1))/1.3
# wave_data2 = wave_data2/np.max(np.abs(wave_data2))/1.3
SNR = -5
wave_data3 = Add_noise(wave_data2,wave_data1,SNR)
time1 = np.arange(0, frames)*(1.0/framerate)
time2 = np.arange(0, frames)*(1.0/framrate2)

plt.subplot(311)
plt.plot(time1, wave_data1)
plt.ylabel('pure sound')
plt.subplot(312)
plt.plot(time2, wave_data2)
plt.ylabel('babble noise')
plt.subplot(313)
plt.plot(time1,wave_data3)
plt.ylabel('noisy sound')
plt.xlabel("time(seconds)")
plt.show()

# N = framerate
# start =0
# df = framerate/(N-1)
# freq = [df*n for n in range(0,N)]
# wave_data4 = wave_data1[start:start+N]
# c1 = np.fft.fft(wave_data1)*2/N
# c2 = np.fft.fft(wave_data2)*2/N
# c3 = np.fft.fft(wave_data3)*2/N
# d=(int)(len(c1)/2)
# plt.subplot(311)
# plt.plot(freq[:d-1],abs(c1[:d-1]),'r')
# plt.ylabel('pure sound')
# plt.subplot(312)
# plt.plot(freq[:d-1],abs(c2[:d-1]),'r')
# plt.ylabel('babble sound')
# plt.subplot(313)
# plt.plot(freq[:d-1],abs(c3[:d-1]),'r')
# plt.ylabel('noise')
# plt.xlabel("frequency(Hz)")
# plt.show()

# 保存文件
def writeData(filename, data, params):
    wav = wave.open(filename, 'wb')
    nchannels, sampwidth, framerate, nframes = params[:4]
    wav.setnchannels(nchannels)
    wav.setsampwidth(sampwidth)
    wav.setframerate(framerate)
    temp = np.array(data).astype(np.short)
    wav.writeframes(temp.tostring())
    wav.close()
# wave_data3 = wave_data2/np.max(np.abs(wave_data3))/1.3
writeData("noisyTest.wav", wave_data3, params)