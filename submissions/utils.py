import secrets


def generate_receipt_code(n_digits: int = 10) -> str:
    """
    Digits-only receipt code. Default: 10 digits formatted as 12345-67890.
    """
    raw = "".join(str(secrets.randbelow(10)) for _ in range(n_digits))
    if n_digits == 10:
        return f"{raw[:5]}-{raw[5:]}"
    return raw

