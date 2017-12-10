# Utlyz
Let's you to access your FB account and check cricket updates from the command line and returns various things number of unread notifications, messages or friend requests you have or scores and schedules of cricket matches.

This program best runs on Ubuntu (Tested and executed)
To run this program follow the given steps:

Before jumping into the steps, please clone and download the FacebookCLI repository

(1) Download virtualenv in the same folder as that of the FacebookCLI repository programs.(if you already have this then skip this and go to the next step)

    sudo apt install virtualenv
    
    
(2) Then run the virutal environment in the same folder.

    virtualenv venv
    
(3) Then to make sure you enter your virtual environment, enter the following command.

    . venv/bin/activate
    
(4) Then type the command below, in order to make sure that the changes you do in your file are directly reflected in your virtual environment.

    pip install --editable .
    
    
(5) Finally type the below command to make sure that you get a list of the functionalities available in the following program

    fbcli --help
    cricbuzz --help
    
 To check the number of notifications you have type the following command and you'll be prompted to enter Email ID and Password :
 
    fbcli --notifs
    Enter Email ID: <email_id>
    Enter Password: <password>
    
 To check the score of all ongoing matches, you'll have to type the following command:
 
    cricbuzz --score
    
