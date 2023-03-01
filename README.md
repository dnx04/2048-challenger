# 2048-challenger

Use this to play <https://play2048.co/>

```
pip install websocket-client
./configure
make
google-chrome --remote-debugging-port=1901
python3 2048.py -b chrome
```