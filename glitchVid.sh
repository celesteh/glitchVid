#/bin/bash


dir=`dirname $0`
working=`pwd`

echo "dir $dir"
echo "./ $working"

jpeg=$working/$1
echo "jpeg $jpeg"

mkdir /tmp/vid
jout="/tmp/vid/jout.jpg"

convert $jpeg    -resize 866x866\>  $jout

audio=$working/$2
echo "audio $audio"

python $dir/jpeg-glitcher.py $jout $audio "/tmp/vid"

ffmpeg  -i /tmp/vid/frame-%d-jout.jpg.jpg  -i $2 -vcodec mpeg4  $audio.avi

rm /tmp/vid/*
