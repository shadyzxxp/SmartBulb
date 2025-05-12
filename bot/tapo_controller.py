# import sys
# import os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# import asyncio
# import aiohttp
# import logging
# from kasa.iot import IotBulb
# from kasa import Discover
# from kasa.credentials import Credentials

# import settings

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# class TapoController:
#     def __init__(self):
#         self.bulb = None
#         self.credentials = Credentials(
#             username=settings.TAPO_EMAIL,
#             password=settings.TAPO_PASSWORD
#         )
#         self.ip = settings.TAPO_IP
#         self.session = None

#     async def initialize(self):
#         self.session = aiohttp.ClientSession()
#         try:
#             logger.info(f"Discovering bulb at {self.ip}")
#             devices = await Discover.discover(
#                 target=self.ip,
#                 username=self.credentials.username,
#                 password=self.credentials.password,
#                 timeout=15
#             )
#             logger.info(f"Devices found: {devices}")
#             self.bulb = devices.get(self.ip)
#             if not self.bulb:
#                 raise ValueError(f"Bulb not found at {self.ip}")
#             await self.bulb.update()
#             logger.info("Bulb initialized successfully")
#         except Exception as e:
#             logger.error(f"Discovery error: {e}")
#             await self.close()
#             raise

#     async def initialize_and_return(self):
#         await self.initialize()
#         return self

#     async def turn_on(self):
#         try:
#             await self.bulb.turn_on()
#             await self.bulb.update()
#         except ConnectionError as e:
#             logger.error(f"Connection error turning on bulb: {e}")
#             raise
#         except Exception as e:
#             logger.error(f"Error turning on bulb: {e}")
#             raise

#     async def turn_off(self):
#         try:
#             await self.bulb.turn_off()
#             await self.bulb.update()
#         except ConnectionError as e:
#             logger.error(f"Connection error turning off bulb: {e}")
#             raise
#         except Exception as e:
#             logger.error(f"Error turning off bulb: {e}")
#             raise

#     async def set_brightness(self, brightness: int):
#         try:
#             await self.bulb.set_brightness(brightness)
#             await self.bulb.update()
#         except ConnectionError as e:
#             logger.error(f"Connection error setting brightness: {e}")
#             raise
#         except Exception as e:
#             logger.error(f"Error setting brightness: {e}")
#             raise

#     async def set_color(self, hue: int, saturation: int):
#         try:
#             await self.bulb.set_hsv(hue, saturation, value=100)
#             await self.bulb.update()
#         except ConnectionError as e:
#             logger.error(f"Connection error setting color: {e}")
#             raise
#         except Exception as e:
#             logger.error(f"Error setting color: {e}")
#             raise

#     async def get_state(self):
#         try:
#             await self.bulb.update()
#             return {
#                 "is_on": self.bulb.is_on,
#                 "brightness": self.bulb.brightness,
#                 "hue": self.bulb.hsv[0],
#                 "saturation": self.bulb.hsv[1]
#             }
#         except ConnectionError as e:
#             logger.error(f"Connection error getting state: {e}")
#             raise
#         except Exception as e:
#             logger.error(f"Error getting state: {e}")
#             raise

#     async def close(self):
#         if self.bulb:
#             try:
#                 await self.bulb.protocol.close()
#             except Exception as e:
#                 logger.error(f"Error closing bulb connection: {e}")
#         if self.session:
#             try:
#                 await self.session.close()
#             except Exception as e:
#                 logger.error(f"Error closing aiohttp session: {e}")

#     def __del__(self):
#         # No automatic cleanup; should be done manually via close()
#         pass

# import sys
# import os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# from kasa.iot import IotBulb
# from kasa import Discover
# from kasa.credentials import Credentials
# import asyncio
# import settings
# import logging
# import aiohttp

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# class TapoController:
#     def __init__(self):
#         self.bulb = None
#         self.credentials = Credentials(
#             username=settings.TAPO_EMAIL,
#             password=settings.TAPO_PASSWORD
#         )
#         self.ip = settings.TAPO_IP
#         self.session = None

#     async def initialize(self):
#         self.session = aiohttp.ClientSession()
#         try:
#             logger.info(f"Discovering bulb at {self.ip}")
#             devices = await Discover.discover(
#                 target=self.ip,
#                 username=self.credentials.username,
#                 password=self.credentials.password,
#                 timeout=30  # Increased timeout
#             )
#             logger.info(f"Devices found: {devices}")
#             self.bulb = devices.get(self.ip)
#             if not self.bulb:
#                 raise ValueError(f"Bulb not found at {self.ip}")
#             await asyncio.create_task(self.bulb.update())
#             logger.info("Bulb initialized successfully")
#         except Exception as e:
#             logger.error(f"Discovery error: {e}")
#             await self.close()
#             raise

#     async def turn_on(self):
#         try:
#             await asyncio.create_task(self.bulb.turn_on())
#             await asyncio.create_task(self.bulb.update())
#         except ConnectionError as e:
#             logger.error(f"Connection error turning on bulb: {e}")
#             raise
#         except Exception as e:
#             logger.error(f"Error turning on bulb: {e}")
#             raise

#     async def turn_off(self):
#         try:
#             await asyncio.create_task(self.bulb.turn_off())
#             await asyncio.create_task(self.bulb.update())
#         except ConnectionError as e:
#             logger.error(f"Connection error turning off bulb: {e}")
#             raise
#         except Exception as e:
#             logger.error(f"Error turning off bulb: {e}")
#             raise

#     async def set_brightness(self, brightness: int):
#         try:
#             await asyncio.create_task(self.bulb.set_brightness(brightness))
#             await asyncio.create_task(self.bulb.update())
#         except ConnectionError as e:
#             logger.error(f"Connection error setting brightness: {e}")
#             raise
#         except Exception as e:
#             logger.error(f"Error setting brightness: {e}")
#             raise

#     async def set_color(self, hue: int, saturation: int):
#         try:
#             await asyncio.create_task(self.bulb.set_hsv(hue, saturation, value=100))
#             await asyncio.create_task(self.bulb.update())
#         except ConnectionError as e:
#             logger.error(f"Connection error setting color: {e}")
#             raise
#         except Exception as e:
#             logger.error(f"Error setting color: {e}")
#             raise

#     async def get_state(self):
#         try:
#             await asyncio.create_task(self.bulb.update())
#             return {
#                 "is_on": self.bulb.is_on,
#                 "brightness": self.bulb.brightness,
#                 "hue": self.bulb.hsv[0],
#                 "saturation": self.bulb.hsv[1]
#             }
#         except ConnectionError as e:
#             logger.error(f"Connection error getting state: {e}")
#             raise
#         except Exception as e:
#             logger.error(f"Error getting state: {e}")
#             raise

#     async def close(self):
#         if self.bulb:
#             try:
#                 await self.bulb.protocol.close()
#             except Exception as e:
#                 logger.error(f"Error closing bulb connection: {e}")
#         if self.session:
#             try:
#                 await self.session.close()
#             except Exception as e:
#                 logger.error(f"Error closing aiohttp session: {e}")

#     def __del__(self):
#         pass

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from kasa.iot import IotBulb
from kasa import Discover
from kasa.credentials import Credentials
import asyncio
import settings
import logging
import aiohttp

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TapoController:
    def __init__(self):
        self.bulb = None
        self.credentials = Credentials(
            username=settings.TAPO_EMAIL,
            password=settings.TAPO_PASSWORD
        )
        self.ip = settings.TAPO_IP
        self.session = None

    async def initialize(self):
        self.session = aiohttp.ClientSession()
        try:
            logger.info(f"Discovering bulb at {self.ip}")
            devices = await Discover.discover(
                target=self.ip,
                username=self.credentials.username,
                password=self.credentials.password,
                timeout=30
            )
            logger.info(f"Devices found: {devices}")
            self.bulb = devices.get(self.ip)
            if not self.bulb:
                raise ValueError(f"Bulb not found at {self.ip}")
            await self.bulb.update()
            logger.info("Bulb initialized successfully")
        except Exception as e:
            logger.error(f"Discovery error: {e}", exc_info=True)
            await self.close()
            raise

    async def turn_on(self):
        try:
            await self.bulb.turn_on()
            await self.bulb.update()
        except ConnectionError as e:
            logger.error(f"Connection error turning on bulb: {e}", exc_info=True)
            raise
        except Exception as e:
            logger.error(f"Error turning on bulb: {e}", exc_info=True)
            raise

    async def turn_off(self):
        try:
            await self.bulb.turn_off()
            await self.bulb.update()
        except ConnectionError as e:
            logger.error(f"Connection error turning off bulb: {e}", exc_info=True)
            raise
        except Exception as e:
            logger.error(f"Error turning off bulb: {e}", exc_info=True)
            raise

    async def set_brightness(self, brightness: int):
        try:
            await self.bulb.set_brightness(brightness)
            await self.bulb.update()
        except ConnectionError as e:
            logger.error(f"Connection error setting brightness: {e}", exc_info=True)
            raise
        except Exception as e:
            logger.error(f"Error setting brightness: {e}", exc_info=True)
            raise

    async def set_color(self, hue: int, saturation: int):
        try:
            await self.bulb.set_hsv(hue, saturation, value=100)
            await self.bulb.update()
        except ConnectionError as e:
            logger.error(f"Connection error setting color: {e}", exc_info=True)
            raise
        except Exception as e:
            logger.error(f"Error setting color: {e}", exc_info=True)
            raise

    async def get_state(self):
        try:
            await self.bulb.update()
            return {
                "is_on": self.bulb.is_on,
                "brightness": self.bulb.brightness,
                "hue": self.bulb.hsv[0],
                "saturation": self.bulb.hsv[1]
            }
        except ConnectionError as e:
            logger.error(f"Connection error getting state: {e}", exc_info=True)
            raise
        except Exception as e:
            logger.error(f"Error getting state: {e}", exc_info=True)
            raise

    async def close(self):
        if self.bulb:
            try:
                await self.bulb.protocol.close()
                logger.info("Bulb protocol closed")
            except Exception as e:
                logger.error(f"Error closing bulb connection: {e}", exc_info=True)
        if self.session:
            try:
                await self.session.close()
                logger.info("aiohttp session closed")
            except Exception as e:
                logger.error(f"Error closing aiohttp session: {e}", exc_info=True)
            self.session = None
        self.bulb = None

    def __del__(self):
        pass