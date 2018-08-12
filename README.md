# JUCO

JUCO is the "JUv sCOre" analysis tool that will be used to evauate companies on various different metrics. This README provides a guide to the files and how to use the repository. 

You HAVE TO use a virtual environment when working with this repository. The README provides a guide to creating this. Additionally, you have to update a file with dependencies as you continue adding them for the various software that we will be creating. There is a guide to how to update the repository to include these dependencies further down. 

## Starting out
1. Clone Repository
2. cd to Repository

## Create a virtual environment
1. Type `virtualenv (directory name)` when you are inside the JUCO file
2. The name of the virtual environment MUST BE `venv` 
3. To activate your virtual environment, type `source venv/bin/activate`
4. Install the dependencies 
5. Continue working within this virtual environment
6. Deactivate the environment by typing `deactivate`

## How to install the various dependencies
1. Within your virtual environment, type `pip install -r requirements.txt` to install the dependencies
2. When you install new dependencies, update this file by typing `pip freeze -l > requirements.txt`

## What are the various files
- (a): `requirements.txt`: Needed to install the dependencies
- (b): `vader_test.py`: Testing the VADER sentiment analysis
