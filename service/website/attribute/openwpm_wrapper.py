import os
import sys
import imp
import subprocess
class startExperiment(object):
    """
    Wrapper for OpenWPM. Changes the directory to interact with 
    testbench_wrapper.
    param: openwpm_dir: The directory where OpenWPM resides
    param: NUM_BROWSERS: Number of browsers required for the experiment.
    param: ITERATIONS: Number of iterations on each browser.
    param: sites: List of sites(array) on which experiment is to be run.
    It has been patched so that it calls a script which changes the directory.

    """
    def __init__(self,openwpm_dir,NUM_BROWSERS,ITERATIONS,sites):
        """
        Initiliaze the variables.
        """
        os.environ['OPENWPM_DIR']= openwpm_dir
        os.environ['ITERATIONS'] = ITERATIONS
        os.environ['NUM_BROWSERS'] = NUM_BROWSERS
        os.environ['sites'] = sites
        self.runBash()
    def runBash(self):
        subprocess.call('./wrapper.sh',shell=True)


a  =startExperiment('/home/shivam/OpenWPM','1','1','http://localhost:8000'
        '/index/test/?country=india')
