from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.payload import BinaryPayloadDecoder, BinaryPayloadBuilder
from pymodbus.constants import Endian
# from pymodbus.client.sync import ModbusUdpClient as ModbusClient
# from pymodbus.client.sync import ModbusSerialClient as ModbusClient

UNIT = 0x1
def write_float_to_register(client,address,value):
    builder= BinaryPayloadBuilder(byteorder=Endian.Big, wordorder=Endian.Little)
    builder.add_32bit_float(value)
    payload=builder.build()
    client.write_registers(address,payload,skip_encode=True)
    return payload

def run_sync_client():
    client = ModbusClient('localhost', port=5020)
    client.connect()

    payload=write_float_to_register(client,1,8)
    payload=write_float_to_register(client,5,9.4)
    payload=write_float_to_register(client,10,6.4)

    read_value=client.read_holding_registers(1,2)
    real_decoder=BinaryPayloadDecoder.fromRegisters(read_value.registers,byteorder=Endian.Big,wordorder=Endian.Little)
    value=real_decoder.decode_32bit_float()
    print(value)

    # close the client
    client.close()



if __name__ == "__main__":
    run_sync_client()
