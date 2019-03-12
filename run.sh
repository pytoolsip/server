#！/bin/sh
rm -rf log/*

python build.py

cd src

python main.py