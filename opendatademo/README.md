# Setup instructions

This code was written for Python 3, and all the dependencies have been confirmed for Python 3. After cloning the repo:

## Python 3 instructions:

1. Install `folium`: `pip install folium`
2. Install `pyzipcode` (the lib in the pip repo is broken for Python 3):
```
git clone https://github.com/invernizzi/pyzipcode
pip install -e .
```
3. Run `python3 wrangler.py`
4. Open zipPlot.html

## Python 2 instructions:

1. Install folium and pyzipcode:
```
pip install folium
pip install pyzipcode
```
2. Modify `print()` to `print` statements
3. Run `python wrangler.py`
4. Open zipPlot.html