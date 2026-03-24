if [[ "$PWD" == */despyner/* || "$PWD" == */despyner ]]; then
    echo "It appears you are in despyner's folder. It is highly likely that the source code you want to compile is not in here"
else
    if [ -d "despyner/icons/" ]; then
        main="main.py"
        name=$(basename $PWD)
        if [ -f $main ]; then
            pyinstaller $main \
                --workpath=./build \
                --specpath=./ \
                --distpath=./dist \
                --noconfirm \
                --log-level=TRACE \
                --onedir \
                --name=$name \
                --add-data=despyner/icons/:despyner/icons/ \
                --add-data=$name.png:. \
                --optimize=2
        else
            echo $main "file does not exist"
        fi
    else
        echo "Path despyner/icons/ does not exist. Your application will have no icon"
    fi
fi
