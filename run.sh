#！/bin/sh
rm -rf log/*

# kill process
ps -ef | grep 'python3 main.py' | awk '{print $2}' | xargs kill -9

# run process
cd src
nohup python3 main.py &