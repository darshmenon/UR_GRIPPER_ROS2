cmake_minimum_required(VERSION 3.5)
project(robotiq_description)

# Find required dependencies
find_package(ament_cmake REQUIRED)

# Install URDF, meshes, and launch files
install(
  DIRECTORY urdf meshes launch config
  DESTINATION share/${PROJECT_NAME}
)

# Export package dependencies
ament_package()
