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

4. INstall PyCoral Library
```
sudo apt-get install python3-pycoral
```

# Documentation on running create3_sim:
https://github.com/iRobotEducation/create3_sim/tree/humble


# Nav2 Dependencies
```
sudo apt-get install -y libbondcpp-dev

sudo apt install ros-navigation2

sudo apt install ros-nav2-bringup

sudo apt-get install ros-humble-turtlebot3
```
