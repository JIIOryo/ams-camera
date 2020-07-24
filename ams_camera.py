import os
import subprocess

def main():
    os.environ['LD_PRELOAD'] = '/usr/lib/arm-linux-gnueabihf/libatomic.so.1.2.0'
    subprocess.run(['python3', '/home/pi/ams-camera/server/server.py'])

if __name__ == '__main__':
    main()
