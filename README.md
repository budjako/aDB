# aDB
A Single-User Prototype DBMS

This project is for the partial fulfillment of CMSC 227: Advanced Database Systems, a graduate course in UPLB. For more information
regarding the project, please refer to the [Project Specifications Document](https://github.com/budjako/aDB/blob/master/CMSC%20227%20Project%20Specifications%20AY%202017-2018.pdf) in this repository

## Installation:

### For Ubuntu:

Clone the project to your local machine.
````
git clone https://github.com/budjako/aDB.git
````
Make sure you install the latest version of Python3. Check this [Digital ocean tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04)
on installing python3.

Next, install PyQt4.
````
sudo apt-get install python3-pyqt4
````

Lastly, install [Btrees python package](https://pypi.python.org/pypi/BTrees). Using pip, you may install the package with
````
pip install btrees
````

With python3, pyqt4 and btrees installed, you may now run the program. In a terminal, go to the your local machine's copy of the project. Then run
````
python3 adb.py
````
