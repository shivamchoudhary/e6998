import json
import os
import Common
class pvals(object):
    def __init__(self,current_prob):
        filelist= []
        foldername = "condition" + str(current_prob)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        BASE_DIR = os.path.join(BASE_DIR,"attribute/multipvalues/" + foldername)
        self.base_dir = BASE_DIR
        filelist += [each for each in os.listdir(BASE_DIR) if each.endswith('.json')]
        filelist.remove('config.json')
        self.filelist = filelist
        print filelist
        self.prob = {}
        self.threshold_detection  = 0.001 
        self.run_exp()
    def run_exp(self):
        for files in self.filelist:
            pvals = self.load_pvals(files)
            iterations = str(files.split(".json")[0].split("pvalues_")[1])
            self.prob[iterations] = (pvals["detected_counter"])
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
        BASE_DIR = os.path.join(BASE_DIR,"attribute/multipvalues/") 
        with open(self.base_dir + "/" + fname) as pvalf:
            pvals = json.load(pvalf)
        return pvals

def main():
    pvaluefiles = []
    pvaluefiles += [each for each in os.listdir(os.curdir+"/pvalues") 
            if each.endswith('.json')]
    p = pvals(pvaluefiles)
if __name__ =="__main__":
    main()
