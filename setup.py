from setuptools import setup, find_packages


# get version from __version__ variable in elifapp/__init__.py


setup(
	name="newara",
	description="Newara",
	author="E",
	author_email="support@ERPGulf.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
)
