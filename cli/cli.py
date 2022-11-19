# most of the program lies here

import argparse
import getpass
from audio.audio import decode_audio, encode_audio
from encoders.encoder import vigenere_encrypt, vigenere_decrypt

parser = argparse.ArgumentParser(
    prog="Audium", description="Encode and decode audio files", epilog="By @yashraj-n")

parser.add_argument('method', help="Method to use",
                    choices=['encode', 'decode'])

parser.add_argument('-f', '--audiofile',
                    help="Name of the audio file to encode/decode", required=True)

parser.add_argument('-d', '--data', help="Data to encode", nargs='?')

parser.add_argument('-df', '--datafile', help="File containing data to encode")

parser.add_argument('-k', '--key',
                    help='Key to use for encryption/decryption',nargs='?')
parser.add_argument('-v', '--verbose',
                    help="Verbose output", nargs='?', type=int)

parser.add_argument("-of", "--outputfile", help="Name of the output file", nargs="?")

args = parser.parse_args()
method = args.method
filename = args.audiofile
data = args.data
key = args.key
verbose = args.verbose
datafile = args.datafile
outputfile = args.outputfile


# If data is not provided in command line, read from file
if not data and datafile:
    with open(datafile, 'r', encoding='utf-8') as f:
        data = f.read()
# Verbose print
if verbose:
    print("[*] - Verbose output enabled\n")

# Adding .wav extension to filename if not provided
if not filename.endswith('.wav'):
    filename += '.wav'

# Taking key from user if not provided in command line
if not key:
    key = getpass.getpass("Enter the key: ")
    
if args.method == 'encode':
    if data is None:
        # If data is not provided, take from stdin
        data = input('Enter data to encode: ')
    # Encrypting data before encoding to file
    data = vigenere_encrypt(data, key)
    encode_audio(data, filename, verbose)
    print('Encoded data to audio file successfully!')

elif args.method == 'decode':
    # Decoding data from audio file
    encrypted = decode_audio(filename, verbose)
    # Decrypting data
    try:
        decrypted = vigenere_decrypt(encrypted, key)
        if not outputfile:
            print('Decoded data: ')
        else:
            print('Decoded data saved to file: ' + outputfile)
        try:
            if not outputfile:
                print(decrypted.decode('utf-8'))
            else:
                with open(outputfile, 'w', encoding='utf-8') as f:
                    f.write(decrypted.decode('utf-8'))
            # Might fail to decode if data is not encoded in utf-8
        except UnicodeDecodeError:
            print(decrypted)
    except Exception as e:
        # Decryption may fail if the padding of key is wrong
        print('Error decoding data from audio file (Maybe check key?)!')
        print('Error: ' + str(e))
        print(e)
        # Appending error to file
        open('AUDIUM_ERR.txt', 'a').write(str(e))
    
# Not possbile to reach here added for safety
else:
    print("Invalid method")
