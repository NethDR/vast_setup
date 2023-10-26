apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

curl https://raw.githubusercontent.com/alexandra-udrescu/stuff/main/WARLLAMA240k.ipynb -O

pip install -U autotrain-advanced > install_logs.txt

autotrain setup > setup_logs.txt

mkdir data

python3 setup.py