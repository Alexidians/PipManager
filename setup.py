from setuptools import setup

setup(
    name='PipManager',
    version='0.1.0',
    entry_points={
        'console_scripts': [
            'pipmanager=commandline.PipManager:main',
        ],
    },
    author='Alexidians',
    description='manage python modules by installing, uninstalling, getting versions, getting an array of all of em.',
    url='https://alexidians.github.io/PipManager/package',
)
