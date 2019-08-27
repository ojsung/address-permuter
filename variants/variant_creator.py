from variants.permutation_functions import manage_permutations, make_variants_by_csv


def _create_address_variants(address_list: list, file_name: str) -> list:
    """
    Reads through the given address list, then matches against the csv of possible variants.
    This will recreate the reader object for every variant created, as I was told that time is not
    an issue, but wasn't told whether resource management would be.  And Brianna is now out of town,
    and it's not a big enough issue that I want to bother her about it.
    Args:
        address_list: A list form of the base address

    Returns: a list of variants of the base address

    """
    address_variant_list: list = []
    for address_piece in address_list:
        if address_piece.isdigit():
            address_variant_list.append([address_piece])
        else:
            address_variant_list.append(make_variants_by_csv(address_piece, file_name))
    return address_variant_list


class VariantCreator:
    def __init__(self, address_string: str, suite_abbr_string: str = '', suite_number: str = ''):
        """
        On initialization, receive the full addresses for addressLine1 and addressLine2
        Args:
            address_string: addressLine1 received from MD_Address
            suite_abbr_string: abbreviation for addressLine2 received from MD_SuiteName
            suite_number: string form of integer for addressLine2 received from MD_SuiteCount
        """
        self._base_address: str = address_string.upper()
        self._base_suite_abbr: str = suite_abbr_string.upper()
        self._base_suite_number: str = suite_number

    def get_variants(self) -> list:
        """
        Splits the base address into a list, then calls the needed functions to create the variants
        Returns: An array of all possible variant addresses

        """

        address1_list: list = list(self._base_address.strip(" ").split(" "))
        address1_variant_list: list = _create_address_variants(address1_list, "address1_variables.csv")
        address1_permutation_list: list = manage_permutations(address1_variant_list)

        if self._base_suite_abbr:
            address2_list: list = [self._base_suite_abbr, self._base_suite_number]
            address2_variant_list: list = _create_address_variants(address2_list, "address2_variables.csv")
            address2_permutation_list: list = manage_permutations(address2_variant_list)
            completed_permutation_list = manage_permutations([address1_permutation_list, address2_permutation_list],
                                                               'list')
        else:
            completed_permutation_list: list = manage_permutations([address1_permutation_list, ['']], 'list')

        return completed_permutation_list
