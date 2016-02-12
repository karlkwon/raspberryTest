import subprocess
from subprocess import Popen, PIPE
from time import sleep

p = Popen(['omxplayer','test.mp3'], stdin=PIPE)

## volume control
for i in range(10):
    print i
    p.stdin.write('-')
    sleep(0.5)

for i in range(10):
    print i
    p.stdin.write('+')
    sleep(0.5)

#up - "\027[A"
#down - "\027[B"
#left - "\027[D"
#right - "\027[C"

## seek control
for i in range(4):
    print i
#    p.stdin.write(' ')
    p.stdin.write('\027[C')
    sleep(0.5)

sleep(5)
p.stdin.write('%c' % 27)

p.wait()
