import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np

#print first round
def printFirst():
  y, sr = librosa.load("applications/data/TUT-acoustic-scenes-2017-development/audio/a104_20_30.wav")
  print(sr)
  D = librosa.stft(y, n_fft=2048, win_length=int(sr*0.04), hop_length=int(sr*0.02),center=True, window="hamming")
  plt.subplot(211)
  librosa.display.specshow(librosa.amplitude_to_db(D,ref=np.max),y_axis='log', x_axis='time')
  plt.title('Power spectrogram: FFT=2048, Win/Hop 0.04/0.02')
  plt.colorbar(format='%+2.0f dB')
  plt.tight_layout()

  D = librosa.stft(y, n_fft=4096, win_length=int(sr*0.08), hop_length=int(sr*0.04),center=True, window="hamming")
  plt.subplot(212)
  librosa.display.specshow(librosa.amplitude_to_db(D,ref=np.max),y_axis='log', x_axis='time')
  plt.title('Power spectrogram: FFT=4096, Win/Hop 0.08/0.04')
  plt.colorbar(format='%+2.0f dB')
  plt.tight_layout()
  #D = librosa.stft(y, n_fft=4096, win_length=int(sr*0.08), hop_length=int(sr*0.04),center=True, window="hamming")
  #plt.subplot(213)
  #librosa.display.specshow(librosa.amplitude_to_db(D,ref=np.max),y_axis='log', x_axis='time')
  #plt.title('Power spectrogram: FFT=4096, Win/Hop 0.08/0.04')
  #plt.colorbar(format='%+2.0f dB')
  #plt.tight_layout()


  ## Print second round
  plt.show()

y, sr = librosa.load("applications/data/TUT-acoustic-scenes-2017-development/audio/a104_20_30.wav")
D = librosa.stft(y, n_fft=4096, win_length=int(sr*0.08), hop_length=int(sr*0.04),center=True, window="hamming")
plt.subplot(211)
librosa.display.specshow(librosa.amplitude_to_db(D,ref=np.max),y_axis='log', x_axis='time')
plt.title('Power spectrogram: FFT=4096, Win/Hop 0.08/0.04')
plt.colorbar(format='%+2.0f dB')
plt.tight_layout()
D = librosa.stft(y, n_fft=4096, win_length=int(sr*0.08), hop_length=int(sr*0.02),center=True, window="hamming")
plt.subplot(212)
librosa.display.specshow(librosa.amplitude_to_db(D,ref=np.max),y_axis='log', x_axis='time')
plt.title('Power spectrogram: FFT=4096, Win/Hop 0.08/0.02')
plt.colorbar(format='%+2.0f dB')
plt.tight_layout()
plt.show()

#
n_ftt = 2048
n_mels = 128 
melfb = librosa.filters.mel(sr, n_ftt, n_mels)

plt.figure()
plt.subplot(211)
librosa.display.specshow(melfb, x_axis='linear')
plt.ylabel('Mel filter')
plt.title('Mel filter bank FFT 2048 Mels 128 ')
plt.colorbar()
plt.tight_layout()
n_ftt = 2048
n_mels = 40
melfb = librosa.filters.mel(sr, n_ftt, n_mels)
plt.subplot(212)
librosa.display.specshow(melfb, x_axis='linear')
plt.ylabel('Mel filter')
plt.title('Mel filter bank FFT 2048 Mels 40')
plt.colorbar()
plt.tight_layout()

melfb = librosa.filters.mel(sr, n_ftt, n_mels)

plt.show()
