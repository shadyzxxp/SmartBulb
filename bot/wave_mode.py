import asyncio

async def wave_mode(controller):
    # Example wave effect
    for b in range(10, 101, 30):
        await controller.set_brightness(b)
        await asyncio.sleep(0.5)
    for b in range(100, 9, -30):
        await controller.set_brightness(b)
        await asyncio.sleep(0.5)
