#!/bin/bash
 
size=5
echo "<html>" > test.html
echo "\t<head>" >> test.html
echo "\t\t<Data Observertory Test Page>" >> test.html
echo "\t</head>" >> test.html
echo "\t<body>" >> test.html
echo "\t\t<h1>Data Observatory Test Page</h1>" >> test.html
echo "\t\t<h3><a href="/index/index/">Go Back to Dashboard</a></h3>" >> test.html
arr=($(jq 'keys[]' config.json))
arrNum=${#arr[@]}
for ((i=0; i<${size}; i++))
do
    randIndex=$((${RANDOM} % ${arrNum}))
    fix="\""
    tag=${arr[$randIndex]}
    tag=${tag#${fix}}
    tag=${tag%${fix}}
    tag={{${tag}}}
    echo "<p>" ${tag} "</p>" >> test.html
done
echo "\t</body>" >> test.html
echo "</html>" >> test.html
