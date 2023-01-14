#!/usr/bin/env sh
filename="modified_file.txt"


while read id
do
        brave --app="https://instagram.com/$id" &
        sleep 7
        maim -i $(xdotool getactivewindow) /home/arka/Pictures/instagram/ss/$(uuidgen | cut -d'-' -f1).jpg
        sleep 1
        pkill brave
        echo $line
done < $filename
# $(clear)
