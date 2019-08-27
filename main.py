from sites_csv_handler import SitesCSVHandler
from sql_handler import SQLHandler
from shared.query_handling import gather_data, do_or_do_not
from config import config_dict


def main():
    """
    The start file. Imports the classes needed to start, asks for needed base data,
    then runs the imported class methods.  The lifespan of this file is the lifecycle
    of the app itself.
    Returns:

    """
    config: dict = gather_data(config_dict)
    sql_handler: SQLHandler = SQLHandler(config)
    sites_csv_handler: SitesCSVHandler = SitesCSVHandler()
    print("Successfully connected.  Building the data")
    sql_data: list = sites_csv_handler.build_sql_insert_data()
    data_length: str = str(len(sql_data))
    print("{} entries created.".format(data_length))
    do_insert: bool = do_or_do_not("SQL INSERT")
    if do_insert:
        print("Proceeding. This may take a while")
        sql_handler.add_row(sql_data)
        print("All done!")
    elif not do_insert:
        print("Okay! I'll exit out.")
        pass
    print("Thanks, and have a great day!")


# '__main__' and 'main' are both included to make development and debugging easier
# 'main' can be removed if you prefer, Brianne, but it's not really hurting anything
if __name__ == '__main__' or 'main':
    main()
