import json
import os
import Common
filename = ['pvalues0.1.json',
        'pvalues0.5.json',
        'pvalues0.9.json']
class pvals(object):
    def __init__(self):
        self.prob = {0.1:"",
                0.5:"",
                0.9:""}
        self.threshold_detection  = 10^-3
    def run_exp(self):
        for files in filename:
            self.pvals = self.load_pvals(files)
            probability = files.split(".json")[0]
            probability = int(probability.split("pvalues")[1])
            self.prob[probability] = self.num_success()
        return dict(sorted(self.prob.iteritems()))
    def num_experiment(self):
        return len(self.pvals.keys())
    def num_success(self):
        self.success = 0
        for k,v in self.pvals.iteritems():
            if v <self.threshold_detection:
                self.success+=1
        return self.success
    def load_pvals(self,fname):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        BASE_DIR = os.path.join(BASE_DIR,"attribute/") 
        print BASE_DIR + fname
        with open(BASE_DIR + fname) as pvalf:
            self.pvals = json.load(pvalf)
        return self.pvals

