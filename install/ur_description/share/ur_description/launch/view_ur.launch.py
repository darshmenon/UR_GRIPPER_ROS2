# Copyright (c) 2021 PickNik, Inc.
# All rights reserved.

import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import (
    Command,
    FindExecutable,
    LaunchConfiguration,
)
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    # Package Configuration
    ur_description_pkg = "ur_description"

    # Get package share directory
    ur_description_share = FindPackageShare(package=ur_description_pkg).find(ur_description_pkg)

    # File Path Configuration
    urdf_xacro_path = os.path.join(ur_description_share, "urdf", "ur.urdf.xacro")
    rviz_config_path = os.path.join(ur_description_share, "rviz", "view_robot.rviz")

    # Launch Arguments
    declared_arguments = [
        DeclareLaunchArgument(
            "ur_type",
            default_value="ur3",
            description="Type/series of UR robot",
            choices=["ur3", "ur3e", "ur5", "ur5e", "ur10", "ur10e", "ur16e", "ur20", "ur30"],
        ),
        DeclareLaunchArgument(
            "use_sim_time",
            default_value="false",
            description="Use simulation clock",
        )
    ]

    # Launch Configurations
    use_sim_time = LaunchConfiguration("use_sim_time")

    # Robot Description (from XACRO)
    robot_description_content = Command([
    FindExecutable(name="xacro"),
    " ",
    urdf_xacro_path
])


    robot_description = {"robot_description": ParameterValue(robot_description_content, value_type=str)}

    # Nodes
    joint_state_publisher_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
    )

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[robot_description],
    )

    # Static Transform Publisher for base_link (if not being published)
    static_tf_pub_node = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        arguments=["0", "0", "0", "0", "0", "0", "world", "base_link"],
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", rviz_config_path],
    )

    return LaunchDescription(
        declared_arguments + [
            joint_state_publisher_node,
            robot_state_publisher_node,
            static_tf_pub_node,
            rviz_node,
        ]
    )
