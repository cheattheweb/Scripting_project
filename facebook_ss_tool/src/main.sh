#! /bin/bash
i=10000
filename="id.txt"

while read id
do
    brave --app="https://www.facebook.com/$id/photos_by" &
    mkdir /home/arka/Pictures/facebook/ss/$id/
    sleep 6
    for n in {1..5}
    do
        maim -i $(xdotool getactivewindow) /home/arka/Pictures/facebook/ss/$id/$i.jpg
        sleep 5
        xdotool key space
        i=$((i+1))
    done
    pkill brave
done < $filename

clear
