import tensorflow as tf
from data_utils import *

path_to_recordname = "record"
path_to_noisy = "noisy/"
path_to_clean = "pure/"
reader = dataPreprocessor(path_to_recordname, path_to_noisy, path_to_clean, use_waveform=True)
reader.write_tfrecord()