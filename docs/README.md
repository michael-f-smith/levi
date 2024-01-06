# levi

# Installation
```
sudo apt install python3-colcon-common-extensions

sudo apt install python3-vcstool

sudo apt install python3-rosdep2

sudo apt-get install build-essential
```

Install xtensor-dev

# Adding Swapfile:
https://www.digitalocean.com/community/tutorials/how-to-add-swap-space-on-ubuntu-20-04


# Using CoralAI
https://coral.ai/docs/accelerator/get-started/

1. Add their deb package repo 
```
echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list

curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

sudo apt-get update
```

2. Install the Edge TPU runtime:
```
sudo apt-get install libedgetpu1-std
```

3. Optional (Check above link for increasing speeds)

4. Install PyCoral Library (requires python3.6 to python3.9 [may need to use pyenv https://realpython.com/intro-to-pyenv/])
```
sudo apt-get install python3-pycoral
```

4.1 Installing pyenv
```
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl

curl https://pyenv.run | bash

# Then run anything that gets printed to the terminal

# Print the python versions available in pyenv
pyenv install --list

# Install a specific version for example 3.7.2
pyenv install -v 3.7.2
```

# Documentation on running create3_sim:
https://github.com/iRobotEducation/create3_sim/tree/humble


# Nav2 Dependencies
```
sudo apt-get install -y libbondcpp-dev  # In actuality, I ended up using rosdep and importing things from .repos file

sudo apt install ros-navigation2

sudo apt install ros-nav2-bringup

sudo apt-get install ros-humble-turtlebot3
```

# Roomba_rpi project
https://github.com/process1183/roomba-rpi/blob/master/docs/roomba_remote_control.md

# ROS on Steam Deck Discussion
https://discourse.ros.org/t/ros-on-steam-deck/27283/14

# RoboStack Documentation on Running ROS with Mamba
https://robostack.github.io/GettingStarted.html

# Docker and ARM
https://www.docker.com/blog/getting-started-with-docker-for-arm-on-linux/

https://www.stereolabs.com/docs/docker/building-arm-container-on-x86/

https://hub.docker.com/r/arm64v8/ros/


# Building in arm docker container:
* Git clone this repo
* Install libignition from here: https://gazebosim.org/api/math/5.0/install.html
   * Run the following to install required build packages:
    ```
    apt update && apt install git wget build-essential libboost-system-dev libboost-thread-dev libboost-program-options-dev libboost-test-dev libbondcpp-dev libignition-math6-dev ros-humble-test-msgs ros-humble-angles ros-humble-control-msgs ros-humble-diagnostic-updater
    ```


# Configuring static ip on ubuntu server on raspi:
* https://linuxopsys.com/topics/configure-static-ip-on-ubuntu
* https://stackoverflow.com/questions/77352932/ovsdb-server-service-from-no-where
  ```
  # run this first
  sudo apt-get install linux-modules-extra-raspi
  # run this then
  sudo apt-get install openvswitch-switch-dpdk
  ```

# Running ROS2 on startup:
* http://iotdesignshop.com/2022/11/06/how-does-the-ros2-turtlebot4-service-launch-when-the-turtlebot-boots-up/
* https://github.com/tmux/tmux/wiki

# Pyroombaadapter
* https://github.com/AtsushiSakai/PyRoombaAdapter

# Cameras
* https://www.raspberrypi.com/documentation/computers/camera_software.html#building-libcamera-and-rpicam-apps
* https://medium.com/@gibryonbhojraj/how-to-raspberry-pi-64-bit-with-camera-support-def95f206188
  - Install raspi-config
  - 

# Raspi Config file
* https://www.raspberrypi.com/documentation/computers/config_txt.html
* https://forums.raspberrypi.com/viewtopic.php?t=310359
  - Potentially comment out gpu_mem in config.txt

