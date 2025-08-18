from setuptools import find_packages, setup

package_name = 'dwa_planner'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),        
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='brahma',
    maintainer_email='brahma@todo.todo',
    description='Custom DWA Local Planner for ROS2 Humble and Jazzy',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dwa_node = dwa_planner.dwa_node:main', 
        ],
    },
)

