from setuptools import setup

setup(
    name='PipManager',
    version='0.1.0',
    entry_points={
        'console_scripts': [
            'pipmanager=commandline.PipManager:main',
        ],
    },
    author='YourUsername',
    description='Description of your package',
    url='https://alexidians.github.io/PipManager/package',
)
