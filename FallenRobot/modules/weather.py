import io

import aiohttp
from telethon.tl import functions, types

from FallenRobot import telethn as tbot
from FallenRobot.events import register


async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):
        return isinstance(
            (
                await tbot(functions.channels.GetParticipantRequest(chat, user))
            ).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator),
        )
    if isinstance(chat, types.InputPeerUser):
        return True


@register(pattern="^/weather (.*)")
async def _(event):
    if event.fwd_from:
        return

    sample_url = "https://wttr.in/{}.png"
    # logger.info(sample_url)
    input_str = event.pattern_match.group(1)
    async with aiohttp.ClientSession() as session:
        response_api_zero = await session.get(sample_url.format(input_str))
        # logger.info(response_api_zero)
        response_api = await response_api_zero.read()
        with io.BytesIO(response_api) as out_file:
            await event.reply(file=out_file)


__help__ = """
I can find weather of all cities

 ❍ /weather <city>*:* Advanced weather module, usage same as /weather
 ❍ /weather moon*:* Get the current status of moon
⏤͟͟͞͞•𓊈𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 ≛⃝🕊[@D3AD_B0Y](https://t.me/D3AD_B0Y)⛦⃕͜🇮🇳𓊉
"""

__mod_name__ = "⛈️𝐖𝐄𝐀𝐓𝐇𝐄𝐑☔"
