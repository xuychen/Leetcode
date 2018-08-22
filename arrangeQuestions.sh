# !/bin/bash

cd $1
for file in *
do
    if [[ $file == .* || $file == miscellaneous ]]; then
        continue
    fi

    if [ -f $file ]; then
        DIR=${file%%.*}
        SHORT=${DIR%%-*}

        if [[ -d $SHORT || -e $SHORT.* ]]; then
            DIR=$SHORT
        elif [ ! -d $DIR ]; then
            echo creating Directory \"$DIR\"
            mkdir $DIR
        fi

        mv $file $DIR
        echo FILE \"$file\" is putting in Directory \"$DIR\"
        echo Please give it a question number at the beginning of Directory
    else
        if [[ $file == *-[^0-9]* ]]; then
            INDEX=${file%%-*}
            if [[ ! $INDEX =~ [0-9]+ ]]; then
                echo Directory \"$file\" is not a valid Directory
                continue
            fi

            START=$((INDEX/10*10+1))
            DIR=$START-$((START+9))

            if [ ! -d $DIR ]; then
                echo creating Directory \"$DIR\"
                mkdir $DIR
            fi

            mv $file $DIR
            echo sub-Directory \"$file\" is putting in Directory \"$DIR\"
            
            file=$DIR
        fi

        if [[ $file =~ .*[1-9]0$ ]]; then
            INDEX=${file%%-*}
            if [[ ! $INDEX =~ [0-9]+ ]]; then
                echo Directory \"$file\" is not a valid Directory
                continue
            fi

            START=$((INDEX/100*100+1))
            DIR=$START-$((START+99))

            if [ ! -d $DIR ]; then
                echo creating Directory \"$DIR\"
                mkdir $DIR
            fi

            mv $file $DIR
            echo sub-Directory \"$file\" is putting in Directory \"$DIR\"
        fi
    fi
done