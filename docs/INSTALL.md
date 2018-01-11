# Utlyz
Let's you to access the following things
                    
                    (1) Your FB account
                    (2) Check cricket updates from the command line
                    (3) Search on Google and Wiki from the Command line
                    (4) Get lyrics of various songs from the command line
                    (5) Gives you the news bulletin as well

This program best runs on Ubuntu (Tested and executed)
To run this program follow the given steps:

Before jumping into the steps, please clone and download the Utlyz-CLI repository

There are 2 ways to run this program!
## 1st PROCEDURE (EASY METHOD)
Run the command below in the  "Utlities" directory (which will be inside the downloaded repository folder) directly on the command line:

    . prep.sh
    
And your virtualenv will be setup and ready to use!

## 2nd PROCEDURE (EASY BUT LONG AND SLIGHTLY CONFUSING)

(1) Download virtualenv in the same folder as that of the Utlyz-CLI repository programs.(if you already have this then skip this and go to the next step)

    sudo apt install virtualenv
    
    
(2) Then run the virutal environment in the same folder.

    virtualenv venv
    
(3) Then to make sure you enter your virtual environment, enter the following command.

    . venv/bin/activate
    
(4) Then type the command below, in order to make sure that the changes you do in your file are directly reflected in your virtual environment.

    pip install --editable .
    
    
(5) Finally type the below commands one by one to make sure that you get a list of the functionalities available in the following program

    fbcli --help
    cricbuzz --help
    lyrics --help
    searching --help
    news --help
