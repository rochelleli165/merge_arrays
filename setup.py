from setuptools import setup

package_name = 'merge_arrays'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Rochelle Li',
    maintainer_email='rli484@wisc.edu',
    description='Wisconsin Autonomous Coding Challege Merge Array Nodei',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
		'merge_arrays_node = merge_arrays.merge_arrays_node:main',
		'arrayone = merge_arrays.first_array_publisher:main',
		'arraytwo = merge_arrays.second_array_publisher:main',
        ],
    },
)
