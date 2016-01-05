import sys
import os
import math
import random
import shutil
import subprocess
import aifc

inputfile=str(sys.argv[1])
#outputfile=str(sys.argv[2])
audiofile=str(sys.argv[2])
outdir = str(sys.argv[3])

audiofile = aifc.open(audiofile)

#duration = audiofile.getnframes() / audiofile.getnchannels() / audiofile.getframerate()
duration = audiofile.getnframes()  / audiofile.getframerate()
frames = duration * 25
frames = frames + 2

farr = range(frames+1)
farr = farr[1:(frames+1)]
random.shuffle(farr)
#print(farr)

insize = os.path.getsize(inputfile)
insize = (insize - 32) / 1024
print(insize)


print (outdir)

if not (os.path.exists(outdir)):
    os.makedirs(outdir)

count = 0

outputfile = outdir+ '/frame-' +str(count) +'-'+ os.path.basename(inputfile) + '.jpg'
shutil.copy(inputfile, outputfile)


glitch = [random.randint(0, 0xfe)]
j=0;
num = random.randint(30, 60);
while (j < num):
    by = random.randint(0, 0xfe)
    glitch.append(by)
    j = j + 1

glitch = bytearray(glitch)


k=0

while(count < frames):
    j=0;
    num = random.randint(0, 30);
    while (j < num):
        by = random.randint(0, 0xfe)
        glitch.append(by)
        j = j + 1

    glitch = bytearray(glitch)

    offset = 0


    while ((offset  < (insize * 2 /3)) and (count < frames)) :

        if (count < frames):
            fnum = farr[count]
            outputfile =  outdir +'/frame-' +str(fnum) +'-'+ os.path.basename(inputfile) + '.jpg'
            #print(outputfile)
            with open (outputfile, "wb") as f:
                with open (inputfile, "rb") as i:

                    # don't touch the header
                    bytes = i.read(32+ (offset * 1024));
                    f.write(bytes)
                    f.write(glitch)

                    while True:
                        bytes=i.read(1024)
                        if bytes:
                            f.write(bytes)
                            #print 'looping'
                        else:
                            break

                    f.close()
                    offset = offset + 1
                    i.close()
        count = count +1
#subprocess.call(["/usr/bin/ffmpeg", '\-i ' + outdir+ '/frame-%d-'+ os.path.basename(inputfile) + '.jpg -vcodec mpeg4 -r 12' + os.path.dirname(inputfile) + os.path.basename(inputfile) +'.avi'])
