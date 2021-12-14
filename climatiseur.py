from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.payload import BinaryPayloadDecoder, BinaryPayloadBuilder
from pymodbus.constants import Endian
# from pymodbus.client.sync import ModbusUdpClient as ModbusClient
# from pymodbus.client.sync import ModbusSerialClient as ModbusClient

UNIT = 0x1

def read_float_from_register(client, address):
    read_value=client.read_holding_registers(address,2)
    real_decoder=BinaryPayloadDecoder.fromRegisters(read_value.registers,byteorder=Endian.Big,wordorder=Endian.Little)
    value=real_decoder.decode_32bit_float()
    return value

def run_sync_client():
    client = ModbusClient('localhost', port=5020)
    client.connect()
    #------------------------------
    addresses=[1,5,10]
    values=[]
    state=0
    for element in range(len(addresses)):
        reading=read_float_from_register(client,addresses[element])
        values.append(reading)
        if reading>30:
            state=1

    message="on" if state else "off"
    print(message)
    

    # close the client
    client.close()



if __name__ == "__main__":
    run_sync_client()
