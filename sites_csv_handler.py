from shared.csv_reader import CSVReader
from variants.variant_creator import VariantCreator
from shared.query_handling import get_source_id


class SitesCSVHandler:
    """
    Takes the CSV of sites and turns it into a list of tuples
    """
    _planningSiteAddressUnformattedSourceID = get_source_id()
    reader: iter = CSVReader().create_reader_object()
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
                sql_insert_row = [self._planningSiteAddressUnformattedSourceID]
                sql_insert_row.insert(1, row[0])
                sql_insert_row.insert(4, variant[0])
                sql_insert_row.insert(5, variant[1])
                sql_insert_tuple = tuple(sql_insert_row)
                self.sql_insertable_data.append(sql_insert_tuple)
        return self.sql_insertable_data
