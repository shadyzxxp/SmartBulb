import asyncio

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', ' ': '/'
}

async def blink_morse(controller, message):
    for char in message.upper():
        if char not in MORSE_CODE_DICT:
            continue
        for symbol in MORSE_CODE_DICT[char]:
            if symbol == '.':
                await controller.turn_on()
                await asyncio.sleep(0.2)
            elif symbol == '-':
                await controller.turn_on()
                await asyncio.sleep(0.6)
            await controller.turn_off()
            await asyncio.sleep(0.2)
        await asyncio.sleep(0.6)