from setuptools import setup, find_packages

setup(
    name="fasterfastapi",
    version="0.0.1",
    packages=find_packages(),  # <== this will include the 'fasterfastapi' package
    install_requires=[
        "Click",
        "Wheel",
    ],
    entry_points={
        "console_scripts": [
            "faster-fastapi = fasterfastapi.cli:cli",
        ]
    }
)
