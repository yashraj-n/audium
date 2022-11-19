import binascii

# Change the string to a list of integers to add in audio file
def str2num(dat):
    s = []
    for i in dat:
        i = i[::-1]
        d = (int(binascii.hexlify(i.encode("utf-8")), 16))
        s.append(d)
    return s

# Changes numeric list to string (Not really used but maybe useful in future)
def num2str(dat):
    s = []
    for i in dat:
        s.append(binascii.unhexlify(
            format(i, "x").encode("utf-8")).decode("utf-8"))
    return s

# There's a limit pf -32768 to 32767 for audio files so we split
#  the string into chunks of 2 letters and then convert them to integers
def convert_string_to_chunks(d):
    return [d[i:i+2] for i in range(0, len(d), 2)]