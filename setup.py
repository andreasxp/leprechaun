"""Install script for leprechaun."""
from setuptools import setup, find_packages

install_requires = [
    "cachetools",
    "pywin32",
    "pyyaml",
    "PySide2",
    "pyinstaller",
    "calc @ https://github.com/andreasxp/calc/archive/refs/heads/main.zip"
]

entry_points = {
    "gui_scripts": ["leprechaun = leprechaun.__main__:main"],
    "console_scripts": ["leprechaun-cli = leprechaun_cli:main"],
}

setup(
    name="leprechaun",
    version="0.2.0",
    description="Friendly crypto miner",
    author="Andrey Zhukov",
    author_email="andres.zhukov@gmail.com",
    license="MIT",
    install_requires=install_requires,
    packages=find_packages(include=[
        "leprechaun",
        "leprechaun.*"
    ]),
    package_data={
        "leprechaun": ["data/*"]
    },
    entry_points=entry_points
)
