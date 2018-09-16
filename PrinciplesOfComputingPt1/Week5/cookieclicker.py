"""
Cookie Clicker Simulator
"""

# import simpleplot

# Used to increase the timeout, if necessary
# import codeskulptor
# codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
# SIM_TIME = 10000000000.0
SIM_TIME = 100000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """

    def __init__(self):
        self.cps = 1.0
        self.cookies_produced = 0.0
        self.current_time = 0.0
        self.cookies = 0.0

        self.history = []

    def __str__(self):
        """
        Return human readable state
        """
        return "There are {} cookies produces per second, a total of {} cookies produced, with a current time of {} and a total of {} cookis".format(self.cps, self.cookies_produced, self.current_time, self.cookies)

    def get_cookies(self):
        """
        Return current number of cookies
        (not total number of cookies)

        Should return a float
        """
        return self.cookies

    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self.cps

    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self.current_time

    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return self.history[:]

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if cookies < self.cookies:
            return 0.0
        else:
            return float(int(cookies - self.cookies) / float(self.cps))

    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time <= 0.0:
            pass
        else:
            self.current_time += time
            cookies_made = time * self.cps
            self.cookies += cookies_made
            self.cookies_produced += cookies_made

    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if cost > self.cookies:
            pass
        else:
            self.cps += additional_cps
            self.cookies -= cost
            self.history.append[(self.current_time, item_name, cost, self.cookies_produced)]

def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """

    # Replace with your code
    return ClickerState()


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
    return None

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    return None

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    return None
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)
    
run()
    

