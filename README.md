# Calibrator environment

The purpose of this project is to support the calibration of the inner camera of Gazebo.
I experimented a little bit with the AR track alvar project in gazebo (http://wiki.ros.org/ar_track_alvar) and was not satisfied with the detected TF positions. I was convinced that the inaccuracies coming from the AR detector are caused by the not well calibrated camera in gazebo so I made this robot to do the calibration for me.

## Results

If you came here only for the calibration results of the Gazebo's inner camera, they are in the file: calibrationdata.tar.gz Please look at the `calibrator_description/calibrator.gazebo` for the camera settings.

## Prepare your catkin environment

The preparation of the catkin workspace is done the usual way:

```
$ mkdir -p ros_catkin_ws/src
$ cd ros_catkin_ws
$ catkin_make
$ cd src 
$ git clone <this project> 
$ cd ..
$ catkin_make
```

## Launching the environment

This project contains a gazebo world which has a modified version of rrbot available from here:
https://github.com/ros-simulation/gazebo_ros_demos

The rviz version contains a launcher in which the user can see how the joints work:

```$ roslaunch calibrator_description calibrator_rviz.launch```

In the default state the camera looks down to a checkerboard. The image from the camera comes from the gazebo simulation which can be started by launching:

```$ roslaunch calibrator_gazebo calibrator_world.launch```

The robot will adjust its joints into random positions by running:

```$ rosrun calibrator_control camera_mover.py```

The calibration will be able to see the checkerboard from different random angles and heights.

## Calibration

The calibration can be started as described here:
http://wiki.ros.org/camera_calibration/Tutorials/MonocularCalibration

First we need to install the calibration tool:

```$ rosdep install camera_calibration```

Then the calibration tool should be started on the camera image, in our case:

```$ rosrun camera_calibration cameracalibrator.py --size 8x6 --square 0.108 image:=/calibrator/camera1/image_raw camera:=/calibrator/camera1 ```

## Moving the checkerboard

The checkerboard is in the same place under the camera, but can be moved after typing:

```$ rosrun teleop_twist_keyboard teleop_twist_keyboard.py ```

More on this tool can be found here: http://wiki.ros.org/teleop_twist_keyboard

## Issues

Tested only on ROS Melodic, if you find issues on other platforms, please send me a PR with the recommended changes.

The gravitation is switched off in the gazebo world so we can move the robot without any hassle. If you feel the need to fix the physical properties, do it in a PR, I will appreciate any improvement.
