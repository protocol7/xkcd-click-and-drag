for f in `ls *.png`
do
    convert $f -scale 128x128 scaled/$f
done
