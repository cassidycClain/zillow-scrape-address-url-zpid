thondef validate_input(identifier):
    """
    Validates input identifiers like ZPID, address, or URL.
    """
    if isinstance(identifier, str) and (identifier.startswith("http") or identifier.isdigit()):
        return True
    return False