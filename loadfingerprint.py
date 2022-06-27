import hashlib
import struct
import numpy as np
from pyfingerprint.pyfingerprint import PyFingerprint

dtype = np.dtype('B')
try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)

cnt=f.getTemplateCount()
print(cnt)

fileName = "database/finger_0.bin"

with open(fileName, mode='rb') as file: # b is important -> binary
    #ac =file.read()
    ac = np.fromfile(file,dtype).tolist()
    #ac = struct.unpack("i" * ((len(fileContent) -24) // 4), fileContent[20:-4])
    #fileContent=struct.unpack("i" * ((len(fileContent) -24) // 4), fileContent[20:-4])
    #fileContent = list(fileContent)
    print(type(ac[0]))
    characterics = str(ac).encode('utf-8')
    #print(str(fileContent).encode('utf-8'))
    # create a new template and add charater into the template
    #f.createTemplate()
    #f.uploadCharacteristics(0x01,ac)
    #positionNumber = f.storeTemplate()
    #print(positionNumber)
    print('SHA-2 hash of template: ' + hashlib.sha256(characterics).hexdigest())