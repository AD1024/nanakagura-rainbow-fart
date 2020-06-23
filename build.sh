python3 verify_files.py
retcode=$?
if [ $retcode -ne 0 ]; then
    echo "Problmatic manifest.json, abort building..."
    exit 1
fi
rm -rf dist
mkdir dist
cd src
make clean
make package
mv ./*.zip ../dist

echo "Finished, check dist/"