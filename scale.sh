#!/bin/sh

mkdir -p images/scaled
mkdir -p images/stitched

for f in `ls images/*.png`
do
    convert $f -scale 128x128 images/scaled/$f
done
