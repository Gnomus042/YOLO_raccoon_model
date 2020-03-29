sudo add-apt-repository ppa:jonathonf/ffmpeg-4
sudo apt-get update
sudo apt-get install ffmpeg

pip3 install tensorflow==1.14.0

wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=16nddbvsE48me8JEq1CU30cs88d14uHb4' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=16nddbvsE48me8JEq1CU30cs88d14uHb4" -O model.h5 && rm -rf /tmp/cookies.txt