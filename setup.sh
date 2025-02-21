#!/bin/bash

# Install apt packages
sudo apt install -y vim \
	python3-flask \
	python3-picamera2 \
	ffmpeg


# Install python packages
pip install pyroombaadapter --break-system-packages
pip install getch --break-system-packages
