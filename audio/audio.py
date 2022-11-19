import struct
import wave
from utils.convertors import convert_string_to_chunks, str2num
from logger.logger import info

# Encoding Audio
def encode_audio(text, file_name: str,verbose=False, sample_rate=44100.0, ):
    # Converting the String to chunks
    r = convert_string_to_chunks(text)
    info(f'Chunks {r}', verbose)
    # Converting the chunks to integers
    r = str2num(r)
    info(f'Numeric chunks {r}', verbose)

    obj = wave.open(file_name, 'w')
    info(f'Opened {file_name} for writing', verbose)
    obj.setnchannels(1)  # Setting mono channel
    obj.setsampwidth(2)
    info(f'Sample width set to 2', verbose)
    obj.setframerate(sample_rate)
    for i in r:
        # Writing the frames
        data = struct.pack('<h', i)
        obj.writeframesraw(data)
    info(f'Wrote data to {file_name}', verbose)
    obj.close()
    info(f'Closed {file_name}', verbose)


def decode_audio(file_name: str, verbose=False):
    obj = wave.open(file_name, 'r')
    info(f'Opened {file_name} for reading', verbose)
    # Reading the frames
    f = obj.readframes(-1)
    info(f'Read frames from {file_name}', verbose)
    # Decoding the frames as str
    return (f.decode("utf-8"))
