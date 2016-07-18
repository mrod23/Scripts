<<Comment
    work on getting this script to work with uri

Comment

#!/bin/bash
filename="$1"
hashNum=1
count=0
while read -r line
do
    if [ $count -gt 3 ]
    then
     echo "Waiting.................."
     sleep 1m
     count=0
    fi
    echo "Retrieving url"
    echo $line
    name=$line
    curl 'https://www.virustotal.com/vtapi/v2/url/report' --form apikey="af492b1351def36003ae0d7e8210bf000c8c52d5c1a7e37a057af865f90c5937" --form resource="$line" >> vt_results/$line.jsons
    count=$((count+1))
    hashNum=$((hashNum+1))
done < "$filename"


