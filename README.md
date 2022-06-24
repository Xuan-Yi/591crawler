# 591crawler
A small python crawler program searching for new registered houses on [591](https://rent.591.com.tw/) and notify user by LINE Notify API

One needs to download chromedriver and place the executable file on PATH.

Modify the URL in line 14 in `591rent.py` to search for houses with desired requirements.

Add yout LINE Notify API token in line 16 in `591rent.py`.

The `max_pages` in line 17 in `591rent.py` denotes the max number of pages one wants to search, and `time_sleep` in line 18 denotes the time interval (in minutes) between two searching.

## Usage
```bash
$ python 591rent.py
```

## Useful Links

* [591租屋網](https://rent.591.com.tw/)
* [chromedriver](https://chromedriver.chromium.org/downloads)
* [LINE Notify API](https://notify-bot.line.me/doc/en/)
