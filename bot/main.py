# import sys
# import os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# import settings
# from tapo_controller import TapoController
# from wave_mode import wave_mode
# from timed_mode import turn_on_for
# from morse_code import blink_morse
# from settings_manager import save_settings, load_settings
# from telegram.ext import Updater, CommandHandler
# import logging
# import nest_asyncio
# import asyncio

# nest_asyncio.apply()
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# def initialize_controller_sync():
#     loop = asyncio.get_event_loop()
#     return loop.run_until_complete(TapoController().initialize_and_return())

# def start(update, context):
#     logger.info("Received /start command")
#     update.message.reply_text("Welcome to Smart Light Bot!")

# def on(update, context):
#     try:
#         logger.info("Received /on command")
#         asyncio.run(controller.turn_on())
#         update.message.reply_text("Lamp turned ON")
#     except Exception as e:
#         logger.error(f"Error in /on: {e}")
#         update.message.reply_text(f"Error turning on lamp: {e}")

# def off(update, context):
#     try:
#         logger.info("Received /off command")
#         asyncio.run(controller.turn_off())
#         update.message.reply_text("Lamp turned OFF")
#     except Exception as e:
#         logger.error(f"Error in /off: {e}")
#         update.message.reply_text(f"Error turning off lamp: {e}")

# def wave(update, context):
#     try:
#         logger.info("Received /wave command")
#         asyncio.run(wave_mode(controller))
#         update.message.reply_text("Wave mode complete")
#     except Exception as e:
#         logger.error(f"Error in /wave: {e}")
#         update.message.reply_text(f"Error in wave mode: {e}")

# def timed(update, context):
#     try:
#         logger.info("Received /timed command")
#         seconds = int(context.args[0])
#         asyncio.create_task(turn_on_for(controller, seconds))
#         update.message.reply_text(f"Lamp will turn off in {seconds} seconds")
#     except IndexError:
#         update.message.reply_text("Usage: /timed <seconds>")
#     except ValueError:
#         update.message.reply_text("Please provide a valid number of seconds")
#     except Exception as e:
#         logger.error(f"Error in /timed: {e}")
#         update.message.reply_text(f"Error in timed mode: {e}")

# def morse(update, context):
#     try:
#         logger.info("Received /morse command")
#         msg = ' '.join(context.args)
#         if not msg:
#             update.message.reply_text("Usage: /morse <message>")
#             return
#         asyncio.run(blink_morse(controller, msg))
#         update.message.reply_text(f"Morse code sent: {msg}")
#     except Exception as e:
#         logger.error(f"Error in /morse: {e}")
#         update.message.reply_text(f"Error in morse mode: {e}")

# def save(update, context):
#     try:
#         logger.info("Received /save command")
#         state = asyncio.run(controller.get_state())
#         save_settings(state)
#         update.message.reply_text("Lamp settings saved")
#     except Exception as e:
#         logger.error(f"Error in /save: {e}")
#         update.message.reply_text(f"Error saving settings: {e}")

# def load(update, context):
#     try:
#         logger.info("Received /load command")
#         state = load_settings()
#         if state:
#             brightness = state.get("brightness")
#             if brightness is not None:
#                 asyncio.run(controller.set_brightness(brightness))
#             update.message.reply_text("Lamp settings loaded")
#         else:
#             update.message.reply_text("No saved settings found")
#     except Exception as e:
#         logger.error(f"Error in /load: {e}")
#         update.message.reply_text(f"Error loading settings: {e}")

# def main():
#     logger.info("Starting bot")
#     updater = Updater(settings.TELEGRAM_BOT_TOKEN, use_context=True)
#     dp = updater.dispatcher

#     global controller
#     controller = initialize_controller_sync()

#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(CommandHandler("on", on))
#     dp.add_handler(CommandHandler("off", off))
#     dp.add_handler(CommandHandler("wave", wave))
#     dp.add_handler(CommandHandler("timed", timed))
#     dp.add_handler(CommandHandler("morse", morse))
#     dp.add_handler(CommandHandler("save", save))
#     dp.add_handler(CommandHandler("load", load))

#     logger.info("Bot started, polling")
#     updater.start_polling()
#     updater.idle()

# if __name__ == "__main__":
#     main()

# import sys
# import os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# import settings
# from tapo_controller import TapoController
# from wave_mode import wave_mode
# from timed_mode import turn_on_for
# from morse_code import blink_morse
# from settings_manager import save_settings, load_settings
# from telegram.ext import Updater, CommandHandler
# from telegram.ext.dispatcher import run_async
# import logging
# import nest_asyncio
# import asyncio

# nest_asyncio.apply()
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# async def initialize_controller():
#     controller = TapoController()
#     await controller.initialize()
#     return controller

# @run_async
# async def start(update, context):
#     logger.info("Received /start command")
#     await update.message.reply_text("Welcome to Smart Light Bot!")

# @run_async
# async def on(update, context):
#     try:
#         logger.info("Received /on command")
#         await controller.turn_on()
#         await update.message.reply_text("Lamp turned ON")
#     except Exception as e:
#         logger.error(f"Error in /on: {e}")
#         await update.message.reply_text(f"Error turning on lamp: {e}")

# @run_async
# async def off(update, context):
#     try:
#         logger.info("Received /off command")
#         await controller.turn_off()
#         await update.message.reply_text("Lamp turned OFF")
#     except Exception as e:
#         logger.error(f"Error in /off: {e}")
#         await update.message.reply_text(f"Error turning off lamp: {e}")

# @run_async
# async def wave(update, context):
#     try:
#         logger.info("Received /wave command")
#         await wave_mode(controller)
#         await update.message.reply_text("Wave mode complete")
#     except Exception as e:
#         logger.error(f"Error in /wave: {e}")
#         await update.message.reply_text(f"Error in wave mode: {e}")

# @run_async
# async def timed(update, context):
#     try:
#         logger.info("Received /timed command")
#         seconds = int(context.args[0])
#         asyncio.create_task(turn_on_for(controller, seconds))
#         await update.message.reply_text(f"Lamp will turn off in {seconds} seconds")
#     except IndexError:
#         await update.message.reply_text("Usage: /timed <seconds>")
#     except ValueError:
#         await update.message.reply_text("Please provide a valid number of seconds")
#     except Exception as e:
#         logger.error(f"Error in /timed: {e}")
#         await update.message.reply_text(f"Error in timed mode: {e}")

# @run_async
# async def morse(update, context):
#     try:
#         logger.info("Received /morse command")
#         msg = ' '.join(context.args)
#         if not msg:
#             await update.message.reply_text("Usage: /morse <message>")
#             return
#         await blink_morse(controller, msg)
#         await update.message.reply_text(f"Morse code sent: {msg}")
#     except Exception as e:
#         logger.error(f"Error in /morse: {e}")
#         await update.message.reply_text(f"Error in morse mode: {e}")

# @run_async
# async def save(update, context):
#     try:
#         logger.info("Received /save command")
#         state = await controller.get_state()
#         save_settings(state)
#         await update.message.reply_text("Lamp settings saved")
#     except Exception as e:
#         logger.error(f"Error in /save: {e}")
#         await update.message.reply_text(f"Error saving settings: {e}")

# @run_async
# async def load(update, context):
#     try:
#         logger.info("Received /load command")
#         state = load_settings()
#         if state:
#             brightness = state.get("brightness")
#             if brightness is not None:
#                 await controller.set_brightness(brightness)
#             await update.message.reply_text("Lamp settings loaded")
#         else:
#             await update.message.reply_text("No saved settings found")
#     except Exception as e:
#         logger.error(f"Error in /load: {e}")
#         await update.message.reply_text(f"Error loading settings: {e}")

# def main():
#     logger.info("Starting bot")
#     updater = Updater(settings.TELEGRAM_BOT_TOKEN, use_context=True)
#     dp = updater.dispatcher

#     global controller
#     controller = asyncio.run(initialize_controller())

#     dp.add_handler(CommandHandler("start", start, run_async=True))
#     dp.add_handler(CommandHandler("off", off, run_async=True))
#     dp.add_handler(CommandHandler("on", on, run_async=True))
#     dp.add_handler(CommandHandler("wave", wave, run_async=True))
#     dp.add_handler(CommandHandler("timed", timed, run_async=True))
#     dp.add_handler(CommandHandler("morse", morse, run_async=True))
#     dp.add_handler(CommandHandler("save", save, run_async=True))
#     dp.add_handler(CommandHandler("load", load, run_async=True))

#     logger.info("Bot started, polling")
#     updater.start_polling()
#     updater.idle()

# if __name__ == "__main__":
#     main()

import sys
import os
import signal
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import settings
from tapo_controller import TapoController
from wave_mode import wave_mode
from timed_mode import turn_on_for
from morse_code import blink_morse
from settings_manager import save_settings, load_settings
from telegram.ext import Application, CommandHandler
import logging
import nest_asyncio
import asyncio


nest_asyncio.apply()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def initialize_controller():
    controller = TapoController()
    await controller.initialize()
    return controller

async def start(update, context):
    logger.info("Received /start command")
    await update.message.reply_text("Welcome to Smart Light Bot!")

async def on(update, context):
    try:
        logger.info("Received /on command")
        await controller.turn_on()
        await update.message.reply_text("Lamp turned ON")
    except Exception as e:
        logger.error(f"Error in /on: {e}", exc_info=True)
        await update.message.reply_text(f"Error turning on lamp: {e}")

async def off(update, context):
    try:
        logger.info("Received /off command")
        await controller.turn_off()
        await update.message.reply_text("Lamp turned OFF")
    except Exception as e:
        logger.error(f"Error in /off: {e}", exc_info=True)
        await update.message.reply_text(f"Error turning off lamp: {e}")

async def wave(update, context):
    try:
        logger.info("Received /wave command")
        await wave_mode(controller)
        await update.message.reply_text("Wave mode complete")
    except Exception as e:
        logger.error(f"Error in /wave: {e}", exc_info=True)
        await update.message.reply_text(f"Error in wave mode: {e}")

async def timed(update, context):
    try:
        logger.info("Received /timed command")
        seconds = int(context.args[0])
        asyncio.create_task(turn_on_for(controller, seconds))
        await update.message.reply_text(f"Lamp will turn off in {seconds} seconds")
    except IndexError:
        await update.message.reply_text("Usage: /timed <seconds>")
    except ValueError:
        await update.message.reply_text("Please provide a valid number of seconds")
    except Exception as e:
        logger.error(f"Error in /timed: {e}", exc_info=True)
        await update.message.reply_text(f"Error in timed mode: {e}")

async def morse(update, context):
    try:
        logger.info("Received /morse command")
        msg = ' '.join(context.args)
        if not msg:
            await update.message.reply_text("Usage: /morse <message>")
            return
        await blink_morse(controller, msg)
        await update.message.reply_text(f"Morse code sent: {msg}")
    except Exception as e:
        logger.error(f"Error in /morse: {e}", exc_info=True)
        await update.message.reply_text(f"Error in morse mode: {e}")

async def save(update, context):
    try:
        logger.info("Received /save command")
        state = await controller.get_state()
        save_settings(state)
        await update.message.reply_text("Lamp settings saved")
    except Exception as e:
        logger.error(f"Error in /save: {e}", exc_info=True)
        await update.message.reply_text(f"Error saving settings: {e}")

async def load(update, context):
    try:
        logger.info("Received /load command")
        state = load_settings()
        if state:
            brightness = state.get("brightness")
            if brightness is not None:
                await controller.set_brightness(brightness)
            await update.message.reply_text("Lamp settings loaded")
        else:
            await update.message.reply_text("No saved settings found")
    except Exception as e:
        logger.error(f"Error in /load: {e}", exc_info=True)
        await update.message.reply_text(f"Error loading settings: {e}")

async def set_commands(application):
    await application.bot.set_my_commands([
        ("start", "Start the bot"),
        ("on", "Turn on the lamp"),
        ("off", "Turn off the lamp"),
        ("wave", "Run wave mode"),
        ("timed", "Turn on for X seconds"),
        ("morse", "Blink Morse code"),
        ("save", "Save lamp settings"),
        ("load", "Load lamp settings")
    ])

async def main():
    logger.info("Starting bot")
    application = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).job_queue(None).build()

    global controller
    controller = await initialize_controller()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("on", on))
    application.add_handler(CommandHandler("off", off))
    application.add_handler(CommandHandler("wave", wave))
    application.add_handler(CommandHandler("timed", timed))
    application.add_handler(CommandHandler("morse", morse))
    application.add_handler(CommandHandler("save", save))
    application.add_handler(CommandHandler("load", load))

    await set_commands(application)

    def stop_and_cleanup(signum, frame):
        logger.info("Received shutdown signal, cleaning up...")
        application.stop()
        asyncio.run(controller.close())
        logger.info("Bot stopped cleanly")
        raise SystemExit

    signal.signal(signal.SIGINT, stop_and_cleanup)
    signal.signal(signal.SIGTERM, stop_and_cleanup)

    logger.info("Bot started, polling")
    await application.run_polling()
    await application.stop()
    await controller.close()

if __name__ == "__main__":
    asyncio.run(main())