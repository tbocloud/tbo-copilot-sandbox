from types import SimpleNamespace


def invoice(**values):
    """A Sales Invoice as validate() reads it."""
    fields = {"selling": 100, "buying": 80, "is_return": 0, "sales_team": []}
    fields.update(values)
    return SimpleNamespace(**fields)
