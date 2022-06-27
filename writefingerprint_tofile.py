import hashlib
import time
from pyfingerprint.pyfingerprint import PyFingerprint
from pyfingerprint.pyfingerprint import FINGERPRINT_CHARBUFFER1 


## Search for a finger
##

## Tries to initialize the sensor
try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)

## Gets some sensor information
print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

try:
    print('Waiting for finger...')

    ## Wait that finger is read
    #while ( f.readImage() == False ):
    #    pass


    ## OPTIONAL stuff
    ##

    ## Loads the found template to charbuffer 1
    characterics=''
    
    for i in range(0, f.getTemplateCount()):
        f.loadTemplate(i, 0x01)
        print('Downloading image (this take a while)...')
        ## Downloads the characteristics of template loaded in charbuffer 1
        ac =f.downloadCharacteristics(0x01) 
        print(type(ac[1]))
        print(len(ac))
        characterics = str(ac).encode('utf-8')
        filename = "./database/finger_{}.bin".format(i)
        wf=open(filename,"wb")
        wf.write(bytearray(ac))
        wf.close()
        ## Hashes characteristics of template
        print('SHA-2 hash of template: ' + hashlib.sha256(characterics).hexdigest())

    #f.loadTemplate(0, 0x01)
    #characterics = f.downloadCharacteristics(0x01)
    #load template 3
    #print("----")
    #f.createTemplate()
    #print("ddfdfd")
    #f.uploadCharacteristics(0x01,characterics)
    #print("fdddd")
    #positionNumber = f.storeTemplate()
    #print("done " + positionNumber)

except Exception as e:
    print('Operation failed!')
    print('Exception message: ' + str(e))
    exit(1)