import views
import Common
import unittest
iterations = 1000
def testing():
    config = Common.config
    for k,v in config.iteritems():
        for k1, val1 in v.iteritems():
            output = {}
            for i in range(0,iterations):
                result = views.make_dom({k:k1})
                result = result[k]
                try:
                    output[result] +=1
                except KeyError:
                    output[result] = 1
            for prob,values in val1.iteritems():
                try:
                    est_prob = output[values]/float (iterations)
                except KeyError:
                    continue
                if est_prob-prob <=0.1:
                    print "Success",k,k1,values
                else:
                    print "Try with more iterations"


class Test(unittest.TestCase):
    def testing(self):
        config = Common.config
        for k,v in config.iteritems():
            for k1, val1 in v.iteritems():
                output = {}
                for i in range(0,iterations):
                    result = views.make_dom({k:k1})
                    result = result[k]
                    try:
                        output[result] +=1
                    except KeyError:
                        output[result] = 1
                for prob,values in val1.iteritems():
                    try:
                        est_prob = output[values]/float (iterations)
                    except KeyError:
                        continue
                    result = est_prob-prob
                    self.assertTrue(result<0.1)
# testing()
if __name__=="__main__":
    unittest.main()
