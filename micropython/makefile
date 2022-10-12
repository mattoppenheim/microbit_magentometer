SHELL := /bin/bash
SOURCE := ./stream_magnetometer.py

mount:
	/home/elm/data/infolab2/progs/scripts/microbit_mount.sh mount

write:
	make mount && uflash $(SOURCE) /media/elm/MICROBIT
