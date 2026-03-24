if ($PWD.Path -match "[\\/]despyner([\\/]|$)") {
    Write-Host "It appears you are in despyner's folder. It is highly likely that the source code you want to compile is not in here"
} else {
    if (Test-Path "despyner/icons/" -PathType Container) {
        $main = "main.py"
        $name = Split-Path -Leaf $PWD

        if (Test-Path $main -PathType Leaf) {
            pyinstaller $main `
                --workpath=./build `
                --specpath=./ `
                --distpath=./dist `
                --log-level=TRACE `
                --onedir `
                --name=$name `
                --add-data="despyner/icons/;despyner/icons/" `
                --add-data="$name.png;." `
                --optimize=2
        } else {
            Write-Host "$main file does not exist"
        }
    } else {
        Write-Host "Path despyner/icons/ does not exist. Your application will have no icon"
    }
}