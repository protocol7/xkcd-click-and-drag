#!/bin/sh

mkdir -p images/scaled
mkdir -p images/stitched

cd images
for f in $(ls *.png)
do
    convert $f -scale 128x128 scaled/$f
done
