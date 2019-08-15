# address-permuter
Creates permutations of addresses, then saves them to a db

To start, create a file called "config.py" that has a dictionary named "config_dict"
 with the default values you want to use with this application.  It should look like:
        config_dict = {
            "username": "desired_username",
            "password": "desired_password",
            "host": "desired_host",
            "database": "desired_default_database_or_schema"
            }

Next, create a csv of all the address line 1 variants you want to consider, and
  put them in a file called "address1_variables.csv".  Your csv should look something like:
        ALLEY,ALY
        ANNEX, ANEX,ANX
        ARCADE,ARCD,ARC
        AVENUE,AVNU,AVE,AV
        BAYOU,BYU
        E,EAST
        N,NORTH,NOR
        S,SOUTH
        W,WEST
  Notice that all the words and abbreviations are capitalized.

Do the same for the variants you want to consider for address line 2, and name it "address2_variables.csv"

From there, put all of these, along with the data received from Melissa Data, into the root directory
  of the application.  Then run the following from your command line: "python main.py"
  If you have both python2 and python3 installed, you will have to instead run "python3 main.py"