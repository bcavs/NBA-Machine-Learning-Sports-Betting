def american_to_decimal(american_odds):
    """
    Converts American odds to decimal odds (European odds).
    """
    if american_odds is not None:
        if american_odds >= 100:
            decimal_odds = american_odds / 100
        else:
            decimal_odds = 100 / abs(american_odds)
        return round(decimal_odds, 2)
    else:
        # Handle the case when american_odds is None
        return None  # or raise an exception or return a default value


def calculate_kelly_criterion(american_odds, model_prob):
    """
    Calculates the fraction of the bankroll to be wagered on each bet
    """
    decimal_odds = american_to_decimal(american_odds)

    if decimal_odds is not None:
        bankroll_fraction = round(
            (100 * (decimal_odds * model_prob - (1 - model_prob))) / decimal_odds, 2
        )
        return bankroll_fraction if bankroll_fraction > 0 else 0
    else:
        # Handle the case where decimal_odds is None
        return 0  # Or handle it in a way that makes sense for your application
