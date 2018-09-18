"""
Cookie Clicker Simulator
"""
import math
import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0


class ClickerState:
    """
    Simple class to keep track of the game state.
    """

    def __init__(self):
        self._total_cookies = 0.0
        self._current_cookies = 0.0
        self._total_time = 0.0
        self._cookies_per_second = 1.0
        self._history = [(0.0, None, 0.0, 0.0)]

    def __str__(self):
        """
        Return human readable state
        """
        return ""

    def get_cookies(self):
        """
        Return current number of cookies
        (not total number of cookies)

        Should return a float
        """
        return self._current_cookies

    def get_total_cookies(self):
        """
        Return total number of cookies
        """
        return self._total_cookies

    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._cookies_per_second

    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._total_time

    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return self._history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if self._current_cookies >= cookies:
            return 0.0
        time_to_wait = math.ceil((cookies - self._current_cookies) / self._cookies_per_second)

        return time_to_wait

    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time > 0:
            self._total_time += time
            self._current_cookies += time * self.get_cps()
            self._total_cookies += time * self.get_cps()

    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if self._current_cookies >= cost:
            self._current_cookies -= cost
            self._cookies_per_second += additional_cps
            self._history.append(tuple([self._total_time, item_name, cost,
                                 self._total_cookies]))


def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    build_clone = build_info.clone()
    clicker = ClickerState()

    while clicker.get_time() <= duration:
        remaining_time = duration - clicker.get_time()

        item_to_get = strategy(clicker.get_cookies(), clicker.get_cps(),
                               clicker.get_history(),
                               remaining_time,
                               build_clone)
        if item_to_get is None:
            break
        elif clicker.time_until(build_clone.get_cost(item_to_get)) > remaining_time:
            break
        else:
            clicker.wait(clicker.time_until(build_clone.get_cost(item_to_get)))
            clicker.buy_item(item_to_get,
                             build_clone.get_cost(item_to_get),
                             build_clone.get_cps(item_to_get))
            build_clone.update_item(item_to_get)

    clicker.wait(remaining_time)

    print ""
    print clicker.get_history()[len(clicker.get_history()) - 1]
    print "Time:", clicker.get_time()
    print "Current Cookies:", clicker.get_cookies()
    print "CPS:", clicker.get_cps()
    print "Total Cookies:", clicker.get_total_cookies()
    print "Number of Buys:", len(clicker.get_history())

    return clicker


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"


def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None


def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    min_item = None
    min_cost = float('inf')
    for item in build_info.build_items():
        if build_info.get_cost(item) <= min_cost:
            min_item = item
            min_cost = build_info.get_cost(item)

    if (time_left * cps + cookies) < min_cost:
        min_item = None

    print "min item", min_item
    print "min_cost:", min_cost
    print "CPS:", cps
    print "Time Left:", time_left
    print time_left * cps + cookies

    return min_item


def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    max_item = None
    max_cost = 0.0
    info = build_info
    for item in info.build_items():
        if (info.get_cost(item) >= max_cost and info.get_cost(item) <= (time_left * cps + cookies)):
            max_item = item
            max_cost = info.get_cost(item)

    return max_item


def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    info = build_info.clone()
    best_choice = None
    best_ratio = 0.0
    choices = info.build_items()
    for item in choices:
        ratio = max_return(cookies, cps, time_left, info.get_cost(item), info.get_cps(item))

        if ratio >= best_ratio:
            best_choice = item
            best_ratio = ratio
            print best_ratio

    if (time_left * cps + cookies) < info.get_cost(best_choice):
        return None

    return best_choice


def max_return(cookies, cps, time_left, item_cost, item_cps):
    """
    Function to calculate best item purchase
    """
    time = float((item_cost - cookies) / cps)

    if time > time_left:
        time = time_left

    ratio = (item_cps / time) * 2.15 ** ((time_left - time) / time_left)

    return ratio


def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    history = state.get_history()
    history = [(item[0], item[3]) for item in history]


def run():
    """
    Run the simulator.
    """
    # run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)
    # run_strategy("None", SIM_TIME, strategy_none)
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best", SIM_TIME, strategy_best)

# run()
