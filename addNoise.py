import wave
import numpy as np
import pylab as plt
import os
import glob

# 添加噪声函数
def Add_noise(s, n, SNR):
    P_s = np.mean(abs(s))
    P_n = np.mean(abs(n))
    fac = P_s/(10**(SNR/20))
    noise = n/P_n*fac
    noise_signal = s+noise
    return noise_signal

# 读取文件
def getData(wav, frames):
    data = wav.readframes(frames)
    data = np.fromstring(data, dtype=np.short)
    return data

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

path1 = 'TIMIT/TEST/DR2'    # 纯净语音文件目录
SNRs = [-5, 0, 5, 10, 15]
files = os.listdir(path1)      
print('pure filepath:\n',files)

noisefile = 'NOISEX-92 8KHz/white_8000.wav'
print('noise file:\n',noisefile)
noise_wav = wave.open(noisefile, 'rb')
params2 = noise_wav.getparams()
nchannels2, sampwidth2, framerate2, nframes2 = params2[:4]
print('噪声语音：', noisefile, params2)
noise_data = getData(noise_wav, nframes2)

count = 0
for file in files[:10]:
    path_n = os.path.join(path1, file)  
    path_ns = path_n+ "/" + "*_N.WAV"
    print(path_ns)

    purefiles = glob.glob(path_ns)

    for purefile in purefiles:
        clean_wav = wave.open(purefile, 'rb')
        params = clean_wav.getparams()
        nchannels, sampwidth, framerate, nframes = params[:4]
        print(purefile,": ", params)
        clean_data = getData(clean_wav,nframes)
        pure_filepath = "pure" + "/"
        pure_file = file + "_"+ purefile.split('/')[-1].split('_N')[0] + ".wav"
        pure_filename = pure_filepath + pure_file
        writeData(pure_filename,clean_data,params)
        # 每个纯净语音添加5种噪音
        for SNR in SNRs:
            noisy_filepath = "noisy" + "/" 
            noisy_file= file + "SNR_" + str(SNR) + purefile.split('/')[-1].split('_N')[0] + ".wav"
            noisy_filename = noisy_filepath + noisy_file
            noisy = Add_noise(clean_data,noise_data[:nframes],SNR)
            writeData(noisy_filename,noisy,params)
        
            count = count + 1
        clean_wav.close()

            # if count==100:
            #     pass
                # time = np.arange(0, nframes)*(1.0/framerate)
                # plt.subplot(311)
                # plt.plot(time, clean_data)
                # plt.ylabel('pure sound')
                # plt.subplot(312)
                # plt.plot(time, noise_data[:nframes])
                # plt.ylabel('babble noise')
                # plt.subplot(313)
                # plt.plot(time,noisy)
                # plt.ylabel('noisy sound')
                # plt.xlabel("time(seconds)")
                # plt.show()
            
# 计数君
print('有',count,'个加噪音语音')
            


        