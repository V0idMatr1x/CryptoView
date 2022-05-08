# CryptermView
## A terminal utility for viewing the current price of various tokens. Written in Python &amp; Nim!
### It was inspired by `curl rate.sx`

https://user-images.githubusercontent.com/88049272/164791628-881fdd8d-6a67-4180-8aaa-b1b27ac17dd8.mp4

### Configuration:
  - `~/.zshrc`: `alias cv="cd ~/CryptermView/src && python3 main.py; ~"` 
  - `~/.bashrc`: `alias cv="cd ~/CryptermView/src && python3 main.py; ~"`

### Personalization
  - The `main()` function call takes a string as an argument.
  - This string is stored within the greeting parameter.
  - Replace `V0idMatrix` with `main(your name)`
    - Adding Coins
      -  https://pypi.org/project/pycoingecko/

### Usage
- `$ cv`

### Dependencies
  - Backend powered by PyCoinGecko API
  - Terminal Interface powered by Rich
  - Nimporter
  - Nimpy
  - runexe

### Requires
- Python3.10^
- Nim1.6.4^
