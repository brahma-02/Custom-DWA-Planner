# DWA-Planner

OVERVIEW

This project implements a custom Dynamic Window Approach (DWA) local planner for a TurtleBot in ROS2 Humble without using nav2_dwb_controller and aims to generate velocity commands (/cmd_vel) for obstacle avoidance and goal navigation. 

1. Clone the Repo

   cd ~/ros2_ws/src

   git clone https://github.com/brahma-02/DWA-Planner

3. Build the Package

   cd ~/ros2_ws

   colcon build --packages-select dwa_planner

   source install/setup.bash

5. Launch Simulation

   ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py


   In other terminal :

   rviz2                                              #subscribe to different topics (/odom, /scan, marker, /tf)
                                                      # Set fixed frame to base_link or odom 


   In another terminal:

   ros2 run dwa_planner dwa_planner

   
