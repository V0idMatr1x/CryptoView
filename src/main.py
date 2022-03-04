import time
import nimporter, ext as n
from rich.progress import Progress
from rich import print
from pycoingecko import CoinGeckoAPI


stdout = print
# initialize CoinGeckoAPI
cg = CoinGeckoAPI()


def prog_bar(d, c, a, e):
    with Progress() as x:
        t1 = x.add_task(n.red_text(d), 
            total=11) # Task: 1
        t2 = x.add_task(n.green_text(c), 
            total=12)
        t3 = x.add_task(n.cyan_text(a),
            total=13)
        t4 = x.add_task(n.purple_text(e), 
            total=14)
        
        
        while not x.finished:
            x.update(t1, advance=0.09)
            x.update(t2, advance=0.09)
            x.update(t3, advance=0.09)
            x.update(t4, advance=0.09)
            time.sleep(0.02)


def main(greeting):
    stdout(greeting)

    
    # for the aesthetic
    _ = prog_bar(
        "Establishing connection to API...",
        "Gathering Data...",
        "Analyzing Data...",
        "Outputting Data to Terminal..."
    )
    
    
    # fetch crypto data
    crypto = [
        cg.get_price(ids="bitcoin", vs_currencies="usd")["bitcoin"]["usd"],
        cg.get_price(ids="ethereum", vs_currencies="usd")["ethereum"]["usd"],
        cg.get_price(ids="ripple", vs_currencies="usd")["ripple"]["usd"],
        cg.get_price(ids="bitcoin-cash", vs_currencies="usd")["bitcoin-cash"]["usd"],
        cg.get_price(ids="litecoin", vs_currencies="usd")["litecoin"]["usd"],
        cg.get_price(ids="cardano", vs_currencies="usd")["cardano"]["usd"],
        cg.get_price(ids="stellar", vs_currencies="usd")["stellar"]["usd"],
        cg.get_price(ids="monero", vs_currencies="usd")["monero"]["usd"],
        cg.get_price(ids="dash", vs_currencies="usd")["dash"]["usd"],
        cg.get_price(ids="iota", vs_currencies="usd")["iota"]["usd"],
        cg.get_price(ids="ethereum-classic", vs_currencies="usd")["ethereum-classic"]["usd"],
        cg.get_price(ids="nem", vs_currencies="usd")["nem"]["usd"],
        cg.get_price(ids="tron", vs_currencies="usd")["tron"]["usd"],
        cg.get_price(ids="tezos", vs_currencies="usd")["tezos"]["usd"]
    ]
    
    
    btc = n.red_text("\n 💰 Bitcoin Val: $" + str(crypto[0]) + " USD")
    stdout(btc.strip())
    eth = n.red_text("\n 💰 Ethereum Val: $" + str(crypto[1]) + " USD")
    stdout(eth.strip())


main = main(n.purple_text(
    "Welcome, V0idMatr1x!\n"
))