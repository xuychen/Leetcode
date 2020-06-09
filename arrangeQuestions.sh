# !/bin/bash
# $ ./arrangeQuestions.sh /path/to/directory
# OR
# $ ./arrangeQuestions.sh


if [ $# -gt 1 ]; then
    cd $1
fi

except=' miscellaneous arrangeQuestions.sh createFile.sh LICENSE README.md '

for file in *; do
    # skippingn files in variable except
    if [[ $file == .* || $except =~ (.* $file .*) ]]; then
        echo \"$file\" is skipped
        continue
    fi

    if [ -f $file ]; then
        # if this is a file
        DIR=${file%%.*} # filename without extension
        SHORT=${DIR%%-*} # question number

        if [[ -d $SHORT || -e $SHORT.* ]]; then
            # if there is a matched directory
            DIR=$SHORT
        elif [ ! -d $DIR ]; then
            # create one if does not exist
            echo creating Directory \"$DIR\"
            mkdir $DIR
        fi

        mv $file $DIR
        echo FILE \"$file\" is putting in Directory \"$DIR\"
        echo Please give it a question number at the beginning of Directory
    else
        # if this is a directory
        INDEX=$((${file%%-*}-1)) # questions 1-10 have index 0-9
        if [[ ! $INDEX =~ [0-9]+ ]]; then
            echo Directory \"$file\" is not a valid Directory
            continue
        fi

        START100=$((INDEX/100*100+1)) # directory start_index
        DIR100=$START100-$((START100+99)) # directory end_index

        if [[ $file == *-[^0-9]* ]]; then
            # if it is a base directory, e.g. 35-findInsertPosition
            START=$((INDEX/10*10+1))
            DIR=$START-$((START+9))
            PATH10=$DIR100/$DIR
            PATH1=$DIR100/$DIR/$file

            if [ -d $PATH1 ]; then
                # if base directory exists in main catalogs
                for SUB_FILE in $file/*; do
                    if [ -f $PATH1/${SUB_FILE##*/} ]; then
                        # if file exists
                        echo File \"${SUB_FILE##*/}\" exists in Directory \"$PATH1\"
                    else
                        # else
                        mv $SUB_FILE $PATH1
                        echo File \"${SUB_FILE##*/}\" is putting in Directory \"$PATH1\"
                    fi
                done
            elif [ -d $PATH10 ]; then
                # if base directory does not exist in main catalogs
                mv $file $PATH10
                echo Directory \"$file\" is putting in Directory \"$PATH10\"
            else
                # if the directory to place base directory does not exist yet
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