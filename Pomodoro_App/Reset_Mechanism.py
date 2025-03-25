class ResetMechanism:
    def __init__(self, timer_mechanism):
        self.timer_mechanism = timer_mechanism

    def reset(self):
        self.timer_mechanism.reset_timer()
