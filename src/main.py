import time
import nimporter, ext as n
from rich.progress import Progress
from rich import print as stdout
from pycoingecko import CoinGeckoAPI


# initialize CoinGeckoAPI
cg = CoinGeckoAPI()


def prog_bar(p1, p2, p3, p4: str) -> str:
    with Progress() as x:
        t1 = x.add_task(n.red_text(p1), total=11)  # Task: 1
        t2 = x.add_task(n.green_text(p2), total=12)
        t3 = x.add_task(n.cyan_text(p3), total=13)
        t4 = x.add_task(n.purple_text(p4), total=14)

        while not x.finished:
            x.update(t1, advance=0.30)
            x.update(t2, advance=0.20)
            x.update(t3, advance=0.11)
            x.update(t4, advance=0.09)
            time.sleep(0.02)


def main(greeting: str) -> str:
    stdout(n.underline_text(greeting))

    prog_bar(
        "🚀 :: Establishing connection to API...\n",
        "🌎 :: Gathering Data...\n",
        "🔍 :: Analyzing Data...\n",
        "🎬 :: Outputting Data to Terminal...\n",
    )
    n.clear("clear")

    # fetch crypto data
    crypto = [
        cg.get_price(ids="bitcoin", vs_currencies="usd")["bitcoin"]["usd"],
        cg.get_price(ids="ethereum", vs_currencies="usd")["ethereum"]["usd"],
        cg.get_price(ids="ripple", vs_currencies="usd")["ripple"]["usd"],
        cg.get_price(ids="bitcoin-cash", vs_currencies="usd")["bitcoin-cash"]["usd"],
        cg.get_price(ids="litecoin", vs_currencies="usd")["litecoin"]["usd"],
        cg.get_price(ids="cardano", vs_currencies="usd")["cardano"]["usd"],
        cg.get_price(ids="monero", vs_currencies="usd")["monero"]["usd"],
        cg.get_price(ids="dash", vs_currencies="usd")["dash"]["usd"],
        cg.get_price(ids="ethereum-classic", vs_currencies="usd")["ethereum-classic"][
            "usd"
        ],
        cg.get_price(ids="tezos", vs_currencies="usd")["tezos"]["usd"],
    ]

    # Title
    stdout(n.bold_text(n.green_text(">> Crypto Prices 📈" + "\n")))
    
    # Format & Output
    btc = n.red_text("\n   ₿   Bitcoin Val: $" + str(crypto[0]) + " USD")
    stdout(btc)
    stdout(n.cyan_text("________________________________________________/"))
    eth = n.red_text("\n   ⟠   Ethereum Val: $" + str(crypto[1]) + " USD")
    stdout(eth)
    stdout(n.cyan_text("________________________________________________/"))
    xrp = n.red_text("\n   ✕   Ripple Val: $" + str(crypto[2]) + " USD")
    stdout(xrp)
    stdout(n.cyan_text("________________________________________________/"))
    bch = n.red_text("\n   Ƀ   Bitcoin Cash Val: $" + str(crypto[3]) + " USD")
    stdout(bch)
    stdout(n.cyan_text("________________________________________________/"))
    ltc = n.red_text("\n   Ł   Litecoin Val: $" + str(crypto[4]) + " USD")
    stdout(ltc)
    stdout(n.cyan_text("________________________________________________/"))
    ada = n.red_text("\n   ₳   Cardano Val: $" + str(crypto[5]) + " USD")
    stdout(ada)
    stdout(n.cyan_text("________________________________________________/"))
    xmr = n.red_text("\n   ɱ   Monero Val: $" + str(crypto[6]) + " USD")
    stdout(xmr)
    stdout(n.cyan_text("________________________________________________/"))
    dash = n.red_text("\n   Đ   Dash Val: $" + str(crypto[7]) + " USD")
    stdout(dash)
    stdout(n.cyan_text("________________________________________________/"))
    ecl = n.red_text("\n   ξ   Ethereum Classic Val: $" + str(crypto[8]) + " USD")
    stdout(ecl)
    stdout(n.cyan_text("________________________________________________/"))
    tezos = n.red_text("\n   ꜩ   Tezos Val: $" + str(crypto[9]) + " USD")
    stdout(tezos)


main(n.purple_text(n.bold_text("🤖 Welcome, V0idMatr1x!\n")))