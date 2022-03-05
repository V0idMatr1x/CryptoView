import os
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
        t1 = x.add_task(n.red_text(d), total=11)  # Task: 1
        t2 = x.add_task(n.green_text(c), total=12)
        t3 = x.add_task(n.cyan_text(a), total=13)
        t4 = x.add_task(n.purple_text(e), total=14)

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
        "🚀 :: Establishing connection to API...\n",
        "🌎 :: Gathering Data...\n",
        "🔍 :: Analyzing Data...\n",
        "🎬 :: Outputting Data to Terminal...\n",
    )
    _ = n.clear("clear")

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
        cg.get_price(ids="ethereum-classic", vs_currencies="usd")["ethereum-classic"][
            "usd"
        ],
        cg.get_price(ids="nem", vs_currencies="usd")["nem"]["usd"],
        cg.get_price(ids="tron", vs_currencies="usd")["tron"]["usd"],
        cg.get_price(ids="tezos", vs_currencies="usd")["tezos"]["usd"],
    ]

    # Panel Title
    stdout(n.bold_text(n.green_text(">> Crypto Prices 📈" + "\n")))

    btc = n.red_text("\n 💸 Bitcoin Val: $" + str(crypto[0]) + " USD")
    stdout(btc)
    print(n.cyan_text("________________________________________________/"))
    eth = n.red_text("\n 💸 Ethereum Val: $" + str(crypto[1]) + " USD")
    stdout(eth)
    print(n.cyan_text("________________________________________________/"))
    xrp = n.red_text("\n 💸 Ripple Val: $" + str(crypto[2]) + " USD")
    stdout(xrp)
    print(n.cyan_text("________________________________________________/"))
    bch = n.red_text("\n 💸 Bitcoin Cash Val: $" + str(crypto[3]) + " USD")
    stdout(bch)
    print(n.cyan_text("________________________________________________/"))
    ltc = n.red_text("\n 💸 Litecoin Val: $" + str(crypto[4]) + " USD")
    stdout(ltc)
    print(n.cyan_text("________________________________________________/"))
    ada = n.red_text("\n 💸 Cardano Val: $" + str(crypto[5]) + " USD")
    stdout(ada)
    print(n.cyan_text("________________________________________________/"))
    xlm = n.red_text("\n 💸 Stellar Val: $" + str(crypto[6]) + " USD")
    stdout(xlm)
    print(n.cyan_text("________________________________________________/"))
    xmr = n.red_text("\n 💸 Monero Val: $" + str(crypto[7]) + " USD")
    stdout(xmr)
    print(n.cyan_text("________________________________________________/"))
    dash = n.red_text("\n 💸 Dash Val: $" + str(crypto[8]) + " USD")
    stdout(dash)
    print(n.cyan_text("________________________________________________/"))
    iota = n.red_text("\n 💸 Iota Val: $" + str(crypto[9]) + " USD")
    stdout(iota)
    print(n.cyan_text("________________________________________________/"))
    ecl = n.red_text("\n 💸 Ethereum Classic Val: $" + str(crypto[10]) + " USD")
    stdout(ecl)
    print(n.cyan_text("________________________________________________/"))
    nem = n.red_text("\n 💸 NEM Val: $" + str(crypto[11]) + " USD")
    stdout(nem)
    print(n.cyan_text("________________________________________________/"))
    trx = n.red_text("\n 💸 Tron Val: $" + str(crypto[12]) + " USD")
    stdout(trx)
    print(n.cyan_text("________________________________________________/"))
    tezos = n.red_text("\n 💸 Tezos Val: $" + str(crypto[13]) + " USD")
    stdout(tezos)
    print(n.cyan_text("________________________________________________/"))


main(n.purple_text(n.bold_text("🤖 Welcome, V0idMatr1x!\n")))