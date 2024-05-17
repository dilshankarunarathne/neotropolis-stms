import secrets


def generate_dtp_token():
    return secrets.token_hex(8)
