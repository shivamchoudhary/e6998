import json
import os
import Common

class pvals(object):
    def __init__(self):
        self.pvalf = Common.BASE_DIR+"/pvalues.json"
        self.success = 0
        self.threshold_detection  = 10^-3
        self.load_pvals(self.pvalf) 
    def num_experiment(self):
        return len(self.pvals.keys())
    def num_success(self):
        for k,v in self.pvals.iteritems():
            if v <self.threshold_detection:
                self.success+=1
        return self.success

    def load_pvals(self,fname):
        with open(self.pvalf) as pvalf:
            self.pvals = json.load(pvalf)
        return self.pvals


