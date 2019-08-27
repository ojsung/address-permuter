def gather_data(default) -> dict:
    """
    Takes a default dictionary, and asks the user if they want to use it.  If the answer is no,
    it calls _ask_the_user
    Args:
        default: The default dictionary for the default values

    Returns: The default or the gathered data of what the user wants

    """
    gathered_data: dict = default
    correct_response: bool = False
    while not correct_response:
        ask_if_defaults: str = input("Use default MySQL connection? (y/n): ")
        if ask_if_defaults == "n":
            query = list(default)
            gathered_data = _ask_the_user(query)
            correct_response = True
        elif ask_if_defaults == "y":
            correct_response = True
        else:
            print("Type \"y\" for yes, or \"n\" for no")

    return gathered_data


def do_or_do_not(do_what: str) -> bool:
    """
    Asks if the user wants to proceed with a certain action
    Args:
        do_what: The action to do or not do

    Returns: A boolean value of what the user chose

    """
    response_given: bool = False
    received_response: bool = False
    while not response_given:
        insert_response = input("Proceed with {}? (y/n): ".format(do_what))
        if insert_response == "y":
            received_response = True
            response_given = True
        elif insert_response == "n":
            response_given = True
    return received_response


def get_source_id() -> str:
    """
    Asks the user to enter, then verify, the source ID
   Returns: The Source ID
    """
    correct_response: bool = False
    source_id: str = ''
    while not correct_response or not source_id:
        source_id = input("Enter the Source ID: ")
        print("You entered {}".format(source_id))
        yes_no: str = input("Is that right? (y/n): ")
        if yes_no == "y":
            correct_response = True
    return source_id


def _ask_the_user(query: list) -> dict:
    """
    Asks the user what the values for each dictionary key should be
    Args:
        query: The list of keys for the dictionary

    Returns: A new dictionary with the values from the user

    """
    query_dict: dict = {}
    for question in query:
        response: str = input("Enter the {}: ".format(question))
        query_dict[question] = response
    return query_dict
