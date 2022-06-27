import hashlib
import struct, sys, os
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

if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = 'database/'


file_list = os.listdir(path)

for fileName in file_list:
    with open(path+"/" + fileName, mode='rb') as file: # b is important -> binary
        # load the template from file in a binary list
        ac = np.fromfile(file,dtype).tolist()
        # convert template into a string
        characterics = str(ac).encode('utf-8')
        # create a new template and add charater into the template
        f.createTemplate()
        f.uploadCharacteristics(0x01,ac)
        positionNumber = f.storeTemplate()
        print(positionNumber)
        print('SHA-2 hash of template: ' + hashlib.sha256(characterics).hexdigest())
