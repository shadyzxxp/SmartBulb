from kasa.iot import IotBulb
from kasa import Discover
from kasa.credentials import Credentials
import asyncio

async def test_bulb():
    credentials = Credentials(
        username="shadyali237@gmail.com",
        password="pyl5302992"
    )
    devices = await Discover.discover(
        target="192.168.0.100",
        username=credentials.username,
        password=credentials.password
    )
    for ip, device in devices.items():
        await device.update()
        print(device.device_info)
        print("Turning on bulb...")
        await device.turn_on()
        await device.update()
        print("Bulb state:", device.is_on)
        return device
    for ip, device in devices.items():
        print("Found device at IP:", ip)



async def main():
    try:
        device = await test_bulb()
        if device:
            await device.protocol.close()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await asyncio.get_event_loop().shutdown_asyncgens()

if __name__ == "__main__":
    asyncio.run(main())