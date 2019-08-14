import mysql.connector

class SQLHandler:
    """
    Creates a SQL connection on creation, and remains open until destroyed
    """
    def __init__(self, config):
        self._config = config
        self.connection = mysql.connector.connect(**self._config)
        self.cursor = self.connection.cursor()
    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def add_row(self, entries: list):
        """
        Adds rows using INSERT to the db
        Args:
            entries: The list of tuples

        Returns:

        """
        query = ("INSERT INTO Core.planningSiteAddressUnformatted"
                 "(planningSiteAddressUnformattedID, planningSiteAddressUnformattedSourceID, planningSiteID, "
                 "dateAdded, dateLastAccessed, addressLine1, addressLine2) "
                 "VALUES (%s, %s)")
        self.cursor.executemany(query, entries)
        self.connection.commit()