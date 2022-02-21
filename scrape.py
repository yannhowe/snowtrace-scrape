import requests
import json
import time
import os

apikey = os.environ['APIKEY']

pretty_data = os.environ['PRETTYJSON']

project_contract_addresses = [
    "0xA32608e873F9DdEF944B24798db69d80Bbb4d1ed", 
    "0xf693248F96Fe03422FEa95aC0aFbBBc4a8FdD172",
    "0xD2cd7a59Aa8f8FDc68d01b1e8A95747730b927d3",
    "0x1fA283b8C14e2d33e699cCe56Bf32b7cb2DB67d8",
    "0x1b7966315eF0259de890F38f1bDB95Acc03caCdD",
    "0x96DD95307295e2f72E6382Fc5130F1A8DB74042C",
    "0x4e57A39Cac2499aBeafd3698F7164eCBFde008eE",
    "0x49F6fC3f882e2Cd915E38bA377f8e977c11e0F66",
    "0x2BA9033E49EC1aa030fA46DE6d6793983945497E",
    "0x7E8DEef5bb861cF158d8BdaAa1c31f7B49922F49",
    "0x82a85407BD612f52577909F4A58bfC6873f14DA8",
    "0x431de0736f523c2d974b5698dbce2707871d04b6",
    "0x67B0eDd7a9FE9ca7dd74531187afa2b1D1114af0",
    "0xADCD1100b704c5fF816962a70b2fFD23D94e9818",
    "0x311C4670906989133629BCf0B67179E95DB5ecAf",
    "0x9b82d362626833938b7BB1c38d131D2C64D64bCd",
    "0x8C576A65d95EFB3F160d3A62B43CCfD9E0e3c59c",
    "0xc609985a1E79eb42219Aa5A1e32eE11f7F8B03de",
    "0x4B147403625A509b8DCd21d65889613686A65987",
    "0x0B6fE2C52A497bbCf5af5Ab4Cd86D41b25E5B7F7",
    "0x502f4bA72C4a8A372A058328997181851E2b00f1"
    ]

api_actions = [
    "tokentx",
    "txlist",
    "txlistinternal",
    "tokennfttx"
]

tic = time.perf_counter()

for address in project_contract_addresses:
    print("Scraping %s" % address)
    for action in api_actions:
        print("Getting " + action)
        params = (
            ('module', 'account'),
            ('action', action),
            ('address', address),
            ('startblock', '0'),
            ('endblock', '100000000'),
            ('sort', 'asc'),
            ('apikey', apikey),
        )

        response = requests.get('https://api.snowtrace.io/api', params=params)

        data = response.json()

        if not os.path.exists("output"):
            os.mkdir("output")

        if pretty_data:
            with open("./output/" + address + "_" + action + "_" + 'data-pretty.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        else:
            with open("./output/" + address + "_" + action + "_" + 'data.json', 'w') as f:
                json.dump(data, f)

        time.sleep(1)

toc = time.perf_counter()
print(f"Scraped in {toc - tic:0.4f} seconds, including 1s sleep")