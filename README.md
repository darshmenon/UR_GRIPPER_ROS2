# UR Gripper with UR Robot Arm - ROS2 Setup

## Overview
This project integrates a **UR robotic arm** with the **Robotiq 2F-85 Gripper** using **ROS2 (Jazzy)**. It includes **URDF/Xacro** files to define the robot structure and allows visualization in **RViz**.

## Prerequisites
Make sure you have **ROS2 Jazzy** installed and sourced:
```bash
source /opt/ros/jazzy/setup.bash
```
Also, install required ROS2 packages if not installed:
```bash
sudo apt update && sudo apt install ros-jazzy-xacro ros-jazzy-joint-state-publisher-gui ros-jazzy-robot-state-publisher ros-jazzy-rviz2
```

## Screenshots

![rviz](/images/image.png)

## Convert Xacro to URDF
Before launching, convert the `.xacro` file into `.urdf`:
```bash
ros2 run xacro xacro /home/darsh/UR_GRIPPER/src/ur_description/urdf/ur.urdf.xacro -o /home/darsh/UR_GRIPPER/src/ur_description/urdf/ur.urdf
```

## Checking URDF Validity
You can verify the URDF file structure:
```bash
check_urdf /home/darsh/UR_GRIPPER/src/ur_description/urdf/ur.urdf
```
If successful, it should print the robot tree structure.

## Launch the URDF Model in RViz
To visualize the URDF in **RViz**, use:
```bash
ros2 launch urdf_tutorial display.launch.py model:=/home/darsh/UR_GRIPPER/src/ur_description/urdf/ur.urdf
```


## Future Enhancements
- Integrate with **MoveIt!** for motion planning.
- Add **Gazebo** simulation support.
- Implement real hardware control for the **UR robot arm + Robotiq Gripper**.

---

Now you are ready to **simulate your UR robot with the Robotiq gripper! 🚀**

