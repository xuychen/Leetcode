# !/bin/bash
# a bash file to generate empty file
# cmd is ./createFile.sh {questionNumber} {filename} {extension}
# or ./createFile.sh {questionNumber} {extension}

extension=' c cpp java py sh js sql '

if [[ ! $1 =~ ^[0-9]+$ ]]; then
    echo Error: \"$1\" is not a valid number
    exit 1
fi

if [[ ! $extension =~ (.* ${@: -1} .*) ]]; then
    echo Error: \"${@: -1} \" is not a valid extension
    exit 1
fi

INDEX=$(($1-1)) # questions 1-10 have index 0-9
START100=$(($INDEX/100*100+1)) # directory start_index
START10=$(($INDEX/10*10+1))
DIRECTORY=`find $START100-*/$START10-*/* -name "$1-*"`

if [[ $# == 2 ]]; then
    if [[ -z $DIRECTORY ]]; then
        echo Error: \"$1\" does not exist in directory
    else
        FILENAME=${DIRECTORY##*/$1-}
        FILEPATH=$DIRECTORY/$FILENAME.$2

        if [[ ! -e $FILEPATH ]]; then
            touch "$FILENAME.$2"
            mv "$FILENAME.$2" $DIRECTORY
            echo Question \"$1-$FILENAME.$2\" created in Directory \"$DIRECTORY\"
        else
            echo Question \"$1-$FILENAME\" has $2 version existed
        fi
    fi
elif [[ $# == 3 ]]; then
    FILENAME="$2.$3"
    if [[ ! -e $FILENAME ]]; then
        touch $FILENAME
        echo create File \"$FILENAME\"
    fi

    if [[ -z $DIRECTORY ]]; then
        DIRECTORY=$1-$2
        mkdir $DIRECTORY
        echo creating Directory \"$DIRECTORY\"
    fi

    mv $FILENAME $DIRECTORY
fi