from sites_csv_handler import SitesCSVHandler
from sql_handler import SQLHandler

if __name__ == '__main__':
    """
    On init, begin gathering the needed data.
    """
    correct_response: bool = False
    while not correct_response:
        ask_if_defaults: str = input("Use default MySQL connection? (y/n)")
        if ask_if_defaults == "n":
            username: str = input("Enter your username: ")
            password: str = input("Enter your password: ")
            host: str = input("Enter the host: ")
            database: str = input("Enter the database: ")
            correct_response: bool = True


    config: dict = {
        "username": username,
        "password": password,
        "host": host,
        "database": database
    }

    sql_handler: SQLHandler = SQLHandler(config)
    sites_csv_handler: SitesCSVHandler = SitesCSVHandler()
    sql_data: list = sites_csv_handler.build_sql_insert_data()
    data_length: str = str(len(sql_data))
    do_insert: bool = False
    while not do_insert:
        insert_response = input("Insert {} new entries? (y/n): ".format(data_length))
        if insert_response == "y":
            sql_handler.add_row(sql_data)
            do_insert = True
        elif insert_response == "n":
            print("Exiting")
            do_insert = True
    
