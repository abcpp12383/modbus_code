from pyModbusTCP.client import ModbusClient
import time

# Modbus TCP 從站的 IP 地址和端口
SERVER_HOST = "192.168.1.1"  # 請替換成實際的從站 IP 地址
SERVER_PORT = 502  # Modbus TCP 默認端口是 502

# Modbus TCP 從站的裝置地址
SLAVE_UNIT_ID = 1  # 從站的裝置地址，通常是1

# Modbus TCP 主站初始化
c = ModbusClient()
c.host(SERVER_HOST)
c.port(SERVER_PORT)
c.unit_id(SLAVE_UNIT_ID)

# 嘗試連接 Modbus TCP 從站
if not c.is_open():
    if not c.open():
        print("無法連接到 Modbus TCP 從站")
        exit()

try:
    # 要讀取的保持寄存器的起始地址和數量
    start_address = 0  # 起始地址，根據實際情況調整
    num_registers = 1  # 要讀取的保持寄存器數量，根據實際情況調整

    while True:
        # 使用 Modbus TCP 讀取保持寄存器數據
        result = c.read_holding_registers(start_address, num_registers)

        if result:
            # 讀取成功，打印數據
            print(f"保持寄存器 {start_address} 的數值為：{result}")
        else:
            print("讀取失敗")

        # 休眠一段時間，模擬頻率抓取
        time.sleep(1)

except Exception as e:
    print(f"發生錯誤：{e}")

finally:
    # 關閉 Modbus TCP 連接
    c.close()
    print("連接已關閉")
