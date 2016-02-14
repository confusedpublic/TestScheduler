import datetime
import time
import threading
import traceback
import logging
import scheduler as scheduler

class testFunc():
    def __init__(self):
        self.lock = threading.Lock()
        self.amActive = False
        
    def run(self, force=False):
        if self.amActive:
            return
        
        self.amActive = True
        _ = force
    
        logging.info("Trying to set up logging once a minute")
        print "test"
        
        self.amActive = False

cycle_time = datetime.timedelta(seconds=30)

testscheduler = scheduler.Scheduler(testFunc(), cycleTime=cycle_time, threadName="TESTSCHEDULER")

testscheduler.run()