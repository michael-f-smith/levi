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
  - May need to comment out gpu_mem in config.txt
  - To list the number of connected cameras as seen [here](https://raspberrypi.stackexchange.com/questions/78604/help-my-rasperry-pi-camera-is-not-being-detected#:~:text=The%20camera%20is%20plugged%20into,use%20it%20with%20this%20Pi)
  ```
  vcgencmd get_camera
  ```

  * Install v4l2-ctl
  ```
    sudo apt install v4l-utils
  ```
  * First need to install and build libcamera:
  ```
    sudo apt install -y python3-pip git python3-jinja2
    sudo apt install -y libboost-dev
    sudo apt install -y libgnutls28-dev openssl libtiff5-dev pybind11-dev
    sudo apt install -y qtbase5-dev libqt5core5a libqt5gui5 libqt5widgets5
    sudo apt install -y meson cmake
    sudo apt install -y python3-yaml python3-ply
    sudo apt install -y libglib2.0-dev libgstreamer-plugins-base1.0-dev

    # Checkout libcamera
    cd
    git clone https://github.com/raspberrypi/libcamera.git
    cd libcamera
    meson setup build --buildtype=release -Dpipelines=rpi/vc4,rpi/pisp -Dipas=rpi/vc4,rpi/pisp -Dv4l2=true -Dgstreamer=enabled -Dtest=false -Dlc-compliance=disabled -Dcam=disabled -Dqcam=disabled -Ddocumentation=disabled -Dpycamera=enabled

    ninja -C build   # use -j 2 on Raspberry Pi 3 or earlier devices
    sudo ninja -C build install
    ```

  # Installing tflite
  ```
  # https://lindevs.com/install-precompiled-tensorflow-lite-on-raspberry-pi/
  wget https://github.com/prepkg/tensorflow-lite-raspberrypi/releases/latest/download/tensorflow-lite_64.deb

  sudo apt install -y ./tensorflow-lite_64.deb

  # Can remove the .deb with:
  rm -rf tensorflow-lite_64.deb
  ```
  ## Installing tflite_runtime
  ```
  pip3 install tflite-runtime
  ```
  
  * Installing rpicam-apps:
  ```
    sudo apt install -y libcamera-dev libjpeg-dev libtiff5-dev
    # https://www.raspberrypi.com/documentation/computers/camera_software.html#building-rpicam-apps
    sudo apt install -y cmake libboost-program-options-dev libdrm-dev libexif-dev
    sudo apt install -y meson ninja-build
  ```
  * Needs meson >=0.64.0
  ```
    sudo pip3 install meson==0.64.0 # Needs to be installed using sudo since: https://github.com/mesonbuild/meson/issues/8425
  ```
  * Then run the following:
  ```
    cd
    git clone https://github.com/raspberrypi/rpicam-apps.git
    cd rpicam-apps
    meson setup build -Denable_libav=false -Denable_drm=true -Denable_egl=false -Denable_qt=false -Denable_opencv=true -Denable_tflite=true
    meson compile -C build # use -j1 on Raspberry Pi 3 or earlier devices
    sudo meson install -C build
    sudo ldconfig # this is only necessary on the first build
  
    
  ```

# Raspi Config file
* https://www.raspberrypi.com/documentation/computers/config_txt.html
* https://forums.raspberrypi.com/viewtopic.php?t=310359
  - Potentially comment out gpu_mem in config.txt
  - 
  

