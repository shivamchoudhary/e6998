#!/bin/bash
cd $OPENWPM_DIR
python testbench_wrapper.py $NUM_BROWSERS $ITERATIONS $sites $fname
cd /home/shivam/e6998/service/website/attribute
python dict_creator.py $fname
cd $dataObservatory_dir
python3 test_dataobservatory.py $fname
mv "$fname.json" /home/shivam/e6998/service/website/attribute/pvalues
