from setuptools import find_packages, setup

package_name = 'dwa_planner'

setup(
    name=package_name,
    version='0.0.1',
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
    description='Custom DWA local planner for TurtleBot3 using ROS2',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 
        	'dwa_planner = dwa_planner.dwa_node:main',
        ],
    },
)
