"""Utilities for cleaning name strings."""


def clean_name(raw):
    """Collapse whitespace and convert a name to title case."""
    return " ".join(raw.split()).title()
