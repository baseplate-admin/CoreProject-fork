import ulid

__all__ = ["generate_ulid"]


def generate_ulid():
    return str(ulid.new())
