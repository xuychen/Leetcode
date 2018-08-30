# !/bin/bash
# a bash file to generate empty file
# cmd is ./createFile.sh {questionNumber} {filename} {extension}

extension=' c cpp java py sh js ' 

if [[ ! -e "$2.$3" ]]; then
    touch "$2.$3"
    echo create File \"$2.$3\"
fi

if [[ ! $1 =~ [0-9]+ ]]; then
    echo Error: \"$1\" is not a valid number
    exit 1
fi

if [[ ! $extension =~ (.* $3 .*) ]]; then
    echo Error: \"$3\" is not a valid extension
    exit 1
fi

if [ ! -d "$1-$2" ]; then
    mkdir "$1-$2"
    echo creating Directory \"$1-$2\"
fi

mv "$2.$3" $1-$2
