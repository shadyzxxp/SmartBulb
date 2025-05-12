import asyncio

async def turn_on_for(controller, seconds):
    await controller.turn_on()
    await asyncio.sleep(seconds)
    await controller.turn_off()