#!/bin/bash
cd $OPENWPM_DIR
python testbench_wrapper.py $NUM_BROWSERS $ITERATIONS $sites
