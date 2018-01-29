#!/bin/sh

# Add the modified files
cp detector.c darknet-nnpack/examples
cp darknet.h darknet-nnpack/include
cd darknet-nnpack

# You may want to check the makefile first to set the install flags as you need
make
export DARKNETNNPACK=$(pwd)

