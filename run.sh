
fullpath="$1"

dir="${fullpath%/*}"
fname=${fullpath##*/}

docker run --rm -v $dir:/app/inout -e input_file_name="$fname" name_swapper:latest