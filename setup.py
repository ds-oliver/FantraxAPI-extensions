from setuptools import setup, find_packages

setup(
    name="fantrax-extensions",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fantraxapi",  # The base package
    ],
    author="hogan_m",
    description="Extensions and tools for the FantraxAPI package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/hogan_m/FantraxAPI-extensions",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
