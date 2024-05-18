import asyncio
import datetime

from lib.bot import RukmanBot
from lib.utils import TOKENS, logger


async def main() -> None:
    bot: RukmanBot = RukmanBot(api_id=TOKENS['api_id'], api_hash=TOKENS['api_hash'])
    while True:
        time_now: datetime.datetime = datetime.datetime.now()
        if 9 < time_now.hour and time_now.hour < 23:
            logger.info('Start')
            async with bot.client:
                async for message in bot.client.iter_messages(TOKENS['chat_id'], reverse=True):
                    if message.reactions is not None:
                        recent_reactions = message.reactions.recent_reactions
                        is_my_reaction: bool = True
                        for recent_reaction in recent_reactions:
                            if recent_reaction.peer_id.user_id == TOKENS['user_id']:
                                is_my_reaction = False
                        # message_date: datetime.datetime = message.date
                        # t1: datetime.datetime = datetime.datetime(2023, 10, 16)
                        # t2: datetime.datetime = datetime.datetime(2024, 4, 10)
                        # if is_my_reaction and (t1 < message_date < t2):
                        if is_my_reaction:
                            emoji: str = message.reactions.results[0].reaction.emoticon
                            try:
                                await bot.send_reaction(TOKENS['chat_id'], message.id, emoji)
                                logger.info(f'text: {message.message}')
                                logger.info(f'emoji: {emoji}')
                                logger.info(f'time: {datetime.datetime.now()}')
                            except Exception as e:
                                logger.error(e)
                            await asyncio.sleep(15)


if __name__ == '__main__':
    asyncio.run(main())
