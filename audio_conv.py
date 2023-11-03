import os
from pydub import AudioSegment
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import numpy as np

def convert_to_spectrogram(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".wav"):
            input_path = os.path.join(input_folder, filename)
            
            # Load the audio file
            audio = AudioSegment.from_wav(input_path)
            
            # Convert audio to numpy array
            samples = np.array(audio.get_array_of_samples())
            
            # Create spectrogram
            plt.specgram(samples, Fs=audio.frame_rate)
            
            # Remove axis labels and ticks
            plt.axis('off')
            
            # Save the spectrogram as an image
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.png")
            plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
            
            # Clear the current plot for the next iteration
            plt.clf()

if __name__ == "__main__":
    input_folder = "audio_inp"
    output_folder = "img_out"

    convert_to_spectrogram(input_folder, output_folder)
    print("Conversion completed.")