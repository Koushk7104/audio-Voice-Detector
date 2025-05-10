import os
import numpy as np
import librosa
def extract_features(file_path, duration=5.0, sr=22050, n_mfcc=13):
    """
    Extracts audio features (MFCCs) from the given file path.

    Args:
        file_path (str): Path to the audio file.
        duration (float): Maximum duration of the audio to load (in seconds).
        sr (int): Sampling rate (in Hz).
        n_mfcc (int): Number of Mel Frequency Cepstral Coefficients (MFCCs) to extract.

    Returns:
        np.ndarray or None: Mean MFCC features or None if an error occurs.
    """
    try:
        print(f"Loading file: {file_path}")
        # Load the audio file
        y, sr = librosa.load(file_path, duration=duration, sr=sr)
        # Extract MFCC features
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
        print(f"Extracted MFCC features for file: {file_path}")
        # Return the mean MFCCs
        return np.mean(mfccs.T, axis=0)
    except Exception as e:
        print(f"Error extracting features from {file_path}: {e}")
        return None
def load_data(data_dir):
    """
    Loads and processes audio data from the given directory.

    Args:
        data_dir (str): Root directory containing 'human' and 'ai_generated' subfolders.

    Returns:
        tuple: A tuple of features (np.ndarray) and labels (np.ndarray).
    """
    features, labels = [], []
    print(f"Starting data loading from directory: {data_dir}")
    # Iterate over 'human' and 'ai_generated' folders
    for label, folder in enumerate(['human', 'ai_generated']):
        folder_path = os.path.join(data_dir, folder)
        print(f"Processing folder: {folder_path} with label: {label}")
        # Process each file in the folder
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            # Only process .wav files
            if file_path.endswith('.wav'):
                print(f"Processing file: {file_path}")
                feature = extract_features(file_path)
                if feature is not None:
                    features.append(feature)
                    labels.append(label)
                    print(f"Feature added for file: {file_path}")
    
    print(f"Data loading completed. Total files processed: {len(features)}")
    return np.array(features), np.array(labels)
def main():
    """
    Main function to load data and print the extracted features and labels.
    """
    # Define the data directory
    data_dir = "data"
    # Check if the data directory exists
    if not os.path.exists(data_dir):
        print(f"Error: Data directory '{data_dir}' not found.")
        return
    print(f"Starting feature extraction...")
    # Load data and labels
    features, labels = load_data(data_dir)
    # Print the features and labels
    print("Extracted Features:")
    print(features)
    print("\nLabels:")
    print(labels)
    print("Program execution completed.")
# Run the main function
if __name__ == "__main__":
    main()
