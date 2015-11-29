#!/bin/bash
cd $OPENWPM_DIR
echo $NUM_BROWSERS,$ITERATIONS,$sites
python testbench_wrapper.py $NUM_BROWSERS $ITERATIONS $sites
