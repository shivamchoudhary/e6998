import os
import sys
class startExperiment(object):
    """
    Wrapper for OpenWPM. Changes the directory to interact with testbench_wrapper.
    """
    def __init__(self,openwpm_dir,NUM_BROWSERS,ITERATIONS,sites):
        self.openwpm_dir = openwpm_dir
        self.ITERATIONS = ITERATIONS
        self.NUM_BROWSERS = NUM_BROWSERS
        self.sites = sites
        self.chdir()
    def chdir(self):
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), self.openwpm_dir))  
        sys.path.insert(1,path)
        import testbench_wrapper
        Exp = testbench_wrapper.Experiment(self.NUM_BROWSERS,self.ITERATIONS,
                self.sites)
