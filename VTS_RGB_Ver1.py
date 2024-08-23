import pyvts
import asyncio
import json
import websockets
import time
import os


plugin_info = {
    "plugin_name": "VTS_RGB",
    "developer": "SpikedKirby",
    "authentication_token_path": "./token.txt"
}

async def main():
    
    vts = pyvts.vts(plugin_info)
        #load config
    absolute_path = os.path.dirname(__file__)
    relative_path = "config.json"
    full_path = os.path.join(absolute_path, relative_path)

    with open(full_path) as f:
        config = json.load(f)
        print(config)
    rainbow_timer= config['rainbow_timer']
    rainbow_hotkey = config['hotkeyName']

    await connect_auth(vts)
    await vts.connect()
    await vts.request_authenticate()
    while True:
        await subscribe(vts)
        if await trigger(vts,rainbow_hotkey):
            #await animate(vts)
            await color(vts,rainbow_timer)
            await vts.close()
    


# Read hotkeypress 
async def trigger(vts, rainbow_hotkey): 
    if vts.get_connection_status() != 1:
        await vts.connect()
        await vts.request_authenticate()
    print(vts.get_connection_status())
    RTA = await vts.websocket.recv()
    hotkeyname = json.loads(RTA)
    if hotkeyname['data']['hotkeyName'] == rainbow_hotkey:
        print(RTA,type(RTA))
        return True
    else:
        return False

    

#connect to Vtube ask for token
async def connect_auth(vts):
    await vts.connect()
    try :
        await vts.read_token()
        print( "token found")
    except:
        await vts.request_authenticate_token()  # get token
        print( "token written")
        await vts.write_token()
    await vts.request_authenticate()  # use token 

    await vts.close()


# Trigger hotkey
async def animate(vts):

    response_data = await vts.request(vts.vts_request.requestHotKeyList())
    hotkey_list = []
    for hotkey in response_data['data']['availableHotkeys']:
        hotkey_list.append(hotkey['name'])
    print(hotkey_list) # ['My Animation 1', 'My Animation 2', ...]
    
   
#Play animation hotkey request
    send_hotkey_request = vts.vts_request.requestTriggerHotKey(hotkey_list[1])
    await vts.request(send_hotkey_request) # send request to play 'My Animation 1'


#Read Mesh and color 

async def color(vts,rainbow_timer):
    
    #Read Mesh
    #response_mesh = await vts.request(vts.vts_request.BaseRequest(message_type="ArtMeshListRequest"))
    #mesh_list = []
    #mesh_list.append(response_mesh['data']['artMeshNames'])
    #print(response_mesh)
    
    
#open mesh files

    absolute_path = os.path.dirname(__file__)
    relative_path = "meshes.txt"
    full_path = os.path.join(absolute_path, relative_path)
    
    try:
        with open(full_path) as file_in:
            lines = []
            for line in file_in:
                lines.append(line)
    except: 
        print("mesh file not found")

#color tint
    
    send_color_tint_request = vts.vts_request.ColorTintRequest(red=100, green=100, blue=100, alpha=255,jeb=True, tint_all=False, name_exact = lines) 
    response_color = await vts.request(send_color_tint_request) # color
#Timer rainbow lasts
    time.sleep(rainbow_timer)

# Subscribe to event 
async def subscribe(vts):
    await vts.connect()
    await vts.request_authenticate()

    event = vts.vts_request.eventSubscription(event_name='HotkeyTriggeredEvent', on=True, cfg={"ignoreHotkeysTriggeredByAPI": False})
    event_response = await vts.event_subscribe(event)



#RUUUUUUUUUUN
if __name__ == "__main__":
    asyncio.run(main())   
