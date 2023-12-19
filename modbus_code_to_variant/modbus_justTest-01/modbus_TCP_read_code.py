from pyModbusTCP.client import ModbusClient
import time
HOST1 = "192.168.0.109"
PORT1 = 502

HOST2 = "192.168.0.110"
PORT2 = 502

c1 = ModbusClient()
c2 = ModbusClient()

# uncomment this line to see debug message
#c1.debug(True)
#c2.debug(True)

# define modbus server host, port
c1.host(HOST1)
c1.port(PORT1)
#set UID to 1
c1.unit_id(1)

c2.host(HOST2)
c2.port(PORT2)
c2.unit_id(1)

while True:
    # open or reconnect TCP to server
    if not c1.is_open():
        if not c1.open():
            print("unable to connect to "+HOST1+":"+str(PORT1))

    if not c2.is_open():
        if not c2.open():
            print("unable to connect to "+HOST2+":"+str(PORT2))

    # if open() is ok, read register (modbus function 0x03)
    if c1.is_open() and c2.is_open():
        # read 32 registers at address 0, store result in regs list
        regs = c1.read_holding_registers(0, 32)
        if regs:
            #write regs) to c2 address 0 (32 registers)
            c2.write_multiple_registers(0,regs)
            #print(regs)
    # sleep 2s before next polling
    time.sleep(2)