# !/bin/bash
# a bash file to generate empty file
# cmd is ./createFile.sh {questionNumber} {filename} {extension}
# or ./createFile.sh {questionNumber} {extension}

extension=' c cpp java py sh js '

if [[ ! $1 =~ ^[0-9]+$ ]]; then
    echo Error: \"$1\" is not a valid number
    exit 1
fi

if [[ ! $extension =~ (.* ${@: -1} .*) ]]; then
    echo Error: \"${@: -1} \" is not a valid extension
    exit 1
fi

if [[ $# == 2 ]]; then
    START100=$(($1/100*100+1)) # directory start_index
    START10=$(($1/10*10+1))
    DIRECTORY=`find $START100-*/$START10-*/* -name $1-*`

    if [ -z $DIRECTORY ]; then
        echo Error: \"$1\" does not exist in directory
    else
        FILENAME=${DIRECTORY##*/$1-}
        FILEPATH=`find $START100-*/$START10-*/$1-*/* -name *.$2`

        if [ -z $FILEPATH ]; then
            touch "$FILENAME.$2"
            mv "$FILENAME.$2" $START100-*/$START10-*/$1-*
        else
            echo Question $1 has $2 version existed
        fi
    fi
elif [[ $# == 3 ]]; then
    if [[ ! -e "$2.$3" ]]; then
        touch "$2.$3"
        echo create File \"$2.$3\"
    fi

    if [ ! -d $1-* ]; then
        short=${2%%-*}
        mkdir "$1-$short"
        echo creating Directory \"$1-$short\"
    fi

    mv "$2.$3" $1-*
fi