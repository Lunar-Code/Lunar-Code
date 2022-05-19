from pypresence import Presence
import time
client_id = "975823272182677554"
RPC = Presence(client_id=client_id)
RPC.connect()

RPC.update(large_image="moon", large_text="Lunar Code Editing")
RPC.update(small_text="Editing the lunar way")
start_time=time.time()
RPC.update(start=start_time)
while True:
    time.sleep(15)