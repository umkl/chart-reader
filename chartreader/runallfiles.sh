filenames=`find ./input -type f -regex ".*\.png"`
for file in $filenames
do    
    echo "$file"
    part1="${file/\.png/".csv"}"
    part2="${part1/input/"output"}"
    python3 main.py "$file" "$part2"
    echo "------------------------------------------------"

done
