#!/bin/bash
dreamlife=/Users/monyatwu/Desktop/dreamlife
read f
if [[ f==~* ]]; then
    f=${f/#~/$HOME}
fi
find $f \( -iname "*png" -o -iname "*jpg" -o -iname "*mov" -o -iname "*mp4" -o -iname "*webp" \) -a -mtime -12 -exec mv {} $dreamlife \;
#here enter ~/Downloads