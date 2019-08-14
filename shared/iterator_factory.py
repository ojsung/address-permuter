class IteratorFactory:
    """
    Takes an un-instantiated generator and returns a stateless iterator.
    Allows for the reuse of the generator.
    This is a high-processing time, low memory-cost solution
    """
    def __init__(self, iterator_function):
        self.iterator_function = iterator_function

    def __iter__(self):
        return self.iterator_function()
