from pypresence import Presence
import time
import json

with open('./config.json') as f:
    config = json.load(f)

RPC = Presence(config['client_id'])
print('Loaded client_id from config.json')
RPC.connect()
print('Connected to RPC.')

if config['rpc']['time']:
    if config['rpc']['custom_time']:
        RPC.update(
            state=config['rpc']['state'],
            details=config['rpc']['details'],
            start=config['rpc']['start'],
            # end=config['rpc']['end']
            large_image=config['rpc']['large_image'],
            large_text=config['rpc']['large_text'],
            small_image=config['rpc']['small_image'],
            small_text=config['rpc']['small_text'],
            # party_id=config['rpc']['party_id'],
            # party_size=config['rpc']['party_size'],
            # join=config['rpc']['join'],
            # spectate=config['rpc']['spectate'],
            # match=config['rpc']['match'],
            # instance=config['rpc']['instance']
        )
    else:
        RPC.update(
            state=config['rpc']['state'],
            details=config['rpc']['details'],
            start=time.time(),
            # end=config['rpc']['end']
            large_image=config['rpc']['large_image'],
            large_text=config['rpc']['large_text'],
            small_image=config['rpc']['small_image'],
            small_text=config['rpc']['small_text'],
            # party_id=config['rpc']['party_id'],
            # party_size=config['rpc']['party_size'],
            # join=config['rpc']['join'],
            # spectate=config['rpc']['spectate'],
            # match=config['rpc']['match'],
            # instance=config['rpc']['instance']
        )
else:
    RPC.update(
        state=config['rpc']['state'],
        details=config['rpc']['details'],
        large_image=config['rpc']['large_image'],
        large_text=config['rpc']['large_text'],
        small_image=config['rpc']['small_image'],
        small_text=config['rpc']['small_text'],
        # party_id=config['rpc']['party_id'],
        # party_size=config['rpc']['party_size'],
        # join=config['rpc']['join'],
        # spectate=config['rpc']['spectate'],
        # match=config['rpc']['match'],
        # instance=config['rpc']['instance']
    )
print('Custom status set.')

while True:
    time.sleep(15)
