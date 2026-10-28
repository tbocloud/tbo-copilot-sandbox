SALES_TEAM_MESSAGE = "Add at least one Sales Person in the Sales Team table."


def margin_rate(selling: float, buying: float) -> float:
    """The margin as a share of the selling price."""
    if not selling:
        return 0.0
    return (selling - buying) / selling


def require_sales_team(doc):
    """A Sales Invoice needs a Sales Team row; a return (credit note) does not."""
    if getattr(doc, "is_return", 0):
        return
    if not getattr(doc, "sales_team", None):
        raise ValueError(SALES_TEAM_MESSAGE)


def validate(doc, method=None):
    doc.margin_rate = margin_rate(doc.selling, doc.buying)
    require_sales_team(doc)
