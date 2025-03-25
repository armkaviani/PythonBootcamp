from CoundDown_mechanism import Countdown

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

class TimerMechanism:
    WORK_MIN = 1
    SHORT_BREAK_MIN = 5
    LONG_BREAK_MIN = 20

    def __init__(self, ui):
        self.ui = ui
        self.countdown = Countdown(ui)
