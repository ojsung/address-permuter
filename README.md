As a note: please forgive any issues you find here, and any peps I didn't follow. I needed to learn Python and develop this app within a week. So between study time and actual development time, this app was put together over a total of 3 days. As a result, I only studied Python for one day. I am very, very sorry for any peps I did not follow.

This app creates permutations of addresses, then saves them to a db one line at a time. It was designed to have a low memory cost at the expense of time and processing.

The inserts to the db are done one at a time to reduce the size of the packet in the case of very large inserts.

To start, edit the file called "config.py" that has a dictionary named "config_dict" with the default values you want to use with this application. It should look like:

    config_dict = {
    
        "username": "desired_username",
        
        "password": "desired_password",
        
        "host": "desired_host",
        
        "database": "desired_default_database_or_schema"
        
        }
Next, create a csv of all the address line 1 variants you want to consider, and put them in a file called "address1_variables.csv". Each line should have all the variants of the abbreviation you want to consider. Each line should be a different abbreviation.. It should be in all capital letters. The first line will be ignored. It should look something like:

ABBREVIATIONS

ALY,ALLY,ALLEY

DR,DRI,DRV,DRIVE

E,EAST

etc..

Notice that all the words and abbreviations are capitalized.

Do the same for the variants you want to consider for address line 2, and name it "address2_variables.csv"

From there, put all of these, along with the data received from Melissa Data, into the root directory of the application. Then run the following from your command line: "python main.py" If you have both python2 and python3 installed, you will have to instead run "python3 main.py"
