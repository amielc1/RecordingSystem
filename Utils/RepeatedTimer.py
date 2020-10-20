from threading import Timer

class RepeatingTimer():
    """A Timer class that does not stop, unless you want it to."""

    def __init__(self, seconds, target):
        self._should_continue = False
        self.is_running = False
        self.seconds = seconds
        self.target = target
        self.thread = None

    def _handle_target(self):
        self.is_running = True
        self.target()
        self.is_running = False
        self._start_timer()

    def _start_timer(self):
        if self._should_continue:  # Code could have been running when cancel was called.
            self.thread = Timer(self.seconds, self._handle_target)
            self.thread.start()

    def start(self):
        if not self._should_continue and not self.is_running:
            self._should_continue = True
            self._start_timer()
        else:
            print("Timer already started or running, please wait if you're restarting.")

    def stop(self):
        if self.thread is not None:
            self._should_continue = False  # Just in case thread is running and cancel fails.
            self.thread.cancel()
        else:
            print("Timer never started or failed to initialize.")

# class RepeatingTimer(object):
#     """
#     USAGE:
#     from time import sleep
#     r = RepeatingTimer(_print, 0.5, "hello")
#     r.start(); sleep(2); r.interval = 0.05; sleep(2); r.stop()
#     """
#
#     def __init__(self, interval, function, *args, **kwargs):
#         super(RepeatingTimer, self).__init__()
#         self.args = args
#         self.kwargs = kwargs
#         self.function = function
#         self.interval = interval
#
#     def start(self):
#         self.callback()
#
#     def stop(self):
#         self.interval = False
#
#     def callback(self):
#         if self.interval:
#             self.function(*self.args, **self.kwargs)
#             Timer(self.interval, self.callback, ).start()

#
#
# class RepeatedTimer(object):
#     def __init__(self, interval, function, *args, **kwargs):
#         self._timer = None
#         self.interval = interval
#         self.function = function
#         self.args = args
#         self.kwargs = kwargs
#         self.is_running = False
#         self.start()
#
#     def _run(self):
#         self.is_running = False
#         self.start()
#         self.function(*self.args, **self.kwargs)
#
#     def start(self):
#         if not self.is_running:
#             self._timer = Timer(self.interval, self._run)
#             self._timer.start()
#             self.is_running = True
#
#     def stop(self):
#         self._timer.cancel()
#         self.is_running = False
