import csv


class CSVReader:
    """
    Reads a CSV file and returns an iterable object
    """
    def __init__(self, file_name: str = ''):
        """
        Check if the file name parameter has been given.  If it has not, set it
        Args:
            file_name: the name of the csv located in the root app directory
        """
        self._file_name = file_name
        if not self._file_name:
            self._file_name_setter()

    def create_reader_object(self):
        """
        Opens the csv in the root app folder with the given name, then creates a reader object
        If the csv could not be found, run _file_name_setter()
        Returns: Reader Object for the CSV

        """
        try:
            with open(self._file_name, newline='') as csv_file:
                csv_reader: object = csv.reader(csv_file, dialect='excel')
                first_row = next(csv_reader, None)
                for row in csv_reader:
                    yield row
        except IOError:
            print("File was not found.")
            self._file_name = ''
            self._file_name_setter()

    def _file_name_setter(self):
        """
        Sets the name of the file.  The file must be in the root folder
        Returns:

        """
        print("Please make sure the CSV is in the root folder of this application")
        while not self._file_name:
            self._file_name = input("Enter the file name: ")
