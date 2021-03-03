
fullpath="$1"

dir="${fullpath%/*}"
fname=${fullpath##*/}

echo $dir

docker run --rm -v $dir:/app/inout -e environment="$fname" name_swapper:latest