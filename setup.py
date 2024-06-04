import setuptools
import os
import subprocess
import pathlib

with open("README.md", "r") as fh:
    long_desc = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]

pyramis_aux_dir_path = pathlib.Path(".pyramis")
home_dir_path = pathlib.Path().home()
clone_into_dir_path = home_dir_path / pyramis_aux_dir_path

# make dir, update permissions
os.umask(0)
clone_into_dir_path.mkdir(exist_ok=True)

# do git clone
repo_path = 'https://github.com/armaanchowfin/pyramis-utils.git'
git_dir_path = clone_into_dir_path / ".git"

if not git_dir_path.is_dir():
    # clone
    ret = subprocess.run(["git", "clone", repo_path, clone_into_dir_path], capture_output=True)
else:
    # pull
    ret = subprocess.run(["git", "-C", clone_into_dir_path, "pull"], capture_output=True)

setuptools.setup(
    name="pyramis",
    version="0.0.1",
    author="Armaan Chowfin",
    author_email="armaanchowfin@gmail.com",
    description="The Pyramis to C++ transpiler",
    long_description=long_desc,
    long_description_content_type="text/x-rst",
    packages=setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
    'console_scripts': [
        'pyramis=pyramis.__main__:run'
    ]},
    python_requires='>=3.10',
    install_requires=requirements,
)