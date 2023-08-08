import pyaudio
import numpy as np



def generate_tones(frequencies, duration, volume=0.5, sample_rate=44100):
    num_samples = int(sample_rate * duration)
    samples = np.arange(num_samples)
    tones = np.sum([volume * np.sin(2 * np.pi * frequency * samples / sample_rate) for frequency in frequencies],
                   axis=0)

    # Normalize the tones to prevent clippings
    tones /= np.max(np.abs(tones))

    return tones.astype(np.float32)


def play_audio(audio_data, sample_rate=44100):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=True)

    stream.write(audio_data.tobytes())

    stream.stop_stream()
    stream.close()
    p.terminate()



'''
if __name__ == "__main__":
    # List of frequencies to play simultaneously
    frequencies_hz = [261, 63, 329.63, 392, ]  # A4, C5, E5, A5-
    duration_seconds = 1

    audio_data = generate_tones(frequencies_hz, duration_seconds)
    play_audio(audio_data)
'''
