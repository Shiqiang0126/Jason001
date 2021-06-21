#bin_rw.py test struct read/write to file

import struct

file = open('bin_test.dat', 'wb')
for i in range(100):
    data = struct.pack('i', i)
    file.write(data)
file.close()

file = open('bin_test.dat', 'rb')
size = struct.calcsize('i')
bytes_read = file.read(size)
while bytes_read:
    value = struct.unpack('i', bytes_read)
    value = value[0]
    print(value, end=' ')
    bytes_read = file.read(size)
file.close()



