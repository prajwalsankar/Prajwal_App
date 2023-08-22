from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in prajwal_app/__init__.py
from prajwal_app import __version__ as version

setup(
	name="prajwal_app",
	version=version,
	description="App for Practice",
	author="Prajwal",
	author_email="prajwalsankarkolakaluri@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
