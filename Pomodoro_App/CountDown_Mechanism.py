import math

class Countdown:
    def __init__(self, ui):
        self.ui = ui
        self.timer = None
        self.reps = 0


    def count_down(self, count):
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count < 10:
            count_sec = f"0{count_sec}"

        self.ui.update_timer_text(f"{count_min}:{count_sec}")
        if count > 0:
            self.timer = self.ui.root.after(1000, self.count_down, count - 1)
        else:
            self.ui.timer_mechanism.start_timer()
            marks = ""
            work_sessions = math.floor(self.reps/2)
            for _ in range(work_sessions):
                marks += "✅"
            self.ui.update_check_marks(marks)

    def reset_countdown(self):
        if self.timer:
            self.ui.root.after_cancel(self.timer)
            self.timer = None
            
