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

    
    def start_timer(self):
        self.countdown.reps += 1
        work_sec= self.WORK_MIN * 60
        short_break_sec= self.SHORT_BREAK_MIN * 60
        long_break_sec = self.LONG_BREAK_MIN * 60

        if self.countdown.reps % 8 == 0:
            self.countdown.count_down(long_break_sec)
            self.ui.update_title("Break", RED)
        elif self.countdown.reps % 2 == 0:
            self.countdown.count_down(short_break_sec)
            self.ui.update_title("Break", PINK)
        else:
            self.countdown.count_down(work_sec)
            self.ui.update_title("Work", GREEN)
