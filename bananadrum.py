"""
	2018 GSOC Raspberry Pi Jam project - bananadrum.py

	**** Don't forget: amixer cset numid=3 1   # sets audio output to headphone jack on the Raspberry Pi ****
	**** Don't forget: ARM I2C interface has to be configured as ON.  You can use raspi-config for this purpose ****
	**** Don't forget: Power the Raspberry Pi on AFTER the bananas are connected; the sensor needs to calibrate them on power up ****
"""

import  sys, time   # these are just standard modules most python programs require
from pygame import mixer  # this module supports working with audio files
import Adafruit_MPR121.MPR121 as MPR121   # this is a module that supports talking to the Capacitive Touch Sensor

mixer.init()

# create and build a list of sounds, each of the WAV files is an audio file of a drum sound
sounds = list()
sounds.append(mixer.Sound('snare01.wav'))
sounds.append(mixer.Sound('snare02.wav'))
sounds.append(mixer.Sound('snare03.wav'))
sounds.append(mixer.Sound('snare04.wav'))
sounds.append(mixer.Sound('pop_side_01.wav'))
sounds.append(mixer.Sound('kick01.wav'))
sounds.append(mixer.Sound('kick02.wav'))
sounds.append(mixer.Sound('cymbal01.wav'))
sounds.append(mixer.Sound('cymbal02.wav'))
sounds.append(mixer.Sound('cymbal03.wav'))
sounds.append(mixer.Sound('woodblock01.wav'))
sounds.append(mixer.Sound('bell01.wav'))
nbr_of_sounds = len(sounds)

print "\nSounds loaded.  Use pins 0 to %d." % (nbr_of_sounds - 1)
print "\nRemember - Use Ctrl+C to exit this program!\n\n"

cap = MPR121.MPR121()  # initialize the capacitive sensor

if not cap.begin():
	print("Error initializing MPR121, check wiring.  Terminating!")
	sys.exit(1)

last_touched = cap.touched()
while True:
	current_touched = cap.touched()
	pinbit = 0
	for i in range(0, nbr_of_sounds):
		pin_bit = 1 << i   # this allows us to determine which of the capacitive sensor's pins were touched
		if current_touched & pin_bit and not last_touched & pin_bit:
			sys.stdout.write('Banana {0} touched!\r'.format(i))
			sounds[i].play()  # now play the sound associated with that capacitive sensor's pin
			time.sleep(0.5)
			sys.stdout.flush()  # this just allows the messages from this program to stay on one line

		if not current_touched & pin_bit and last_touched & pin_bit:
			sys.stdout.write ('Banana {0} released!\r'.format(i))
			sys.stdout.flush()

	last_touched = current_touched
	time.sleep(0.1)


del sounds
del cap
