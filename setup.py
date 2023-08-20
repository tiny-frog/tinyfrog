from setuptools import setup, find_packages

setup(
    name='tinyfrog',
    version='0.0.1',
    install_requires=[
        'requests',
        'importlib-metadata; python_version == "3.8"',
        'backoff',
    ],
    author='Tiny Frog',
    license='GPLv3',
    platforms='any',
    packages=find_packages(),
)
