#!/usr/bin/env python3

import os

def convert(array):
    result = []
    for byte in array:
        temp = (byte & 0x7) << 0x5
        byte >>= 0x3
        byte |= temp
        byte ^= 0xff
        result.append(byte)
    return result

if __name__ == '__main__':
    f = input("image/folder location: ").strip('"')
    if os.path.isfile(f):
        file_path = f.replace('.lsc', '.dds')

        with open(f, 'rb') as file:
            data = file.read()
            array_byte = list(data)

        with open(file_path, 'wb') as dds:
            dds.write(bytearray(convert(array_byte)))
            print("Saved file:", file_path)
    else:
        for x, _, y in os.walk(f):
            for z in y:
                if not z.endswith('.lsc'):
                    continue
                
                file = x + '\\' + z
                file_path = x + '\\' + z.replace('.lsc', '.dds')

                with open(file, 'rb') as raw_file:
                    data = raw_file.read()
                    array_byte = list(data)

                with open(file_path, 'wb') as dds:
                    dds.write(bytearray((convert(array_byte))))
                    print("Saved image: ", file_path)
    print()
    input('Press enter to exit')
