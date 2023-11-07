cat regions.txt | while read line; do python3 parser.py $line > output/$line.json; done
