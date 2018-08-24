# !/bin/bash

cd $1
except=' miscellaneous arrangeQuestions.sh '

for file in *; do
    if [[ $file == .* || $except =~ (.* $file .*) ]]; then
        echo \"$file\" is skipped
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
        INDEX=$((${file%%-*}-1))
        if [[ ! $INDEX =~ [0-9]+ ]]; then
            echo Directory \"$file\" is not a valid Directory
            continue
        fi

        START100=$((INDEX/100*100+1))
        DIR100=$START100-$((START100+99))

        if [[ $file == *-[^0-9]* ]]; then
            START=$((INDEX/10*10+1))
            DIR=$START-$((START+9))

            if [ -d "$DIR100/$DIR" ]; then
                mv $file $DIR100/$DIR
                echo Directory \"$file\" is putting in Directory \"$DIR100/$DIR\"
            else
                if [ ! -d $DIR ]; then
                    echo creating Directory \"$DIR\"
                    mkdir $DIR
                fi

                mv $file $DIR
                echo sub-Directory \"$file\" is putting in Directory \"$DIR\"
            
                file=$DIR
            fi
        fi

        if [[ $file =~ .*[0-9]0$ && $file != $DIR100 ]]; then
            if [ ! -d $DIR100 ]; then
                echo creating Directory \"$DIR100\"
                mkdir $DIR100
            fi
    
            if [ -d "$DIR100/$file" ]; then
                echo exist a Directory with the same name under Directory \"$DIR100\"
                mv $file/* $DIR100/$file
                rmdir $file
            else
                mv $file $DIR100
            fi

            echo sub-Directory \"$file\" is putting in Directory \"$DIR100\"
        fi
    fi
done