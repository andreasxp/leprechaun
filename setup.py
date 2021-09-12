"""Install script for leprechaun."""
from setuptools import setup, find_packages
from setuptools.command.egg_info import egg_info


class egg_info_ex(egg_info):
    """Includes license file into `.egg-info` folder."""

    def run(self):
        # don't duplicate license into `.egg-info` when building a distribution
        if not self.distribution.have_run.get('install', True):
            # `install` command is in progress, copy license
            self.mkpath(self.egg_info)
            self.copy_file('LICENSE.txt', self.egg_info)

        egg_info.run(self)


install_requires = [
    "appdirs",
    "cachetools",
    "pywin32; platform_system=='Windows'",
    "pyyaml",
    "PySide2",
    "better_exceptions",
    "calc @ https://github.com/andreasxp/calc/archive/refs/heads/main.zip",
    "idle @ https://github.com/andreasxp/idle/archive/refs/heads/main.zip"
]

extras_require = {
    "freeze":  [
        "pyinstaller",
    ],
    "docs": [
        "sphinx",
        "furo",
        "sphinx-copybutton"
    ]
}

entry_points = {
    "gui_scripts": ["leprechaun-gui = leprechaun.__main__:mainw"],
    "console_scripts": ["leprechaun = leprechaun.__main__:main"],
}

setup(
    name="leprechaun",
    version="0.5.0",
    description="Your friendly neighborhood cryptominer",
    author="Andrey Zhukov",
    url="https://github.com/andreasxp/leprechaun",
    license="GPLv3",
    license_files = ('LICENSE.txt',),
    cmdclass = {'egg_info': egg_info_ex},
    install_requires=install_requires,
    extras_require=extras_require,
    packages=find_packages(include=[
        "leprechaun",
        "leprechaun.*"
    ]),
    package_data={
        "leprechaun": ["data/*"]
    },
    entry_points=entry_points
)
