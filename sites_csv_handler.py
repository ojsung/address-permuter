from shared.csv_reader import CSVReader
from variants.variant_creator import  VariantCreator
from uuid import uuid4
import time


class SitesCSVHandler:
    """
    Takes the CSV of sites and turns it into a list of tuples
    """
    _planningSiteAddressUnformattedSourceID = 'e6150894-ba19-11e9-8e22-0050568000e2'
    _unix_timestamp: int = time.time()
    reader: object = CSVReader().create_reader_object()
    sql_insertable_data: list = []

    def build_sql_insert_data(self) -> list:
        """
        Uses the shared CSV reader to create the tuple
        Returns: A list of tuples of sites

        """
        for row in self.reader:
            address_string: str = row[4]
            suite_abbr_string: str = row[5]
            suite_number: str = row[6]
            variant_list: list = VariantCreator(address_string, suite_abbr_string, suite_number).get_variants()
            for variant in variant_list:
                sql_insert_row = [str(uuid4())]
                sql_insert_row.insert(1, self._planningSiteAddressUnformattedSourceID)
                sql_insert_row.insert(2, row[0])
                sql_insert_row.insert(3, self._unix_timestamp)
                sql_insert_row.insert(4, self._unix_timestamp)
                sql_insert_row.insert(5, variant[0])
                sql_insert_row.insert(6, variant[1])
                sql_insert_tuple = tuple(sql_insert_row)
                self.sql_insertable_data.append(sql_insert_tuple)
        return self.sql_insertable_data
