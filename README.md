# banana
GSOC 2018 Raspberry Pi Banana Drum project files

Use to setup a GSOC Raspberry Pi kit for the banana drum project

Instructions:

cd /usr/local/bin

git clone https://github.com/bhontz/banana.git

cd banana

sudo sh banana_setup.sh

This script will setup i2c on the Raspberry Pi, install the python Adafruit MPR121 library, and move the project files to /var/www

AFTER REBOOTING THE PI, you can test the script by running:

sudo i2cdetect -y 1

... you should see a matrix of dashs, confirming i2c is setup.

You should also confirm the presence of the file snare01.wav within folder /var/www, and that you can import the python library Adafruit_MPR121.MPR121
