# Wakatime Visualizer
Visualize your language and editor data from [wakatime](https://wakatime.com/).

## Usage
```sh
./wakatime_visualize.sh <input(json)>"
```
Where the `.json` file is the file you download from your wakatime account, in Settings > Export.

## Installation
```sh
pip install -r requirements.txt
```
Any version of Python 3.x will work.

### Wakadump
You also need [wakadump](https://github.com/wakatime/wakadump), which is installable with
```sh
pip install wakadump
```
* Q: Why is this not in `requirements.txt`?
* A: `Wakadump` has outdated dependencies, and if you are using Python 3.9+, it is likely to break your dependencies.
    Manual installation and version fixing is recommended.
