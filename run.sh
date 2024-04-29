source .venv/bin/activate
startTime=$(date +"%s%3N")
pypy3 solve.py DEBUG < input.txt 1> output.txt
#python3 solve.py DEBUG < input.txt 1> output.txt
endTime=$(date +"%s%3N")
elapsedTime=$(bc <<< "scale=3; ($endTime - $startTime)/1000" | sed -e 's/^\./0./g')
echo "elapsedTime(s): ${elapsedTime}"
