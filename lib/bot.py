from telethon import TelegramClient
from telethon import functions, types

from typing import List


class RukmanBot:
    def __init__(self, api_id: int, api_hash: str) -> None:
        self.client = TelegramClient('my_session', api_id=api_id, api_hash=api_hash, system_version='4.16.30-vxCUSTOM')

    async def send_message(self, chat_id: int, message: str) -> None:
        async with self.client:
            await self.client.send_message(entity=chat_id, message=message)

    async def get_messages(self, chat_id: int) -> List:
        async with self.client:
            return await self.client.get_messages(chat_id)

    async def send_reaction(self, chat_id: int, message_id: int, reaction: str) -> None:
        async with self.client:
            await self.client(functions.messages.SendReactionRequest(
                    peer=chat_id,
                    msg_id=message_id,
                    reaction=[types.ReactionEmoji(
                        emoticon=reaction
                    )]
                ))
