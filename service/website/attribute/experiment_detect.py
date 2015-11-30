import json
import os
import Common
class pvals(object):
    def __init__(self,filelist):
        self.filelist = filelist
        self.prob = {}
        self.threshold_detection  = 10^-3
        self.run_exp()
    def run_exp(self):
        for files in self.filelist:
            pvals = self.load_pvals(files)
            probability = str(files.split(".json")[0].split("prob_")[1])
            self.prob[probability] = self.num_success(pvals)
        return self.prob
    def num_experiment(self,pvals):
        return len(pvals.keys())
    def num_success(self,pvals):
        success = 0
        for k,v in pvals.iteritems():
            if v <self.threshold_detection:
                success+=1
        return success
    def load_pvals(self,fname):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        BASE_DIR = os.path.join(BASE_DIR,"attribute/pvalues/") 
        print BASE_DIR + fname
        with open(BASE_DIR + fname) as pvalf:
            pvals = json.load(pvalf)
        return pvals

def main():
    pvaluefiles = []
    probability = {}
    pvaluefiles += [each for each in os.listdir(os.curdir+"/pvalues") 
            if each.endswith('.json')]
    p = pvals(pvaluefiles)
if __name__ =="__main__":
    main()
