__author__ = 'Brian M Anderson'
# Created on 9/15/2020


from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='RegisteringImages',
    author='Brian Mark Anderson',
    author_email='bmanderson@mdanderson.org',
    version='0.1.2',
    description='Tools for reading DICOM registration file along with two SimpleITK Images (probably from DICOM) '
                'and resampling the moving image. Major help from Bastien Rigaud in creation.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={'RegisterImages': 'src/RegisterImages'},
    packages=['RegisterImages'],
    include_package_data=True,
    url='https://github.com/brianmanderson/RegisteringImages',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
    ],
    install_requires=required,
)
