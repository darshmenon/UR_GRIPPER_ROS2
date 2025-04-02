import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command, LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import PythonExpression
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    robotiq_description_path = get_package_share_directory('robotiq_description')
    xacro_file = os.path.join(robotiq_description_path, 'urdf', 'robotiq_85_gripper.xacro')

    # Convert Xacro to URDF
    robot_description = ParameterValue(
        Command(['xacro ', xacro_file]), value_type=str
    )

    return LaunchDescription([
        # Argument to enable GUI for joint state publisher
        DeclareLaunchArgument(
            name='use_gui', default_value='true', 
            description='Enable joint_state_publisher_gui'
        ),

        # Robot State Publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}],
            output='screen'
        ),

        # RViz for visualization
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', os.path.join(robotiq_description_path, 'config', 'config.rviz')],
            output='screen'
        ),

        # Joint State Publisher (if GUI is disabled)
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            output='screen',
            condition=IfCondition(LaunchConfiguration('use_gui'))
        ),

        # Joint State Publisher GUI (if GUI is enabled)
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            output='screen',
            condition=IfCondition(LaunchConfiguration('use_gui'))
        ),
    ])
