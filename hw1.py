"""Calculates the three highest salaries and the percentage of all salaries to the top."""


def statistics(*divisions: tuple[str, dict[str, float]], lim: float | None = None) -> tuple[str]:
    """
    Extract top 3 salaries and percentage.

    Args:
        divisions: tuple[str, dict[str, float]] - tuple of divisions names and wages.
        lim: float | None = None - limit from which wages are taken.

    Returns:
        tuple[list, float] - tuple of the three highest salaries and the percentage.
    """
    top_wages = []
    all_wages = []
    wages_limit = []

    for division in divisions:
        for wages in division[1].values():
            all_wages.append(wages)

    for wage in all_wages:
        if lim is not None:
            if wage >= lim:
                wages_limit.append(wage)
        else:
            wages_limit.append(wage)

    top_wages = sorted(wages_limit, reverse=True)[:3]
    wages_sum = sum(wages_limit)
    percent = round(sum(top_wages) / wages_sum * 100, 2) if wages_sum else 0

    return top_wages, percent
