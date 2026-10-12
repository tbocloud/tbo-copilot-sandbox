def margin_rate(selling: float, buying: float) -> float:
    """The margin as a share of the selling price."""
    if not selling:
        return 0.0
    return (selling - buying) / selling


def validate(doc, method=None):
    doc.margin_rate = margin_rate(doc.selling, doc.buying)
