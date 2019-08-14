from shared import csv_reader
from shared.iterator_factory import IteratorFactory
CSVReader = csv_reader.CSVReader


def manage_permutations(address_variant_list: list, return_type: str="str") -> list:
    """
    Take the variants created and turn them into a list of completed strings
    Args:
        address_variant_list: The list of incomplete variants, ordered by the order in the address

    Returns: A list of every permutation of every address piece variant

    """
    permuted_variants: list = address_variant_list[0]
    for variant in address_variant_list[1:]:
        permuted_variants = _permute_list(permuted_variants, variant, return_type)
    else:
        completed_variants = permuted_variants
    return completed_variants


def make_variants_by_csv(address_piece, file_name) -> list:
    """
    Takes a single section of the address, and find all variants of it in the csv
    Args:
        address_piece: The section of address we are testing against the csv
        file_name: The name of the csv, in the root folder of the app

    Returns: A list of all variants for that section of address

    """
    reader = IteratorFactory(lambda: CSVReader(file_name).create_reader_object())
    # reader = CSVReader(file_name).create_reader_object()
    try:
        returned_variants = [address_piece]
        for row in reader:
            variant_list: list = row
            if address_piece in variant_list:
                returned_variants = variant_list
                break
    except StopIteration:
        pass
    return returned_variants


def _permute_list(list1: list, list2: list, return_type: str) -> list:

    """
    Receives two string lists and creates all possible permutations of the two lists, separated by a space
    Args:
        list1: The list whose values should appear first in the permutation
        list2: The list whose values should appear second in the permutation

    Returns: A list of permuted strings

    """
    permutations_list: list = []
    if return_type == "str":
        def joiner(permuted_list):
            return ' '.join(permuted_list)
    else:
        def joiner(permuted_list):
            return permuted_list
    for string1 in list1:
        for string2 in list2:
            permuted_val: any = joiner([string1, string2])
            permutations_list.append(permuted_val)
    return permutations_list
