import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "basicops",
    version = "0.0.1",
    author = "Swumplurd",
    author_email = "swumplurd@outlook.com",
    description = ("Ejemplo de paquete para pip local"),
    packages=['basicops']
)