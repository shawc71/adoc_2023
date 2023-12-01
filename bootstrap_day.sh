set -e
if [ -z "$1" ]
then
	echo "No day number provided"
	exit 1
fi
dir="src/day$1"
mkdir -p "$dir"
python3 ./templater.py "$1" > "$dir/sol.py"
touch "$dir/__init__.py"
touch "$dir/sample-data.txt"
touch "$dir/data.txt"