def calc_int(x, i, z, t):
    """"
    Used to calculate compound interest over time assuming you add a set amount each year and achieve a set
    interest rate each year. Outputs a list with total monetary value at the end of each year.
    :param x: the initial amount invested
    :param i: the interest rate (1.10 being 10%)
    :param z: the amount being added after each year
    :param t: the years being calculated.
    """
    index = []
    for d in range(t):
        earn = x * i + z
        index.append(earn)
        x = earn
    return index


def calc_simple_int(x, i, t):
    """
    Calculates simple interest based on an initial investment, an interest rate, and a period of years.
    Returns a list with the total value at the end of each year.
    :param x: The amount of money contributed.
    :param i: The interest rate, with 1.10 equaling 10%.
    :param t: The time of the investment, in years.
    """
    index = []
    for d in range(t):
        earn = x * i
        index.append(earn)
        x = earn
    return index


def rev_cmp_int(f, i, t):
    """
    Takes in the amount of money you need, the interest earned on your account, and the number of years you
    are able to invest. Returns the principle you need to achieve the desired outcome.
    :param f: Final amount needed.
    :param i: Interest you can earn.
    :param t: Years you are investing.
    """
    amount = f / i ** t
    return amount


def interest_needed(x, y, t):
    """
    Takes an initial amount invested and a final amount and calculates the average interest compounded each year.
    Returns the interest rate required for initial amount to end at final amount.
    :param x: The initial investment amount.
    :param y: The final account value.
    :param t: The amount of time it is being invested.
    """
    amount = (y / x) ** (1/float(t))
    return amount


def profit_goal(x, y, z):
    """
    Takes in the initial stock price, the desired profit, and the number of shares.
    Returns the stock value required to make a profit.
    :param x: Initial Stock price.
    :param y: The desired profit.
    :param z: The number of shares.
    """
    answer = (x * z + y) / z
    return answer


def simple_roi(x, y):
    """
    Calculates simple Return on Investment (ROI). Returns your ROI as a percent value.
    :param x: Your revenue.
    :param y: Your total costs.
    """
    roi = ((x - y) / y) * 100
    return roi