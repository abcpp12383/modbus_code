from pyModbusTCP.client import ModbusClient
import time

# 定義 Modbus 伺服器的地址和端口：
# 定義了兩個 Modbus 伺服器的地址和端口。
HOST1 = "192.168.0.109"
PORT1 = 502

HOST2 = "192.168.0.110"
PORT2 = 502
#  創建 ModbusClient 對象：
c1 = ModbusClient()
c2 = ModbusClient()
# 創建了兩個 ModbusClient 對象，用於與兩個不同的 Modbus 伺服器通信。


# uncomment this line to see debug message
#c1.debug(True)
#c2.debug(True)

# 設置 ModbusClient 對象的屬性：
# define modbus server host, port
c1.host(HOST1)
c1.port(PORT1)
#set UID to 1
c1.unit_id(1)

c2.host(HOST2)
c2.port(PORT2)
c2.unit_id(1)
# 建立連接並進行 Modbus 操作：
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

    # 進入無窮迴圈，檢查並建立到兩個 Modbus 伺服器的連接。如果連接成功，
    # 則從第一個伺服器讀取 32 個保持寄存器的值，然後將這些值寫入到第二個伺服器的相應地址。
    # 在每次迴圈之後，暫停 2 秒（time.sleep(2)），然後進行下一次的 Modbus 操作。

    # 總的來說，這段代碼實現了一個簡單的 Modbus 數據複製程序，定期讀取一個 Modbus 伺服器的數據，
    # 然後將這些數據寫入到另一個 Modbus 伺服器。