# banana
GSOC 2018 Raspberry Pi Banana Drum project files

Use to setup a GSOC Raspberry Pi kit for the banana drum project

Instructions:

cd /usr/local/bin

git clone https://github.com/bhontz/banana.git

cd banana

sudo sh setup_banana.sh

This script will setup i2c on the Raspberry Pi, install the python Adafruit MPR121 library, and move the project files to /var/www

AFTER REBOOTING THE PI, you can test the script by running:

sudo i2cdetect -y 1

... you should see a matrix of dashs, confirming i2c is setup.

You should also confirm the presence of the file snare01.wav within folder /var/www, and that you can import the python library Adafruit_MPR121.MPR121

In addition to the software above, you need two incremental (to the GSOC kits) hardware pieces:
  
  a) Adafruit MPR121 capacitive touch sensor. The "Hat" board is ready as is, I soldered a pin header onto the cheaper sensor board.
  
  b) powered USB speaker with a 3.5mm phono jack (as you would connect to a phone)  I used a UE Boom from Costco.
  
You need to connect the "bananas" (or whatever fruit) to the board (and Pi) before you power up the Pi.  The board reads an initial capacitance level.

You may find that you need to adjust the volume.  From terminal, run: sudo amixer cset numid=1 99% to set it louder (less < 99% == quieter!)
