from __future__ import annotations
import httpx
import asyncio
import json
import logging
from typing import TYPE_CHECKING
from .exceptions import TelegramBadRequestError, TelegramUnauthorizedError, TelegramNetworkError, TelegramAPIError

if TYPE_CHECKING:
    from .objects.accepted_gift_types import AcceptedGiftTypes
    from .objects.bot_access_settings import BotAccessSettings
    from .objects.bot_command import BotCommand
    from .objects.bot_command_scope import BotCommandScope
    from .objects.bot_description import BotDescription
    from .objects.bot_name import BotName
    from .objects.bot_short_description import BotShortDescription
    from .objects.business_connection import BusinessConnection
    from .objects.chat_administrator_rights import ChatAdministratorRights
    from .objects.chat_full_info import ChatFullInfo
    from .objects.chat_invite_link import ChatInviteLink
    from .objects.chat_member import ChatMember
    from .objects.chat_permissions import ChatPermissions
    from .objects.ephemeral_message_parameters import EphemeralMessageParameters
    from .objects.file import File
    from .objects.force_reply import ForceReply
    from .objects.forum_topic import ForumTopic
    from .objects.game_high_score import GameHighScore
    from .objects.gifts import Gifts
    from .objects.inline_keyboard_markup import InlineKeyboardMarkup
    from .objects.inline_query_result import InlineQueryResult
    from .objects.inline_query_results_button import InlineQueryResultsButton
    from .objects.input_checklist import InputChecklist
    from .objects.input_file import InputFile
    from .objects.input_media import InputMedia
    from .objects.input_media_audio import InputMediaAudio
    from .objects.input_media_document import InputMediaDocument
    from .objects.input_media_live_photo import InputMediaLivePhoto
    from .objects.input_media_photo import InputMediaPhoto
    from .objects.input_media_video import InputMediaVideo
    from .objects.input_paid_media import InputPaidMedia
    from .objects.input_poll_media import InputPollMedia
    from .objects.input_poll_option import InputPollOption
    from .objects.input_profile_photo import InputProfilePhoto
    from .objects.input_rich_message import InputRichMessage
    from .objects.input_sticker import InputSticker
    from .objects.input_story_content import InputStoryContent
    from .objects.keyboard_button import KeyboardButton
    from .objects.labeled_price import LabeledPrice
    from .objects.link_preview_options import LinkPreviewOptions
    from .objects.mask_position import MaskPosition
    from .objects.menu_button import MenuButton
    from .objects.message import Message
    from .objects.message_entity import MessageEntity
    from .objects.message_id import MessageId
    from .objects.owned_gifts import OwnedGifts
    from .objects.passport_element_error import PassportElementError
    from .objects.poll import Poll
    from .objects.prepared_inline_message import PreparedInlineMessage
    from .objects.prepared_keyboard_button import PreparedKeyboardButton
    from .objects.reaction_type import ReactionType
    from .objects.reply_keyboard_markup import ReplyKeyboardMarkup
    from .objects.reply_keyboard_remove import ReplyKeyboardRemove
    from .objects.reply_parameters import ReplyParameters
    from .objects.sent_guest_message import SentGuestMessage
    from .objects.sent_web_app_message import SentWebAppMessage
    from .objects.shipping_option import ShippingOption
    from .objects.star_amount import StarAmount
    from .objects.star_transactions import StarTransactions
    from .objects.sticker import Sticker
    from .objects.sticker_set import StickerSet
    from .objects.story import Story
    from .objects.story_area import StoryArea
    from .objects.suggested_post_parameters import SuggestedPostParameters
    from .objects.update import Update
    from .objects.user import User
    from .objects.user_chat_boosts import UserChatBoosts
    from .objects.user_profile_audios import UserProfileAudios
    from .objects.user_profile_photos import UserProfilePhotos
    from .objects.webhook_info import WebhookInfo


logger = logging.getLogger("teleasync")

class TelegramBot:
    def __init__(self, token: str, client: httpx.AsyncClient | None = None):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}"
        self.file_url = f"https://api.telegram.org/file/bot{token}"
        self._client = client
        self._owns_client = client is None

        if len(token) > 10:
            self.masked_token = f"{token[:6]}...{token[-4:]}"
        else:
            self.masked_token = "***"
            
        logger.info(f"Initialize Telegram Bot with token: {self.masked_token}")

    async def get_client(self) -> httpx.AsyncClient:
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(timeout=60.0)
        return self._client

    async def close(self):
        if self._owns_client and self._client and not self._client.is_closed:
            await self._client.aclose()

    async def request(self, method_name: str, params: dict | None = None, files: dict | None = None) -> dict:
        url = f"{self.base_url}/{method_name}"
        if params:
            cleaned_params = {}
            for k, v in params.items():
                if v is not None:
                    if hasattr(v, 'to_dict'):
                        v = v.to_dict()
                    elif isinstance(v, list):
                        v = [i.to_dict() if hasattr(i, 'to_dict') else i for i in v]

                    if isinstance(v, (dict, list)):
                        v = json.dumps(v)

                    original_key = k[:-1] if k.endswith('_') and k[:-1] in ['from', 'photo', 'video', 'document', 'audio', 'sticker', 'animation', 'voice'] else k
                    cleaned_params[original_key] = v
            params = cleaned_params
        
        client = await self.get_client()
        
        try:
            if files:
                response = await client.post(url, data=params, files=files)
            else:
                response = await client.post(url, json=params)
        except httpx.RequestError as e:
            raise TelegramNetworkError(f"Network error during request to {method_name}: {e}")

        try:
            data_json = response.json()
            logger.debug(f"DEBUG API [{method_name}] Content: {data_json}")
        except Exception:
            raise TelegramAPIError("Received an invalid JSON response from the Telegram server.")

        if not isinstance(data_json, dict):
            if isinstance(data_json, list):
                return data_json
            raise TelegramAPIError(f"Received an invalid response format from Telegram: {data_json}")

        if not data_json.get("ok", False):
            error_code = data_json.get("error_code")
            description = data_json.get("description", "Unknown error")
            
            if error_code == 401:
                raise TelegramUnauthorizedError(f"Authorization error: {description}", error_code)
            elif error_code == 400:
                raise TelegramBadRequestError(f"Bad request: {description}", error_code)
            else:
                raise TelegramAPIError(f"API error [{error_code}]: {description}", error_code)

        return data_json.get("result")

    async def download_file(self, file_path: str, destination_path: str) -> None:
        url = f"{self.file_url}/{file_path}"
        client = await self.get_client()
        try:
            async with client.stream("GET", url) as response:
                if response.status_code == 200:
                    with open(destination_path, 'wb') as f:
                        async for chunk in response.aiter_bytes(chunk_size=8192):
                            f.write(chunk)
                else:
                    raise TelegramAPIError(f"Failed to download file. Status code: {response.status_code}")
        except httpx.RequestError as e:
            raise TelegramNetworkError(f"Network error while downloading file: {e}")

    async def start_polling_from(self, router, interval: float = 1.0) -> None:
        offset = 0
        bot_username = "Unknown Bot"

        try:
            me = await self.get_me()
            if isinstance(me, dict) and "username" in me:
                bot_username = f"@{me['username']}"
            elif hasattr(me, "username") and me.username:
                bot_username = f"@{me.username}"
        except Exception:
            pass

        logger.info("\n%s", "-" * 50)
        logger.info("Bot [%s] started!", bot_username)
        logger.info("Polling for updates... (Press CTRL+C to stop)")
        logger.info("%s\n", "-" * 50)

        try:
            while True:
                try:
                    updates = await self.get_updates(offset=offset, timeout=30)

                    if updates:
                        if not isinstance(updates, list):
                            updates = [updates]

                        for update in updates:
                            sub_items = update if isinstance(update, list) else [update]

                            for item in sub_items:
                                if isinstance(item, dict):
                                    offset = item.get("update_id", offset) + 1
                                    await router.feed(item)
                                elif hasattr(item, "update_id"):
                                    offset = getattr(item, "update_id", offset) + 1
                                    await router.feed(item.to_dict() if hasattr(item, "to_dict") else item)
                                else:
                                    await router.feed(item)

                except asyncio.CancelledError:
                    raise
                except Exception as e:
                    import traceback
                    logger.error(f"⚠️ Polling error detail: {e}\n{traceback.format_exc()}")

                await asyncio.sleep(interval)
        finally:
            await self.close()
            logger.info("\n%s", "-" * 50)
            logger.info("Polling for [@%s] stopped gracefully. Goodbye!", bot_username)
            logger.info("%s", "-" * 50)

    # --- Telegram API Methods ---
    
    async def get_updates(self, offset: int | None = None, limit: int | None = None, timeout: int | None = None, allowed_updates: list[str] | None = None) -> list[Update]:
        """Use this method to receive incoming updates using long polling (wiki). Returns an Array of Update objects."""
        payload = {
            'offset': offset,
            'limit': limit,
            'timeout': timeout,
            'allowed_updates': allowed_updates,
        }
        return await self.request('getUpdates', payload)

    
    async def set_webhook(self, url: str, certificate: InputFile | None = None, ip_address: str | None = None, max_connections: int | None = None, allowed_updates: list[str] | None = None, drop_pending_updates: bool | None = None, secret_token: str | None = None) -> bool:
        """Use this method to specify a URL and receive incoming updates via an outgoing webhook. Whenever there is an update for the bot, we will send an HTTPS POST request to the specified URL, containing a JSON-serialized Update. In case of an unsuccessful request (a request with response HTTP status code different from 2XY), we will repeat the request and give up after a reasonable amount of attempts. Returns True on success. If you'd like to make sure that the webhook was set by you, you can specify secret data in the parameter secret_token. If specified, the request will contain a header "X-Telegram-Bot-Api-Secret-Token" with the secret token as content."""
        payload = {
            'url': url,
            'certificate': certificate,
            'ip_address': ip_address,
            'max_connections': max_connections,
            'allowed_updates': allowed_updates,
            'drop_pending_updates': drop_pending_updates,
            'secret_token': secret_token,
        }
        return await self.request('setWebhook', payload)

    
    async def delete_webhook(self, drop_pending_updates: bool | None = None) -> bool:
        """Use this method to remove webhook integration if you decide to switch back to getUpdates. Returns True on success."""
        payload = {
            'drop_pending_updates': drop_pending_updates,
        }
        return await self.request('deleteWebhook', payload)

    
    async def get_webhook_info(self) -> WebhookInfo:
        """Use this method to get current webhook status. Requires no parameters. On success, returns a WebhookInfo object. If the bot is using getUpdates, will return an object with the url field empty."""
        payload = {
        }
        return await self.request('getWebhookInfo', payload)

    
    async def get_me(self) -> User:
        """A simple method for testing your bot's authentication token. Requires no parameters. Returns basic information about the bot in form of a User object."""
        payload = {
        }
        return await self.request('getMe', payload)

    
    async def log_out(self) -> bool:
        """Use this method to log out from the cloud Bot API server before launching the bot locally. You must log out the bot before running it locally, otherwise there is no guarantee that the bot will receive updates. After a successful call, you can immediately log in on a local server, but will not be able to log in back to the cloud Bot API server for 10 minutes. Returns True on success. Requires no parameters."""
        payload = {
        }
        return await self.request('logOut', payload)

    
    async def close(self) -> bool:
        """Use this method to close the bot instance before moving it from one local server to another. You need to delete the webhook before calling this method to ensure that the bot isn't launched again after server restart. The method will return error 429 in the first 10 minutes after the bot is launched. Returns True on success. Requires no parameters."""
        payload = {
        }
        return await self.request('close', payload)

    
    async def send_message(self, chat_id: int | str, text: str, business_connection_id: str | None = None, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, ephemeral_message_parameters: EphemeralMessageParameters | None = None, parse_mode: str | None = None, entities: list[MessageEntity] | None = None, link_preview_options: LinkPreviewOptions | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: ReplyKeyboardMarkup | ForceReply | ReplyKeyboardRemove | InlineKeyboardMarkup | None = None) -> Message:
        """Use this method to send text messages. On success, the sent Message is returned."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'direct_messages_topic_id': direct_messages_topic_id,
            'ephemeral_message_parameters': ephemeral_message_parameters,
            'text': text,
            'parse_mode': parse_mode,
            'entities': entities,
            'link_preview_options': link_preview_options,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'suggested_post_parameters': suggested_post_parameters,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup,
        }
        return await self.request('sendMessage', payload)

    
    async def forward_message(self, chat_id: int | str, from_chat_id: int | str, message_id: int, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, video_start_timestamp: int | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None) -> Message:
        """Use this method to forward messages of any kind. Service messages and messages with protected content can't be forwarded. On success, the sent Message is returned."""
        payload = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'direct_messages_topic_id': direct_messages_topic_id,
            'from_chat_id': from_chat_id,
            'video_start_timestamp': video_start_timestamp,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'message_effect_id': message_effect_id,
            'suggested_post_parameters': suggested_post_parameters,
            'message_id': message_id,
        }
        return await self.request('forwardMessage', payload)

    
    async def forward_messages(self, chat_id: int | str, from_chat_id: int | str, message_ids: list[int], message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, disable_notification: bool | None = None, protect_content: bool | None = None) -> list[MessageId]:
        """Use this method to forward multiple messages of any kind. If some of the specified messages can't be found or forwarded, they are skipped. Service messages and messages with protected content can't be forwarded. Album grouping is kept for forwarded messages. On success, an Array of MessageId of the sent messages is returned."""
        payload = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'direct_messages_topic_id': direct_messages_topic_id,
            'from_chat_id': from_chat_id,
            'message_ids': message_ids,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
        }
        return await self.request('forwardMessages', payload)

    
    async def copy_message(self, chat_id: int | str, from_chat_id: int | str, message_id: int, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, video_start_timestamp: int | None = None, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, show_caption_above_media: bool | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: ReplyKeyboardMarkup | ForceReply | ReplyKeyboardRemove | InlineKeyboardMarkup | None = None) -> MessageId:
        """Use this method to copy messages of any kind. Service messages, paid media messages, giveaway messages, giveaway winners messages, and invoice messages can't be copied. A quiz poll can be copied only if the value of the field correct_option_ids is known to the bot. The method is analogous to the method forwardMessage, but the copied message doesn't have a link to the original message. Returns the MessageId of the sent message on success."""
        payload = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'direct_messages_topic_id': direct_messages_topic_id,
            'from_chat_id': from_chat_id,
            'message_id': message_id,
            'video_start_timestamp': video_start_timestamp,
            'caption': caption,
            'parse_mode': parse_mode,
            'caption_entities': caption_entities,
            'show_caption_above_media': show_caption_above_media,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'suggested_post_parameters': suggested_post_parameters,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup,
        }
        return await self.request('copyMessage', payload)

    
    async def copy_messages(self, chat_id: int | str, from_chat_id: int | str, message_ids: list[int], message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, remove_caption: bool | None = None) -> list[MessageId]:
        """Use this method to copy messages of any kind. If some of the specified messages can't be found or copied, they are skipped. Service messages, paid media messages, giveaway messages, giveaway winners messages, and invoice messages can't be copied. A quiz poll can be copied only if the value of the field correct_option_ids is known to the bot. The method is analogous to the method forwardMessages, but the copied messages don't have a link to the original message. Album grouping is kept for copied messages. On success, an Array of MessageId of the sent messages is returned."""
        payload = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'direct_messages_topic_id': direct_messages_topic_id,
            'from_chat_id': from_chat_id,
            'message_ids': message_ids,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'remove_caption': remove_caption,
        }
        return await self.request('copyMessages', payload)

    
    async def send_photo(self, chat_id: int | str, photo_: InputFile | str, business_connection_id: str | None = None, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, ephemeral_message_parameters: EphemeralMessageParameters | None = None, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, show_caption_above_media: bool | None = None, has_spoiler: bool | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: ReplyKeyboardMarkup | ForceReply | ReplyKeyboardRemove | InlineKeyboardMarkup | None = None) -> Message:
        """Use this method to send photos. On success, the sent Message is returned."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'direct_messages_topic_id': direct_messages_topic_id,
            'ephemeral_message_parameters': ephemeral_message_parameters,
            'caption': caption,
            'parse_mode': parse_mode,
            'caption_entities': caption_entities,
            'show_caption_above_media': show_caption_above_media,
            'has_spoiler': has_spoiler,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'suggested_post_parameters': suggested_post_parameters,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup,
        }
        files = {
            'photo': photo_,
        }
        files = {k: v for k, v in files.items() if v is not None}
        return await self.request('sendPhoto', payload, files=files if files else None)

    
    async def send_live_photo(self, chat_id: int | str, live_photo: InputFile | str, photo_: InputFile | str, business_connection_id: str | None = None, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, ephemeral_message_parameters: EphemeralMessageParameters | None = None, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, show_caption_above_media: bool | None = None, has_spoiler: bool | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: ReplyKeyboardMarkup | ForceReply | ReplyKeyboardRemove | InlineKeyboardMarkup | None = None) -> Message:
        """Use this method to send live photos. On success, the sent Message is returned."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'direct_messages_topic_id': direct_messages_topic_id,
            'ephemeral_message_parameters': ephemeral_message_parameters,
            'live_photo': live_photo,
            'caption': caption,
            'parse_mode': parse_mode,
            'caption_entities': caption_entities,
            'show_caption_above_media': show_caption_above_media,
            'has_spoiler': has_spoiler,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'suggested_post_parameters': suggested_post_parameters,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup,
        }
        files = {
            'photo': photo_,
        }
        files = {k: v for k, v in files.items() if v is not None}
        return await self.request('sendLivePhoto', payload, files=files if files else None)

    
    async def send_audio(self, chat_id: int | str, audio_: InputFile | str, business_connection_id: str | None = None, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, ephemeral_message_parameters: EphemeralMessageParameters | None = None, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, duration: int | None = None, performer: str | None = None, title: str | None = None, thumbnail: InputFile | str | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: ReplyKeyboardMarkup | ForceReply | ReplyKeyboardRemove | InlineKeyboardMarkup | None = None) -> Message:
        """Use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .MP3 or .M4A format. On success, the sent Message is returned. Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future. For sending voice messages, use the sendVoice method instead."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'direct_messages_topic_id': direct_messages_topic_id,
            'ephemeral_message_parameters': ephemeral_message_parameters,
            'caption': caption,
            'parse_mode': parse_mode,
            'caption_entities': caption_entities,
            'duration': duration,
            'performer': performer,
            'title': title,
            'thumbnail': thumbnail,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'suggested_post_parameters': suggested_post_parameters,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup,
        }
        files = {
            'audio': audio_,
        }
        files = {k: v for k, v in files.items() if v is not None}
        return await self.request('sendAudio', payload, files=files if files else None)

    
    async def send_document(self, chat_id: int | str, document_: InputFile | str, business_connection_id: str | None = None, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, ephemeral_message_parameters: EphemeralMessageParameters | None = None, thumbnail: InputFile | str | None = None, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, disable_content_type_detection: bool | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: ReplyKeyboardMarkup | ForceReply | ReplyKeyboardRemove | InlineKeyboardMarkup | None = None) -> Message:
        """Use this method to send general files. On success, the sent Message is returned. Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'direct_messages_topic_id': direct_messages_topic_id,
            'ephemeral_message_parameters': ephemeral_message_parameters,
            'thumbnail': thumbnail,
            'caption': caption,
            'parse_mode': parse_mode,
            'caption_entities': caption_entities,
            'disable_content_type_detection': disable_content_type_detection,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'suggested_post_parameters': suggested_post_parameters,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup,
        }
        files = {
            'document': document_,
        }
        files = {k: v for k, v in files.items() if v is not None}
        return await self.request('sendDocument', payload, files=files if files else None)

    
    async def send_video(self, chat_id: int | str, video_: InputFile | str, business_connection_id: str | None = None, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, ephemeral_message_parameters: EphemeralMessageParameters | None = None, duration: int | None = None, width: int | None = None, height: int | None = None, thumbnail: InputFile | str | None = None, cover: InputFile | str | None = None, start_timestamp: int | None = None, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, show_caption_above_media: bool | None = None, has_spoiler: bool | None = None, supports_streaming: bool | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: ReplyKeyboardMarkup | ForceReply | ReplyKeyboardRemove | InlineKeyboardMarkup | None = None) -> Message:
        """Use this method to send video files, Telegram clients support MPEG4 videos (other formats may be sent as Document). On success, the sent Message is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'direct_messages_topic_id': direct_messages_topic_id,
            'ephemeral_message_parameters': ephemeral_message_parameters,
            'duration': duration,
            'width': width,
            'height': height,
            'thumbnail': thumbnail,
            'cover': cover,
            'start_timestamp': start_timestamp,
            'caption': caption,
            'parse_mode': parse_mode,
            'caption_entities': caption_entities,
            'show_caption_above_media': show_caption_above_media,
            'has_spoiler': has_spoiler,
            'supports_streaming': supports_streaming,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'suggested_post_parameters': suggested_post_parameters,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup,
        }
        files = {
            'video': video_,
        }
        files = {k: v for k, v in files.items() if v is not None}
        return await self.request('sendVideo', payload, files=files if files else None)

    
    async def send_animation(self, chat_id: int | str, animation_: InputFile | str, business_connection_id: str | None = None, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, ephemeral_message_parameters: EphemeralMessageParameters | None = None, duration: int | None = None, width: int | None = None, height: int | None = None, thumbnail: InputFile | str | None = None, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, show_caption_above_media: bool | None = None, has_spoiler: bool | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: ReplyKeyboardMarkup | ForceReply | ReplyKeyboardRemove | InlineKeyboardMarkup | None = None) -> Message:
        """Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound). On success, the sent Message is returned. Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'direct_messages_topic_id': direct_messages_topic_id,
            'ephemeral_message_parameters': ephemeral_message_parameters,
            'duration': duration,
            'width': width,
            'height': height,
            'thumbnail': thumbnail,
            'caption': caption,
            'parse_mode': parse_mode,
            'caption_entities': caption_entities,
            'show_caption_above_media': show_caption_above_media,
            'has_spoiler': has_spoiler,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'suggested_post_parameters': suggested_post_parameters,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup,
        }
        files = {
            'animation': animation_,
        }
        files = {k: v for k, v in files.items() if v is not None}
        return await self.request('sendAnimation', payload, files=files if files else None)

    
    async def send_voice(self, chat_id: int | str, voice_: InputFile | str, business_connection_id: str | None = None, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, ephemeral_message_parameters: EphemeralMessageParameters | None = None, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, duration: int | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: ReplyKeyboardMarkup | ForceReply | ReplyKeyboardRemove | InlineKeyboardMarkup | None = None) -> Message:
        """Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS, or in .MP3 format, or in .M4A format (other formats may be sent as Audio or Document). On success, the sent Message is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'direct_messages_topic_id': direct_messages_topic_id,
            'ephemeral_message_parameters': ephemeral_message_parameters,
            'caption': caption,
            'parse_mode': parse_mode,
            'caption_entities': caption_entities,
            'duration': duration,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'suggested_post_parameters': suggested_post_parameters,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup,
        }
        files = {
            'voice': voice_,
        }
        files = {k: v for k, v in files.items() if v is not None}
        return await self.request('sendVoice', payload, files=files if files else None)

    
    async def send_video_note(self, chat_id: int | str, video_note: InputFile | str, business_connection_id: str | None = None, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, ephemeral_message_parameters: EphemeralMessageParameters | None = None, duration: int | None = None, length: int | None = None, thumbnail: InputFile | str | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: ReplyKeyboardMarkup | ForceReply | ReplyKeyboardRemove | InlineKeyboardMarkup | None = None) -> Message:
        """Use this method to send a rounded square MPEG4 video of up to 1 minute long. On success, the sent Message is returned."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'direct_messages_topic_id': direct_messages_topic_id,
            'ephemeral_message_parameters': ephemeral_message_parameters,
            'video_note': video_note,
            'duration': duration,
            'length': length,
            'thumbnail': thumbnail,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'suggested_post_parameters': suggested_post_parameters,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup,
        }
        return await self.request('sendVideoNote', payload)

    
    async def send_paid_media(self, chat_id: int | str, star_count: int, media: list[InputPaidMedia], business_connection_id: str | None = None, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, payload: str | None = None, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, show_caption_above_media: bool | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: ReplyKeyboardMarkup | ForceReply | ReplyKeyboardRemove | InlineKeyboardMarkup | None = None) -> Message:
        """Use this method to send paid media. On success, the sent Message is returned."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'direct_messages_topic_id': direct_messages_topic_id,
            'star_count': star_count,
            'media': media,
            'payload': payload,
            'caption': caption,
            'parse_mode': parse_mode,
            'caption_entities': caption_entities,
            'show_caption_above_media': show_caption_above_media,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'suggested_post_parameters': suggested_post_parameters,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup,
        }
        return await self.request('sendPaidMedia', payload)

    
    async def send_media_group(self, chat_id: int | str, media: list[InputMediaPhoto] | list[InputMediaVideo] | list[InputMediaLivePhoto] | list[InputMediaAudio] | list[InputMediaDocument], business_connection_id: str | None = None, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, reply_parameters: ReplyParameters | None = None) -> list[Message]:
        """Use this method to send a group of photos, live photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type. On success, an Array of Message objects that were sent is returned."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'direct_messages_topic_id': direct_messages_topic_id,
            'media': media,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'reply_parameters': reply_parameters,
        }
        return await self.request('sendMediaGroup', payload)

    
    async def send_location(self, chat_id: int | str, latitude: float, longitude: float, business_connection_id: str | None = None, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, ephemeral_message_parameters: EphemeralMessageParameters | None = None, horizontal_accuracy: float | None = None, live_period: int | None = None, heading: int | None = None, proximity_alert_radius: int | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: ReplyKeyboardMarkup | ForceReply | ReplyKeyboardRemove | InlineKeyboardMarkup | None = None) -> Message:
        """Use this method to send point on the map. On success, the sent Message is returned."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'direct_messages_topic_id': direct_messages_topic_id,
            'ephemeral_message_parameters': ephemeral_message_parameters,
            'latitude': latitude,
            'longitude': longitude,
            'horizontal_accuracy': horizontal_accuracy,
            'live_period': live_period,
            'heading': heading,
            'proximity_alert_radius': proximity_alert_radius,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'suggested_post_parameters': suggested_post_parameters,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup,
        }
        return await self.request('sendLocation', payload)

    
    async def send_venue(self, chat_id: int | str, latitude: float, longitude: float, title: str, address: str, business_connection_id: str | None = None, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, ephemeral_message_parameters: EphemeralMessageParameters | None = None, foursquare_id: str | None = None, foursquare_type: str | None = None, google_place_id: str | None = None, google_place_type: str | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: ReplyKeyboardMarkup | ForceReply | ReplyKeyboardRemove | InlineKeyboardMarkup | None = None) -> Message:
        """Use this method to send information about a venue. On success, the sent Message is returned."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'direct_messages_topic_id': direct_messages_topic_id,
            'ephemeral_message_parameters': ephemeral_message_parameters,
            'latitude': latitude,
            'longitude': longitude,
            'title': title,
            'address': address,
            'foursquare_id': foursquare_id,
            'foursquare_type': foursquare_type,
            'google_place_id': google_place_id,
            'google_place_type': google_place_type,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'suggested_post_parameters': suggested_post_parameters,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup,
        }
        return await self.request('sendVenue', payload)

    
    async def send_contact(self, chat_id: int | str, phone_number: str, first_name: str, business_connection_id: str | None = None, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, ephemeral_message_parameters: EphemeralMessageParameters | None = None, last_name: str | None = None, vcard: str | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: ReplyKeyboardMarkup | ForceReply | ReplyKeyboardRemove | InlineKeyboardMarkup | None = None) -> Message:
        """Use this method to send phone contacts. On success, the sent Message is returned."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'direct_messages_topic_id': direct_messages_topic_id,
            'ephemeral_message_parameters': ephemeral_message_parameters,
            'phone_number': phone_number,
            'first_name': first_name,
            'last_name': last_name,
            'vcard': vcard,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'suggested_post_parameters': suggested_post_parameters,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup,
        }
        return await self.request('sendContact', payload)

    
    async def send_poll(self, chat_id: int | str, question: str, options: list[InputPollOption], business_connection_id: str | None = None, message_thread_id: int | None = None, question_parse_mode: str | None = None, question_entities: list[MessageEntity] | None = None, is_anonymous: bool | None = None, type: str | None = None, allows_multiple_answers: bool | None = None, allows_revoting: bool | None = None, shuffle_options: bool | None = None, allow_adding_options: bool | None = None, hide_results_until_closes: bool | None = None, members_only: bool | None = None, country_codes: list[str] | None = None, correct_option_ids: list[int] | None = None, explanation: str | None = None, explanation_parse_mode: str | None = None, explanation_entities: list[MessageEntity] | None = None, explanation_media: InputPollMedia | None = None, open_period: int | None = None, close_date: int | None = None, is_closed: bool | None = None, description: str | None = None, description_parse_mode: str | None = None, description_entities: list[MessageEntity] | None = None, media: InputPollMedia | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: ReplyKeyboardMarkup | ForceReply | ReplyKeyboardRemove | InlineKeyboardMarkup | None = None) -> Message:
        """Use this method to send a native poll. On success, the sent Message is returned."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'question': question,
            'question_parse_mode': question_parse_mode,
            'question_entities': question_entities,
            'options': options,
            'is_anonymous': is_anonymous,
            'type': type,
            'allows_multiple_answers': allows_multiple_answers,
            'allows_revoting': allows_revoting,
            'shuffle_options': shuffle_options,
            'allow_adding_options': allow_adding_options,
            'hide_results_until_closes': hide_results_until_closes,
            'members_only': members_only,
            'country_codes': country_codes,
            'correct_option_ids': correct_option_ids,
            'explanation': explanation,
            'explanation_parse_mode': explanation_parse_mode,
            'explanation_entities': explanation_entities,
            'explanation_media': explanation_media,
            'open_period': open_period,
            'close_date': close_date,
            'is_closed': is_closed,
            'description': description,
            'description_parse_mode': description_parse_mode,
            'description_entities': description_entities,
            'media': media,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup,
        }
        return await self.request('sendPoll', payload)

    
    async def send_checklist(self, business_connection_id: str, chat_id: int | str, checklist: InputChecklist, disable_notification: bool | None = None, protect_content: bool | None = None, message_effect_id: str | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: InlineKeyboardMarkup | None = None) -> Message:
        """Use this method to send a checklist on behalf of a connected business account. On success, the sent Message is returned."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'checklist': checklist,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'message_effect_id': message_effect_id,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup,
        }
        return await self.request('sendChecklist', payload)

    
    async def send_dice(self, chat_id: int | str, business_connection_id: str | None = None, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, emoji: str | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: ReplyKeyboardMarkup | ForceReply | ReplyKeyboardRemove | InlineKeyboardMarkup | None = None) -> Message:
        """Use this method to send an animated emoji that will display a random value. On success, the sent Message is returned."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'direct_messages_topic_id': direct_messages_topic_id,
            'emoji': emoji,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'suggested_post_parameters': suggested_post_parameters,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup,
        }
        return await self.request('sendDice', payload)

    
    async def send_message_draft(self, chat_id: int, draft_id: int, message_thread_id: int | None = None, text: str | None = None, parse_mode: str | None = None, entities: list[MessageEntity] | None = None, can_stop: bool | None = None, keep_on_stop: bool | None = None) -> bool:
        """Use this method to stream a partial message to a user while the message is being generated. Note that the streamed draft is ephemeral and acts as a temporary 30-second preview - once the output is finalized, you must call sendMessage with the complete message to persist it in the user's chat. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'draft_id': draft_id,
            'text': text,
            'parse_mode': parse_mode,
            'entities': entities,
            'can_stop': can_stop,
            'keep_on_stop': keep_on_stop,
        }
        return await self.request('sendMessageDraft', payload)

    
    async def send_chat_action(self, chat_id: int | str, action: str, business_connection_id: str | None = None, message_thread_id: int | None = None) -> bool:
        """Use this method when you need to tell the user that something is happening on the bot's side. The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status). Returns True on success. We only recommend using this method when a response from the bot will take a noticeable amount of time to arrive."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'action': action,
        }
        return await self.request('sendChatAction', payload)

    
    async def set_message_reaction(self, chat_id: int | str, message_id: int, reaction: list[ReactionType] | None = None, is_big: bool | None = None) -> bool:
        """Use this method to change the chosen reactions on a message. Service messages of some types can't be reacted to. Automatically forwarded messages from a channel to its discussion group have the same available reactions as messages in the channel. Bots can't use paid reactions. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'message_id': message_id,
            'reaction': reaction,
            'is_big': is_big,
        }
        return await self.request('setMessageReaction', payload)

    
    async def get_user_profile_photos(self, user_id: int, offset: int | None = None, limit: int | None = None) -> UserProfilePhotos:
        """Use this method to get a list of profile pictures for a user. Returns a UserProfilePhotos object."""
        payload = {
            'user_id': user_id,
            'offset': offset,
            'limit': limit,
        }
        return await self.request('getUserProfilePhotos', payload)

    
    async def get_user_profile_audios(self, user_id: int, offset: int | None = None, limit: int | None = None) -> UserProfileAudios:
        """Use this method to get a list of profile audios for a user. Returns a UserProfileAudios object."""
        payload = {
            'user_id': user_id,
            'offset': offset,
            'limit': limit,
        }
        return await self.request('getUserProfileAudios', payload)

    
    async def set_user_emoji_status(self, user_id: int, emoji_status_custom_emoji_id: str | None = None, emoji_status_expiration_date: int | None = None) -> bool:
        """Changes the emoji status for a given user that previously allowed the bot to manage their emoji status via the Mini App method requestEmojiStatusAccess. Returns True on success."""
        payload = {
            'user_id': user_id,
            'emoji_status_custom_emoji_id': emoji_status_custom_emoji_id,
            'emoji_status_expiration_date': emoji_status_expiration_date,
        }
        return await self.request('setUserEmojiStatus', payload)

    
    async def get_file(self, file_id: str) -> File:
        """Use this method to get basic information about a file and prepare it for downloading. For the moment, bots can download files of up to 20MB in size. On success, a File object is returned. The file can then be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>, where <file_path> is taken from the response. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile again. Note: This function may not preserve the original file name and MIME type. You should save the file's MIME type and name (if available) when the File object is received."""
        payload = {
            'file_id': file_id,
        }
        return await self.request('getFile', payload)

    
    async def ban_chat_member(self, chat_id: int | str, user_id: int, until_date: int | None = None, revoke_messages: bool | None = None) -> bool:
        """Use this method to ban a user in a group, a supergroup or a channel. In the case of supergroups and channels, the user will not be able to return to the chat on their own using invite links, etc., unless unbanned first. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'user_id': user_id,
            'until_date': until_date,
            'revoke_messages': revoke_messages,
        }
        return await self.request('banChatMember', payload)

    
    async def unban_chat_member(self, chat_id: int | str, user_id: int, only_if_banned: bool | None = None) -> bool:
        """Use this method to unban a previously banned user in a supergroup or channel. The user will not return to the group or channel automatically, but will be able to join via link, etc. The bot must be an administrator for this to work. By default, this method guarantees that after the call the user is not a member of the chat, but will be able to join it. So if the user is a member of the chat they will also be removed from the chat. If you don't want this, use the parameter only_if_banned. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'user_id': user_id,
            'only_if_banned': only_if_banned,
        }
        return await self.request('unbanChatMember', payload)

    
    async def restrict_chat_member(self, chat_id: int | str, user_id: int, permissions: ChatPermissions, use_independent_chat_permissions: bool | None = None, until_date: int | None = None) -> bool:
        """Use this method to restrict a user in a supergroup. The bot must be an administrator in the supergroup for this to work and must have the appropriate administrator rights. Pass True for all permissions to lift restrictions from a user. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'user_id': user_id,
            'permissions': permissions,
            'use_independent_chat_permissions': use_independent_chat_permissions,
            'until_date': until_date,
        }
        return await self.request('restrictChatMember', payload)

    
    async def promote_chat_member(self, chat_id: int | str, user_id: int, is_anonymous: bool | None = None, can_manage_chat: bool | None = None, can_delete_messages: bool | None = None, can_manage_video_chats: bool | None = None, can_restrict_members: bool | None = None, can_promote_members: bool | None = None, can_change_info: bool | None = None, can_invite_users: bool | None = None, can_post_stories: bool | None = None, can_edit_stories: bool | None = None, can_delete_stories: bool | None = None, can_post_messages: bool | None = None, can_edit_messages: bool | None = None, can_pin_messages: bool | None = None, can_manage_topics: bool | None = None, can_manage_direct_messages: bool | None = None, can_manage_tags: bool | None = None, can_send_welcome_messages: bool | None = None) -> bool:
        """Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Pass False for all boolean parameters to demote a user. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'user_id': user_id,
            'is_anonymous': is_anonymous,
            'can_manage_chat': can_manage_chat,
            'can_delete_messages': can_delete_messages,
            'can_manage_video_chats': can_manage_video_chats,
            'can_restrict_members': can_restrict_members,
            'can_promote_members': can_promote_members,
            'can_change_info': can_change_info,
            'can_invite_users': can_invite_users,
            'can_post_stories': can_post_stories,
            'can_edit_stories': can_edit_stories,
            'can_delete_stories': can_delete_stories,
            'can_post_messages': can_post_messages,
            'can_edit_messages': can_edit_messages,
            'can_pin_messages': can_pin_messages,
            'can_manage_topics': can_manage_topics,
            'can_manage_direct_messages': can_manage_direct_messages,
            'can_manage_tags': can_manage_tags,
            'can_send_welcome_messages': can_send_welcome_messages,
        }
        return await self.request('promoteChatMember', payload)

    
    async def set_chat_administrator_custom_title(self, chat_id: int | str, user_id: int, custom_title: str) -> bool:
        """Use this method to set a custom title for an administrator in a supergroup promoted by the bot. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'user_id': user_id,
            'custom_title': custom_title,
        }
        return await self.request('setChatAdministratorCustomTitle', payload)

    
    async def set_chat_member_tag(self, chat_id: int | str, user_id: int, tag: str | None = None) -> bool:
        """Use this method to set a tag for a regular member in a group or a supergroup. The bot must be an administrator in the chat for this to work and must have the can_manage_tags administrator right. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'user_id': user_id,
            'tag': tag,
        }
        return await self.request('setChatMemberTag', payload)

    
    async def ban_chat_sender_chat(self, chat_id: int | str, sender_chat_id: int) -> bool:
        """Use this method to ban a channel chat in a supergroup or a channel. Until the chat is unbanned, the owner of the banned chat won't be able to send messages on behalf of any of their channels. The bot must be an administrator in the supergroup or channel for this to work and must have the appropriate administrator rights. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'sender_chat_id': sender_chat_id,
        }
        return await self.request('banChatSenderChat', payload)

    
    async def unban_chat_sender_chat(self, chat_id: int | str, sender_chat_id: int) -> bool:
        """Use this method to unban a previously banned channel chat in a supergroup or channel. The bot must be an administrator for this to work and must have the appropriate administrator rights. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'sender_chat_id': sender_chat_id,
        }
        return await self.request('unbanChatSenderChat', payload)

    
    async def set_chat_permissions(self, chat_id: int | str, permissions: ChatPermissions, use_independent_chat_permissions: bool | None = None) -> bool:
        """Use this method to set default chat permissions for all members. The bot must be an administrator in the group or a supergroup for this to work and must have the can_restrict_members administrator rights. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'permissions': permissions,
            'use_independent_chat_permissions': use_independent_chat_permissions,
        }
        return await self.request('setChatPermissions', payload)

    
    async def export_chat_invite_link(self, chat_id: int | str) -> str:
        """Use this method to generate a new primary invite link for a chat; any previously generated primary link is revoked. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the new invite link as String on success."""
        payload = {
            'chat_id': chat_id,
        }
        return await self.request('exportChatInviteLink', payload)

    
    async def create_chat_invite_link(self, chat_id: int | str, name: str | None = None, expire_date: int | None = None, member_limit: int | None = None, creates_join_request: bool | None = None) -> ChatInviteLink:
        """Use this method to create an additional invite link for a chat. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. The link can be revoked using the method revokeChatInviteLink. Returns the new invite link as ChatInviteLink object."""
        payload = {
            'chat_id': chat_id,
            'name': name,
            'expire_date': expire_date,
            'member_limit': member_limit,
            'creates_join_request': creates_join_request,
        }
        return await self.request('createChatInviteLink', payload)

    
    async def edit_chat_invite_link(self, chat_id: int | str, invite_link: str, name: str | None = None, expire_date: int | None = None, member_limit: int | None = None, creates_join_request: bool | None = None) -> ChatInviteLink:
        """Use this method to edit a non-primary invite link created by the bot. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the edited invite link as a ChatInviteLink object."""
        payload = {
            'chat_id': chat_id,
            'invite_link': invite_link,
            'name': name,
            'expire_date': expire_date,
            'member_limit': member_limit,
            'creates_join_request': creates_join_request,
        }
        return await self.request('editChatInviteLink', payload)

    
    async def create_chat_subscription_invite_link(self, chat_id: int | str, subscription_period: int, subscription_price: int, name: str | None = None) -> ChatInviteLink:
        """Use this method to create a subscription invite link for a channel chat. The bot must have the can_invite_users administrator rights. The link can be edited using the method editChatSubscriptionInviteLink or revoked using the method revokeChatInviteLink. Returns the new invite link as a ChatInviteLink object."""
        payload = {
            'chat_id': chat_id,
            'name': name,
            'subscription_period': subscription_period,
            'subscription_price': subscription_price,
        }
        return await self.request('createChatSubscriptionInviteLink', payload)

    
    async def edit_chat_subscription_invite_link(self, chat_id: int | str, invite_link: str, name: str | None = None) -> ChatInviteLink:
        """Use this method to edit a subscription invite link created by the bot. The bot must have the can_invite_users administrator rights. Returns the edited invite link as a ChatInviteLink object."""
        payload = {
            'chat_id': chat_id,
            'invite_link': invite_link,
            'name': name,
        }
        return await self.request('editChatSubscriptionInviteLink', payload)

    
    async def revoke_chat_invite_link(self, chat_id: int | str, invite_link: str) -> ChatInviteLink:
        """Use this method to revoke an invite link created by the bot. If the primary link is revoked, a new link is automatically generated. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the revoked invite link as ChatInviteLink object."""
        payload = {
            'chat_id': chat_id,
            'invite_link': invite_link,
        }
        return await self.request('revokeChatInviteLink', payload)

    
    async def approve_chat_join_request(self, chat_id: int | str, user_id: int) -> bool:
        """Use this method to approve a chat join request. The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'user_id': user_id,
        }
        return await self.request('approveChatJoinRequest', payload)

    
    async def decline_chat_join_request(self, chat_id: int | str, user_id: int) -> bool:
        """Use this method to decline a chat join request. The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'user_id': user_id,
        }
        return await self.request('declineChatJoinRequest', payload)

    
    async def answer_chat_join_request_query(self, chat_join_request_query_id: str, result: str) -> bool:
        """Use this method to process a received chat join request query. Returns True on success."""
        payload = {
            'chat_join_request_query_id': chat_join_request_query_id,
            'result': result,
        }
        return await self.request('answerChatJoinRequestQuery', payload)

    
    async def send_chat_join_request_web_app(self, chat_join_request_query_id: str, web_app_url: str) -> bool:
        """Use this method to process a received chat join request query by showing a Mini App to the user before deciding the outcome. Call answerChatJoinRequestQuery to resolve the join request query based on the user interaction with the Mini App. Returns True on success."""
        payload = {
            'chat_join_request_query_id': chat_join_request_query_id,
            'web_app_url': web_app_url,
        }
        return await self.request('sendChatJoinRequestWebApp', payload)

    
    async def set_chat_photo(self, chat_id: int | str, photo_: InputFile) -> bool:
        """Use this method to set a new profile photo for the chat. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
        payload = {
            'chat_id': chat_id,
        }
        files = {
            'photo': photo_,
        }
        files = {k: v for k, v in files.items() if v is not None}
        return await self.request('setChatPhoto', payload, files=files if files else None)

    
    async def delete_chat_photo(self, chat_id: int | str) -> bool:
        """Use this method to delete a chat photo. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
        payload = {
            'chat_id': chat_id,
        }
        return await self.request('deleteChatPhoto', payload)

    
    async def set_chat_title(self, chat_id: int | str, title: str) -> bool:
        """Use this method to change the title of a chat. Titles can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'title': title,
        }
        return await self.request('setChatTitle', payload)

    
    async def set_chat_description(self, chat_id: int | str, description: str | None = None) -> bool:
        """Use this method to change the description of a group, a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'description': description,
        }
        return await self.request('setChatDescription', payload)

    
    async def pin_chat_message(self, chat_id: int | str, message_id: int, business_connection_id: str | None = None, disable_notification: bool | None = None) -> bool:
        """Use this method to add a message to the list of pinned messages in a chat. In private chats and channel direct messages chats, all non-service messages can be pinned. Conversely, the bot must be an administrator with the 'can_pin_messages' right or the 'can_edit_messages' right to pin messages in groups and channels respectively. Returns True on success."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_id': message_id,
            'disable_notification': disable_notification,
        }
        return await self.request('pinChatMessage', payload)

    
    async def unpin_chat_message(self, chat_id: int | str, business_connection_id: str | None = None, message_id: int | None = None) -> bool:
        """Use this method to remove a message from the list of pinned messages in a chat. In private chats and channel direct messages chats, all messages can be unpinned. Conversely, the bot must be an administrator with the 'can_pin_messages' right or the 'can_edit_messages' right to unpin messages in groups and channels respectively. Returns True on success."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_id': message_id,
        }
        return await self.request('unpinChatMessage', payload)

    
    async def unpin_all_chat_messages(self, chat_id: int | str) -> bool:
        """Use this method to clear the list of pinned messages in a chat. In private chats and channel direct messages chats, no additional rights are required to unpin all pinned messages. Conversely, the bot must be an administrator with the 'can_pin_messages' right or the 'can_edit_messages' right to unpin all pinned messages in groups and channels respectively. Returns True on success."""
        payload = {
            'chat_id': chat_id,
        }
        return await self.request('unpinAllChatMessages', payload)

    
    async def leave_chat(self, chat_id: int | str) -> bool:
        """Use this method for your bot to leave a group, supergroup or channel. Returns True on success."""
        payload = {
            'chat_id': chat_id,
        }
        return await self.request('leaveChat', payload)

    
    async def get_chat(self, chat_id: int | str) -> ChatFullInfo:
        """Use this method to get up-to-date information about the chat. Returns a ChatFullInfo object on success."""
        payload = {
            'chat_id': chat_id,
        }
        return await self.request('getChat', payload)

    
    async def get_chat_administrators(self, chat_id: int | str, return_bots: bool | None = None) -> list[ChatMember]:
        """Use this method to get a list of administrators in a chat. Returns an Array of ChatMember objects."""
        payload = {
            'chat_id': chat_id,
            'return_bots': return_bots,
        }
        return await self.request('getChatAdministrators', payload)

    
    async def get_chat_member_count(self, chat_id: int | str) -> int:
        """Use this method to get the number of members in a chat. Returns Integer on success."""
        payload = {
            'chat_id': chat_id,
        }
        return await self.request('getChatMemberCount', payload)

    
    async def get_chat_member(self, chat_id: int | str, user_id: int) -> ChatMember:
        """Use this method to get information about a member of a chat. The method is only guaranteed to work for other users if the bot is an administrator in the chat. Returns a ChatMember object on success."""
        payload = {
            'chat_id': chat_id,
            'user_id': user_id,
        }
        return await self.request('getChatMember', payload)

    
    async def get_user_personal_chat_messages(self, user_id: int, limit: int) -> list[Message]:
        """Use this method to get the last messages from the personal chat (i.e., the chat currently added to their profile) of a given user. On success, an Array of Message objects is returned."""
        payload = {
            'user_id': user_id,
            'limit': limit,
        }
        return await self.request('getUserPersonalChatMessages', payload)

    
    async def set_chat_sticker_set(self, chat_id: int | str, sticker_set_name: str) -> bool:
        """Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'sticker_set_name': sticker_set_name,
        }
        return await self.request('setChatStickerSet', payload)

    
    async def delete_chat_sticker_set(self, chat_id: int | str) -> bool:
        """Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success."""
        payload = {
            'chat_id': chat_id,
        }
        return await self.request('deleteChatStickerSet', payload)

    
    async def get_forum_topic_icon_stickers(self) -> list[Sticker]:
        """Use this method to get custom emoji stickers, which can be used as a forum topic icon by any user. Requires no parameters. Returns an Array of Sticker objects."""
        payload = {
        }
        return await self.request('getForumTopicIconStickers', payload)

    
    async def create_forum_topic(self, chat_id: int | str, name: str, icon_color: int | None = None, icon_custom_emoji_id: str | None = None) -> ForumTopic:
        """Use this method to create a topic in a forum supergroup chat or a private chat with a user. In the case of a supergroup chat the bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator right. Returns information about the created topic as a ForumTopic object."""
        payload = {
            'chat_id': chat_id,
            'name': name,
            'icon_color': icon_color,
            'icon_custom_emoji_id': icon_custom_emoji_id,
        }
        return await self.request('createForumTopic', payload)

    
    async def edit_forum_topic(self, chat_id: int | str, message_thread_id: int, name: str | None = None, icon_custom_emoji_id: str | None = None) -> bool:
        """Use this method to edit name and icon of a topic in a forum supergroup chat or a private chat with a user. In the case of a supergroup chat the bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights, unless it is the creator of the topic. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'name': name,
            'icon_custom_emoji_id': icon_custom_emoji_id,
        }
        return await self.request('editForumTopic', payload)

    
    async def close_forum_topic(self, chat_id: int | str, message_thread_id: int) -> bool:
        """Use this method to close an open topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights, unless it is the creator of the topic. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
        }
        return await self.request('closeForumTopic', payload)

    
    async def reopen_forum_topic(self, chat_id: int | str, message_thread_id: int) -> bool:
        """Use this method to reopen a closed topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights, unless it is the creator of the topic. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
        }
        return await self.request('reopenForumTopic', payload)

    
    async def delete_forum_topic(self, chat_id: int | str, message_thread_id: int) -> bool:
        """Use this method to delete a forum topic along with all its messages in a forum supergroup chat or a private chat with a user. In the case of a supergroup chat the bot must be an administrator in the chat for this to work and must have the can_delete_messages administrator rights. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
        }
        return await self.request('deleteForumTopic', payload)

    
    async def unpin_all_forum_topic_messages(self, chat_id: int | str, message_thread_id: int) -> bool:
        """Use this method to clear the list of pinned messages in a forum topic in a forum supergroup chat or a private chat with a user. In the case of a supergroup chat the bot must be an administrator in the chat for this to work and must have the can_pin_messages administrator right in the supergroup. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
        }
        return await self.request('unpinAllForumTopicMessages', payload)

    
    async def edit_general_forum_topic(self, chat_id: int | str, name: str) -> bool:
        """Use this method to edit the name of the 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'name': name,
        }
        return await self.request('editGeneralForumTopic', payload)

    
    async def close_general_forum_topic(self, chat_id: int | str) -> bool:
        """Use this method to close an open 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. Returns True on success."""
        payload = {
            'chat_id': chat_id,
        }
        return await self.request('closeGeneralForumTopic', payload)

    
    async def reopen_general_forum_topic(self, chat_id: int | str) -> bool:
        """Use this method to reopen a closed 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. The topic will be automatically unhidden if it was hidden. Returns True on success."""
        payload = {
            'chat_id': chat_id,
        }
        return await self.request('reopenGeneralForumTopic', payload)

    
    async def hide_general_forum_topic(self, chat_id: int | str) -> bool:
        """Use this method to hide the 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. The topic will be automatically closed if it was open. Returns True on success."""
        payload = {
            'chat_id': chat_id,
        }
        return await self.request('hideGeneralForumTopic', payload)

    
    async def unhide_general_forum_topic(self, chat_id: int | str) -> bool:
        """Use this method to unhide the 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. Returns True on success."""
        payload = {
            'chat_id': chat_id,
        }
        return await self.request('unhideGeneralForumTopic', payload)

    
    async def unpin_all_general_forum_topic_messages(self, chat_id: int | str) -> bool:
        """Use this method to clear the list of pinned messages in a General forum topic. The bot must be an administrator in the chat for this to work and must have the can_pin_messages administrator right in the supergroup. Returns True on success."""
        payload = {
            'chat_id': chat_id,
        }
        return await self.request('unpinAllGeneralForumTopicMessages', payload)

    
    async def answer_callback_query(self, callback_query_id: str, text: str | None = None, show_alert: bool | None = None, url: str | None = None, cache_time: int | None = None) -> bool:
        """Use this method to send answers to callback queries sent from inline keyboards. The answer will be displayed to the user as a notification at the top of the chat screen or as an alert. On success, True is returned."""
        payload = {
            'callback_query_id': callback_query_id,
            'text': text,
            'show_alert': show_alert,
            'url': url,
            'cache_time': cache_time,
        }
        return await self.request('answerCallbackQuery', payload)

    
    async def answer_guest_query(self, guest_query_id: str, result: InlineQueryResult) -> SentGuestMessage:
        """Use this method to reply to a received guest message. On success, a SentGuestMessage object is returned."""
        payload = {
            'guest_query_id': guest_query_id,
            'result': result,
        }
        return await self.request('answerGuestQuery', payload)

    
    async def get_user_chat_boosts(self, chat_id: int | str, user_id: int) -> UserChatBoosts:
        """Use this method to get the list of boosts added to a chat by a user. Requires administrator rights in the chat. Returns a UserChatBoosts object."""
        payload = {
            'chat_id': chat_id,
            'user_id': user_id,
        }
        return await self.request('getUserChatBoosts', payload)

    
    async def get_business_connection(self, business_connection_id: str) -> BusinessConnection:
        """Use this method to get information about the connection of the bot with a business account. Returns a BusinessConnection object on success."""
        payload = {
            'business_connection_id': business_connection_id,
        }
        return await self.request('getBusinessConnection', payload)

    
    async def get_managed_bot_token(self, user_id: int) -> str:
        """Use this method to get the token of a managed bot. Returns the token as String on success."""
        payload = {
            'user_id': user_id,
        }
        return await self.request('getManagedBotToken', payload)

    
    async def replace_managed_bot_token(self, user_id: int) -> str:
        """Use this method to revoke the current token of a managed bot and generate a new one. Returns the new token as String on success."""
        payload = {
            'user_id': user_id,
        }
        return await self.request('replaceManagedBotToken', payload)

    
    async def get_managed_bot_access_settings(self, user_id: int) -> BotAccessSettings:
        """Use this method to get the access settings of a managed bot. Returns a BotAccessSettings object on success."""
        payload = {
            'user_id': user_id,
        }
        return await self.request('getManagedBotAccessSettings', payload)

    
    async def set_managed_bot_access_settings(self, user_id: int, is_access_restricted: bool, added_user_ids: list[int] | None = None) -> bool:
        """Use this method to change the access settings of a managed bot. Returns True on success."""
        payload = {
            'user_id': user_id,
            'is_access_restricted': is_access_restricted,
            'added_user_ids': added_user_ids,
        }
        return await self.request('setManagedBotAccessSettings', payload)

    
    async def set_my_commands(self, commands: list[BotCommand], scope: BotCommandScope | None = None, language_code: str | None = None) -> bool:
        """Use this method to change the list of the bot's commands. See this manual for more details about bot commands. Returns True on success."""
        payload = {
            'commands': commands,
            'scope': scope,
            'language_code': language_code,
        }
        return await self.request('setMyCommands', payload)

    
    async def delete_my_commands(self, scope: BotCommandScope | None = None, language_code: str | None = None) -> bool:
        """Use this method to delete the list of the bot's commands for the given scope and user language. After deletion, higher level commands will be shown to affected users. Returns True on success."""
        payload = {
            'scope': scope,
            'language_code': language_code,
        }
        return await self.request('deleteMyCommands', payload)

    
    async def get_my_commands(self, scope: BotCommandScope | None = None, language_code: str | None = None) -> list[BotCommand]:
        """Use this method to get the current list of the bot's commands for the given scope and user language. Returns an Array of BotCommand objects. If commands aren't set, an empty list is returned."""
        payload = {
            'scope': scope,
            'language_code': language_code,
        }
        return await self.request('getMyCommands', payload)

    
    async def set_my_name(self, name: str | None = None, language_code: str | None = None) -> bool:
        """Use this method to change the bot's name. Returns True on success."""
        payload = {
            'name': name,
            'language_code': language_code,
        }
        return await self.request('setMyName', payload)

    
    async def get_my_name(self, language_code: str | None = None) -> BotName:
        """Use this method to get the current bot name for the given user language. Returns BotName on success."""
        payload = {
            'language_code': language_code,
        }
        return await self.request('getMyName', payload)

    
    async def set_my_description(self, description: str | None = None, language_code: str | None = None) -> bool:
        """Use this method to change the bot's description, which is shown in the chat with the bot if the chat is empty. Returns True on success."""
        payload = {
            'description': description,
            'language_code': language_code,
        }
        return await self.request('setMyDescription', payload)

    
    async def get_my_description(self, language_code: str | None = None) -> BotDescription:
        """Use this method to get the current bot description for the given user language. Returns BotDescription on success."""
        payload = {
            'language_code': language_code,
        }
        return await self.request('getMyDescription', payload)

    
    async def set_my_short_description(self, short_description: str | None = None, language_code: str | None = None) -> bool:
        """Use this method to change the bot's short description, which is shown on the bot's profile page and is sent together with the link when users share the bot. Returns True on success."""
        payload = {
            'short_description': short_description,
            'language_code': language_code,
        }
        return await self.request('setMyShortDescription', payload)

    
    async def get_my_short_description(self, language_code: str | None = None) -> BotShortDescription:
        """Use this method to get the current bot short description for the given user language. Returns BotShortDescription on success."""
        payload = {
            'language_code': language_code,
        }
        return await self.request('getMyShortDescription', payload)

    
    async def set_my_profile_photo(self, photo_: InputProfilePhoto) -> bool:
        """Changes the profile photo of the bot. Returns True on success."""
        payload = {
        }
        files = {
            'photo': photo_,
        }
        files = {k: v for k, v in files.items() if v is not None}
        return await self.request('setMyProfilePhoto', payload, files=files if files else None)

    
    async def remove_my_profile_photo(self) -> bool:
        """Removes the profile photo of the bot. Requires no parameters. Returns True on success."""
        payload = {
        }
        return await self.request('removeMyProfilePhoto', payload)

    
    async def set_chat_menu_button(self, chat_id: int | None = None, menu_button: MenuButton | None = None) -> bool:
        """Use this method to change the bot's menu button in a private chat, or the default menu button. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'menu_button': menu_button,
        }
        return await self.request('setChatMenuButton', payload)

    
    async def get_chat_menu_button(self, chat_id: int | None = None) -> MenuButton:
        """Use this method to get the current value of the bot's menu button in a private chat, or the default menu button. Returns MenuButton on success."""
        payload = {
            'chat_id': chat_id,
        }
        return await self.request('getChatMenuButton', payload)

    
    async def set_my_default_administrator_rights(self, rights: ChatAdministratorRights | None = None, for_channels: bool | None = None) -> bool:
        """Use this method to change the default administrator rights requested by the bot when it's added as an administrator to groups or channels. These rights will be suggested to users, but they are free to modify the list before adding the bot. Returns True on success."""
        payload = {
            'rights': rights,
            'for_channels': for_channels,
        }
        return await self.request('setMyDefaultAdministratorRights', payload)

    
    async def get_my_default_administrator_rights(self, for_channels: bool | None = None) -> ChatAdministratorRights:
        """Use this method to get the current default administrator rights of the bot. Returns ChatAdministratorRights on success."""
        payload = {
            'for_channels': for_channels,
        }
        return await self.request('getMyDefaultAdministratorRights', payload)

    
    async def get_available_gifts(self) -> Gifts:
        """Returns the list of gifts that can be sent by the bot to users and channel chats. Requires no parameters. Returns a Gifts object."""
        payload = {
        }
        return await self.request('getAvailableGifts', payload)

    
    async def send_gift(self, gift_id: str, user_id: int | None = None, chat_id: int | str | None = None, pay_for_upgrade: bool | None = None, text: str | None = None, text_parse_mode: str | None = None, text_entities: list[MessageEntity] | None = None) -> bool:
        """Sends a gift to the given user or channel chat. The gift can't be converted to Telegram Stars by the receiver. Returns True on success."""
        payload = {
            'user_id': user_id,
            'chat_id': chat_id,
            'gift_id': gift_id,
            'pay_for_upgrade': pay_for_upgrade,
            'text': text,
            'text_parse_mode': text_parse_mode,
            'text_entities': text_entities,
        }
        return await self.request('sendGift', payload)

    
    async def gift_premium_subscription(self, user_id: int, month_count: int, star_count: int, text: str | None = None, text_parse_mode: str | None = None, text_entities: list[MessageEntity] | None = None) -> bool:
        """Gifts a Telegram Premium subscription to the given user. Returns True on success."""
        payload = {
            'user_id': user_id,
            'month_count': month_count,
            'star_count': star_count,
            'text': text,
            'text_parse_mode': text_parse_mode,
            'text_entities': text_entities,
        }
        return await self.request('giftPremiumSubscription', payload)

    
    async def verify_user(self, user_id: int, custom_description: str | None = None) -> bool:
        """Verifies a user on behalf of the organization which is represented by the bot. Returns True on success."""
        payload = {
            'user_id': user_id,
            'custom_description': custom_description,
        }
        return await self.request('verifyUser', payload)

    
    async def verify_chat(self, chat_id: int | str, custom_description: str | None = None) -> bool:
        """Verifies a chat on behalf of the organization which is represented by the bot. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'custom_description': custom_description,
        }
        return await self.request('verifyChat', payload)

    
    async def remove_user_verification(self, user_id: int) -> bool:
        """Removes verification from a user who is currently verified on behalf of the organization represented by the bot. Returns True on success."""
        payload = {
            'user_id': user_id,
        }
        return await self.request('removeUserVerification', payload)

    
    async def remove_chat_verification(self, chat_id: int | str) -> bool:
        """Removes verification from a chat that is currently verified on behalf of the organization represented by the bot. Returns True on success."""
        payload = {
            'chat_id': chat_id,
        }
        return await self.request('removeChatVerification', payload)

    
    async def read_business_message(self, business_connection_id: str, chat_id: int, message_id: int) -> bool:
        """Marks incoming message as read on behalf of a business account. Requires the can_read_messages business bot right. Returns True on success."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_id': message_id,
        }
        return await self.request('readBusinessMessage', payload)

    
    async def delete_business_messages(self, business_connection_id: str, message_ids: list[int]) -> bool:
        """Delete messages on behalf of a business account. Requires the can_delete_sent_messages business bot right to delete messages sent by the bot itself, or the can_delete_all_messages business bot right to delete any message. Returns True on success."""
        payload = {
            'business_connection_id': business_connection_id,
            'message_ids': message_ids,
        }
        return await self.request('deleteBusinessMessages', payload)

    
    async def set_business_account_name(self, business_connection_id: str, first_name: str, last_name: str | None = None) -> bool:
        """Changes the first and last name of a managed business account. Requires the can_change_name business bot right. Returns True on success."""
        payload = {
            'business_connection_id': business_connection_id,
            'first_name': first_name,
            'last_name': last_name,
        }
        return await self.request('setBusinessAccountName', payload)

    
    async def set_business_account_username(self, business_connection_id: str, username: str | None = None) -> bool:
        """Changes the username of a managed business account. Requires the can_change_username business bot right. Returns True on success."""
        payload = {
            'business_connection_id': business_connection_id,
            'username': username,
        }
        return await self.request('setBusinessAccountUsername', payload)

    
    async def set_business_account_bio(self, business_connection_id: str, bio: str | None = None) -> bool:
        """Changes the bio of a managed business account. Requires the can_change_bio business bot right. Returns True on success."""
        payload = {
            'business_connection_id': business_connection_id,
            'bio': bio,
        }
        return await self.request('setBusinessAccountBio', payload)

    
    async def set_business_account_profile_photo(self, business_connection_id: str, photo_: InputProfilePhoto, is_public: bool | None = None) -> bool:
        """Changes the profile photo of a managed business account. Requires the can_edit_profile_photo business bot right. Returns True on success."""
        payload = {
            'business_connection_id': business_connection_id,
            'is_public': is_public,
        }
        files = {
            'photo': photo_,
        }
        files = {k: v for k, v in files.items() if v is not None}
        return await self.request('setBusinessAccountProfilePhoto', payload, files=files if files else None)

    
    async def remove_business_account_profile_photo(self, business_connection_id: str, is_public: bool | None = None) -> bool:
        """Removes the current profile photo of a managed business account. Requires the can_edit_profile_photo business bot right. Returns True on success."""
        payload = {
            'business_connection_id': business_connection_id,
            'is_public': is_public,
        }
        return await self.request('removeBusinessAccountProfilePhoto', payload)

    
    async def set_business_account_gift_settings(self, business_connection_id: str, show_gift_button: bool, accepted_gift_types: AcceptedGiftTypes) -> bool:
        """Changes the privacy settings pertaining to incoming gifts in a managed business account. Requires the can_change_gift_settings business bot right. Returns True on success."""
        payload = {
            'business_connection_id': business_connection_id,
            'show_gift_button': show_gift_button,
            'accepted_gift_types': accepted_gift_types,
        }
        return await self.request('setBusinessAccountGiftSettings', payload)

    
    async def get_business_account_star_balance(self, business_connection_id: str) -> StarAmount:
        """Returns the amount of Telegram Stars owned by a managed business account. Requires the can_view_gifts_and_stars business bot right. Returns StarAmount on success."""
        payload = {
            'business_connection_id': business_connection_id,
        }
        return await self.request('getBusinessAccountStarBalance', payload)

    
    async def transfer_business_account_stars(self, business_connection_id: str, star_count: int) -> bool:
        """Transfers Telegram Stars from the business account balance to the bot's balance. Requires the can_transfer_stars business bot right. Returns True on success."""
        payload = {
            'business_connection_id': business_connection_id,
            'star_count': star_count,
        }
        return await self.request('transferBusinessAccountStars', payload)

    
    async def get_business_account_gifts(self, business_connection_id: str, exclude_unsaved: bool | None = None, exclude_saved: bool | None = None, exclude_unlimited: bool | None = None, exclude_limited_upgradable: bool | None = None, exclude_limited_non_upgradable: bool | None = None, exclude_unique: bool | None = None, exclude_from_blockchain: bool | None = None, sort_by_price: bool | None = None, offset: str | None = None, limit: int | None = None) -> OwnedGifts:
        """Returns the gifts received and owned by a managed business account. Requires the can_view_gifts_and_stars business bot right. Returns OwnedGifts on success."""
        payload = {
            'business_connection_id': business_connection_id,
            'exclude_unsaved': exclude_unsaved,
            'exclude_saved': exclude_saved,
            'exclude_unlimited': exclude_unlimited,
            'exclude_limited_upgradable': exclude_limited_upgradable,
            'exclude_limited_non_upgradable': exclude_limited_non_upgradable,
            'exclude_unique': exclude_unique,
            'exclude_from_blockchain': exclude_from_blockchain,
            'sort_by_price': sort_by_price,
            'offset': offset,
            'limit': limit,
        }
        return await self.request('getBusinessAccountGifts', payload)

    
    async def get_user_gifts(self, user_id: int, exclude_unlimited: bool | None = None, exclude_limited_upgradable: bool | None = None, exclude_limited_non_upgradable: bool | None = None, exclude_from_blockchain: bool | None = None, exclude_unique: bool | None = None, sort_by_price: bool | None = None, offset: str | None = None, limit: int | None = None) -> OwnedGifts:
        """Returns the gifts owned and hosted by a user. Returns OwnedGifts on success."""
        payload = {
            'user_id': user_id,
            'exclude_unlimited': exclude_unlimited,
            'exclude_limited_upgradable': exclude_limited_upgradable,
            'exclude_limited_non_upgradable': exclude_limited_non_upgradable,
            'exclude_from_blockchain': exclude_from_blockchain,
            'exclude_unique': exclude_unique,
            'sort_by_price': sort_by_price,
            'offset': offset,
            'limit': limit,
        }
        return await self.request('getUserGifts', payload)

    
    async def get_chat_gifts(self, chat_id: int | str, exclude_unsaved: bool | None = None, exclude_saved: bool | None = None, exclude_unlimited: bool | None = None, exclude_limited_upgradable: bool | None = None, exclude_limited_non_upgradable: bool | None = None, exclude_from_blockchain: bool | None = None, exclude_unique: bool | None = None, sort_by_price: bool | None = None, offset: str | None = None, limit: int | None = None) -> OwnedGifts:
        """Returns the gifts owned by a chat. Returns OwnedGifts on success."""
        payload = {
            'chat_id': chat_id,
            'exclude_unsaved': exclude_unsaved,
            'exclude_saved': exclude_saved,
            'exclude_unlimited': exclude_unlimited,
            'exclude_limited_upgradable': exclude_limited_upgradable,
            'exclude_limited_non_upgradable': exclude_limited_non_upgradable,
            'exclude_from_blockchain': exclude_from_blockchain,
            'exclude_unique': exclude_unique,
            'sort_by_price': sort_by_price,
            'offset': offset,
            'limit': limit,
        }
        return await self.request('getChatGifts', payload)

    
    async def convert_gift_to_stars(self, business_connection_id: str, owned_gift_id: str) -> bool:
        """Converts a given regular gift to Telegram Stars. Requires the can_convert_gifts_to_stars business bot right. Returns True on success."""
        payload = {
            'business_connection_id': business_connection_id,
            'owned_gift_id': owned_gift_id,
        }
        return await self.request('convertGiftToStars', payload)

    
    async def upgrade_gift(self, business_connection_id: str, owned_gift_id: str, keep_original_details: bool | None = None, star_count: int | None = None) -> bool:
        """Upgrades a given regular gift to a unique gift. Requires the can_transfer_and_upgrade_gifts business bot right. Additionally requires the can_transfer_stars business bot right if the upgrade is paid. Returns True on success."""
        payload = {
            'business_connection_id': business_connection_id,
            'owned_gift_id': owned_gift_id,
            'keep_original_details': keep_original_details,
            'star_count': star_count,
        }
        return await self.request('upgradeGift', payload)

    
    async def transfer_gift(self, business_connection_id: str, owned_gift_id: str, new_owner_chat_id: int, star_count: int | None = None) -> bool:
        """Transfers an owned unique gift to another user. Requires the can_transfer_and_upgrade_gifts business bot right. Requires can_transfer_stars business bot right if the transfer is paid. Returns True on success."""
        payload = {
            'business_connection_id': business_connection_id,
            'owned_gift_id': owned_gift_id,
            'new_owner_chat_id': new_owner_chat_id,
            'star_count': star_count,
        }
        return await self.request('transferGift', payload)

    
    async def post_story(self, business_connection_id: str, content: InputStoryContent, active_period: int, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, areas: list[StoryArea] | None = None, post_to_chat_page: bool | None = None, protect_content: bool | None = None) -> Story:
        """Posts a story on behalf of a managed business account. Requires the can_manage_stories business bot right. Returns Story on success."""
        payload = {
            'business_connection_id': business_connection_id,
            'content': content,
            'active_period': active_period,
            'caption': caption,
            'parse_mode': parse_mode,
            'caption_entities': caption_entities,
            'areas': areas,
            'post_to_chat_page': post_to_chat_page,
            'protect_content': protect_content,
        }
        return await self.request('postStory', payload)

    
    async def repost_story(self, business_connection_id: str, from_chat_id: int, from_story_id: int, active_period: int, post_to_chat_page: bool | None = None, protect_content: bool | None = None) -> Story:
        """Reposts a story on behalf of a business account from another business account. Both business accounts must be managed by the same bot, and the story on the source account must have been posted (or reposted) by the bot. Requires the can_manage_stories business bot right for both business accounts. Returns Story on success."""
        payload = {
            'business_connection_id': business_connection_id,
            'from_chat_id': from_chat_id,
            'from_story_id': from_story_id,
            'active_period': active_period,
            'post_to_chat_page': post_to_chat_page,
            'protect_content': protect_content,
        }
        return await self.request('repostStory', payload)

    
    async def edit_story(self, business_connection_id: str, story_id: int, content: InputStoryContent, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, areas: list[StoryArea] | None = None) -> Story:
        """Edits a story previously posted by the bot on behalf of a managed business account. Requires the can_manage_stories business bot right. Returns Story on success."""
        payload = {
            'business_connection_id': business_connection_id,
            'story_id': story_id,
            'content': content,
            'caption': caption,
            'parse_mode': parse_mode,
            'caption_entities': caption_entities,
            'areas': areas,
        }
        return await self.request('editStory', payload)

    
    async def delete_story(self, business_connection_id: str, story_id: int) -> bool:
        """Deletes a story previously posted by the bot on behalf of a managed business account. Requires the can_manage_stories business bot right. Returns True on success."""
        payload = {
            'business_connection_id': business_connection_id,
            'story_id': story_id,
        }
        return await self.request('deleteStory', payload)

    
    async def answer_web_app_query(self, web_app_query_id: str, result: InlineQueryResult) -> SentWebAppMessage:
        """Use this method to set the result of an interaction with a Web App and send a corresponding message on behalf of the user to the chat from which the query originated. On success, a SentWebAppMessage object is returned."""
        payload = {
            'web_app_query_id': web_app_query_id,
            'result': result,
        }
        return await self.request('answerWebAppQuery', payload)

    
    async def save_prepared_inline_message(self, user_id: int, result: InlineQueryResult, allow_user_chats: bool | None = None, allow_bot_chats: bool | None = None, allow_group_chats: bool | None = None, allow_channel_chats: bool | None = None) -> PreparedInlineMessage:
        """Stores a message that can be sent by a user of a Mini App. Returns a PreparedInlineMessage object."""
        payload = {
            'user_id': user_id,
            'result': result,
            'allow_user_chats': allow_user_chats,
            'allow_bot_chats': allow_bot_chats,
            'allow_group_chats': allow_group_chats,
            'allow_channel_chats': allow_channel_chats,
        }
        return await self.request('savePreparedInlineMessage', payload)

    
    async def save_prepared_keyboard_button(self, user_id: int, button: KeyboardButton) -> PreparedKeyboardButton:
        """Stores a keyboard button that can be used by a user within a Mini App. Returns a PreparedKeyboardButton object."""
        payload = {
            'user_id': user_id,
            'button': button,
        }
        return await self.request('savePreparedKeyboardButton', payload)

    
    async def edit_message_text(self, business_connection_id: str | None = None, chat_id: int | str | None = None, message_id: int | None = None, inline_message_id: str | None = None, text: str | None = None, parse_mode: str | None = None, entities: list[MessageEntity] | None = None, link_preview_options: LinkPreviewOptions | None = None, rich_message: InputRichMessage | None = None, reply_markup: InlineKeyboardMarkup | None = None) -> Message | bool:
        """Use this method to edit text, rich and game messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within 48 hours from the time they were sent."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_id': message_id,
            'inline_message_id': inline_message_id,
            'text': text,
            'parse_mode': parse_mode,
            'entities': entities,
            'link_preview_options': link_preview_options,
            'rich_message': rich_message,
            'reply_markup': reply_markup,
        }
        return await self.request('editMessageText', payload)

    
    async def edit_message_caption(self, business_connection_id: str | None = None, chat_id: int | str | None = None, message_id: int | None = None, inline_message_id: str | None = None, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, show_caption_above_media: bool | None = None, reply_markup: InlineKeyboardMarkup | None = None) -> Message | bool:
        """Use this method to edit captions of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within 48 hours from the time they were sent."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_id': message_id,
            'inline_message_id': inline_message_id,
            'caption': caption,
            'parse_mode': parse_mode,
            'caption_entities': caption_entities,
            'show_caption_above_media': show_caption_above_media,
            'reply_markup': reply_markup,
        }
        return await self.request('editMessageCaption', payload)

    
    async def edit_message_media(self, media: InputMedia, business_connection_id: str | None = None, chat_id: int | str | None = None, message_id: int | None = None, inline_message_id: str | None = None, reply_markup: InlineKeyboardMarkup | None = None) -> Message | bool:
        """Use this method to edit animation, audio, document, live photo, photo, or video messages, or to replace a text or a rich message with a media. If a message is part of a message album, then it can be edited only to an audio for audio albums, only to a document for document albums and to a photo, a live photo, or a video otherwise. When an inline message is edited, a new file can't be uploaded; use a previously uploaded file via its file_id or specify a URL. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within 48 hours from the time they were sent."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_id': message_id,
            'inline_message_id': inline_message_id,
            'media': media,
            'reply_markup': reply_markup,
        }
        return await self.request('editMessageMedia', payload)

    
    async def edit_message_live_location(self, latitude: float, longitude: float, business_connection_id: str | None = None, chat_id: int | str | None = None, message_id: int | None = None, inline_message_id: str | None = None, live_period: int | None = None, horizontal_accuracy: float | None = None, heading: int | None = None, proximity_alert_radius: int | None = None, reply_markup: InlineKeyboardMarkup | None = None) -> Message | bool:
        """Use this method to edit live location messages. A location can be edited until its live_period expires or editing is explicitly disabled by a call to stopMessageLiveLocation. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_id': message_id,
            'inline_message_id': inline_message_id,
            'latitude': latitude,
            'longitude': longitude,
            'live_period': live_period,
            'horizontal_accuracy': horizontal_accuracy,
            'heading': heading,
            'proximity_alert_radius': proximity_alert_radius,
            'reply_markup': reply_markup,
        }
        return await self.request('editMessageLiveLocation', payload)

    
    async def stop_message_live_location(self, business_connection_id: str | None = None, chat_id: int | str | None = None, message_id: int | None = None, inline_message_id: str | None = None, reply_markup: InlineKeyboardMarkup | None = None) -> Message | bool:
        """Use this method to stop updating a live location message before live_period expires. On success, if the message is not an inline message, the edited Message is returned, otherwise True is returned."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_id': message_id,
            'inline_message_id': inline_message_id,
            'reply_markup': reply_markup,
        }
        return await self.request('stopMessageLiveLocation', payload)

    
    async def edit_message_checklist(self, business_connection_id: str, chat_id: int | str, message_id: int, checklist: InputChecklist, reply_markup: InlineKeyboardMarkup | None = None) -> Message:
        """Use this method to edit a checklist on behalf of a connected business account. On success, the edited Message is returned."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_id': message_id,
            'checklist': checklist,
            'reply_markup': reply_markup,
        }
        return await self.request('editMessageChecklist', payload)

    
    async def edit_message_reply_markup(self, business_connection_id: str | None = None, chat_id: int | str | None = None, message_id: int | None = None, inline_message_id: str | None = None, reply_markup: InlineKeyboardMarkup | None = None) -> Message | bool:
        """Use this method to edit only the reply markup of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within 48 hours from the time they were sent."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_id': message_id,
            'inline_message_id': inline_message_id,
            'reply_markup': reply_markup,
        }
        return await self.request('editMessageReplyMarkup', payload)

    
    async def stop_poll(self, chat_id: int | str, message_id: int, business_connection_id: str | None = None, reply_markup: InlineKeyboardMarkup | None = None) -> Poll:
        """Use this method to stop a poll which was sent by the bot. On success, the stopped Poll is returned."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_id': message_id,
            'reply_markup': reply_markup,
        }
        return await self.request('stopPoll', payload)

    
    async def edit_ephemeral_message_text(self, chat_id: int | str, receiver_user_id: int, ephemeral_message_id: int, text: str | None = None, parse_mode: str | None = None, entities: list[MessageEntity] | None = None, rich_message: InputRichMessage | None = None, link_preview_options: LinkPreviewOptions | None = None, reply_markup: InlineKeyboardMarkup | None = None) -> bool:
        """Use this method to edit an ephemeral text or rich message. Note that it is not guaranteed that the user will receive the message edit event, especially if they are offline. On success, True is returned."""
        payload = {
            'chat_id': chat_id,
            'receiver_user_id': receiver_user_id,
            'ephemeral_message_id': ephemeral_message_id,
            'text': text,
            'parse_mode': parse_mode,
            'entities': entities,
            'rich_message': rich_message,
            'link_preview_options': link_preview_options,
            'reply_markup': reply_markup,
        }
        return await self.request('editEphemeralMessageText', payload)

    
    async def edit_ephemeral_message_media(self, chat_id: int | str, receiver_user_id: int, ephemeral_message_id: int, media: InputMedia, reply_markup: InlineKeyboardMarkup | None = None) -> bool:
        """Use this method to edit the media of an ephemeral message. Note that it is not guaranteed that the user will receive the message edit event, especially if they are offline. On success, True is returned."""
        payload = {
            'chat_id': chat_id,
            'receiver_user_id': receiver_user_id,
            'ephemeral_message_id': ephemeral_message_id,
            'media': media,
            'reply_markup': reply_markup,
        }
        return await self.request('editEphemeralMessageMedia', payload)

    
    async def edit_ephemeral_message_caption(self, chat_id: int | str, receiver_user_id: int, ephemeral_message_id: int, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, show_caption_above_media: bool | None = None, reply_markup: InlineKeyboardMarkup | None = None) -> bool:
        """Use this method to edit the caption of an ephemeral message. Note that it is not guaranteed that the user will receive the message edit event, especially if they are offline. On success, True is returned."""
        payload = {
            'chat_id': chat_id,
            'receiver_user_id': receiver_user_id,
            'ephemeral_message_id': ephemeral_message_id,
            'caption': caption,
            'parse_mode': parse_mode,
            'caption_entities': caption_entities,
            'show_caption_above_media': show_caption_above_media,
            'reply_markup': reply_markup,
        }
        return await self.request('editEphemeralMessageCaption', payload)

    
    async def edit_ephemeral_message_reply_markup(self, chat_id: int | str, receiver_user_id: int, ephemeral_message_id: int, reply_markup: InlineKeyboardMarkup | None = None) -> bool:
        """Use this method to edit only the reply markup of an ephemeral message. Note that it is not guaranteed that the user will receive the message edit event, especially if they are offline. On success, True is returned."""
        payload = {
            'chat_id': chat_id,
            'receiver_user_id': receiver_user_id,
            'ephemeral_message_id': ephemeral_message_id,
            'reply_markup': reply_markup,
        }
        return await self.request('editEphemeralMessageReplyMarkup', payload)

    
    async def approve_suggested_post(self, chat_id: int, message_id: int, send_date: int | None = None) -> bool:
        """Use this method to approve a suggested post in a direct messages chat. The bot must have the 'can_post_messages' administrator right in the corresponding channel chat. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'message_id': message_id,
            'send_date': send_date,
        }
        return await self.request('approveSuggestedPost', payload)

    
    async def decline_suggested_post(self, chat_id: int, message_id: int, comment: str | None = None) -> bool:
        """Use this method to decline a suggested post in a direct messages chat. The bot must have the 'can_manage_direct_messages' administrator right in the corresponding channel chat. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'message_id': message_id,
            'comment': comment,
        }
        return await self.request('declineSuggestedPost', payload)

    
    async def delete_message(self, chat_id: int | str, message_id: int) -> bool:
        """Use this method to delete a message, including service messages, with the following limitations: - A message can only be deleted if it was sent less than 48 hours ago. - Service messages about a supergroup, channel, or forum topic creation can't be deleted. - A dice message in a private chat can only be deleted if it was sent more than 24 hours ago. - Bots can delete outgoing messages in private chats, groups, and supergroups. - Bots can delete incoming messages in private chats. - Bots granted can_post_messages permissions can delete outgoing messages in channels. - If the bot is an administrator of a group, it can delete any message there. - If the bot has can_delete_messages administrator right in a supergroup or a channel, it can delete any message there. - If the bot has can_manage_direct_messages administrator right in a channel, it can delete any message in the corresponding direct messages chat. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'message_id': message_id,
        }
        return await self.request('deleteMessage', payload)

    
    async def delete_messages(self, chat_id: int | str, message_ids: list[int]) -> bool:
        """Use this method to delete multiple messages simultaneously. If some of the specified messages can't be found, they are skipped. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'message_ids': message_ids,
        }
        return await self.request('deleteMessages', payload)

    
    async def delete_ephemeral_message(self, chat_id: int | str, receiver_user_id: int, ephemeral_message_id: int) -> bool:
        """Use this method to delete an ephemeral message. Note that it is not guaranteed that the user will receive the message deletion event, especially if they are offline. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'receiver_user_id': receiver_user_id,
            'ephemeral_message_id': ephemeral_message_id,
        }
        return await self.request('deleteEphemeralMessage', payload)

    
    async def delete_message_reaction(self, chat_id: int | str, message_id: int, user_id: int | None = None, actor_chat_id: int | None = None) -> bool:
        """Use this method to remove a reaction from a message in a group or a supergroup chat. The bot must have the 'can_delete_messages' administrator right in the chat. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'message_id': message_id,
            'user_id': user_id,
            'actor_chat_id': actor_chat_id,
        }
        return await self.request('deleteMessageReaction', payload)

    
    async def delete_all_message_reactions(self, chat_id: int | str, user_id: int | None = None, actor_chat_id: int | None = None) -> bool:
        """Use this method to remove up to 10000 recent reactions in a group or a supergroup chat added by a given user or chat. The bot must have the 'can_delete_messages' administrator right in the chat. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'user_id': user_id,
            'actor_chat_id': actor_chat_id,
        }
        return await self.request('deleteAllMessageReactions', payload)

    
    async def send_sticker(self, chat_id: int | str, sticker_: InputFile | str, business_connection_id: str | None = None, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, ephemeral_message_parameters: EphemeralMessageParameters | None = None, emoji: str | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: ReplyKeyboardMarkup | ForceReply | ReplyKeyboardRemove | InlineKeyboardMarkup | None = None) -> Message:
        """Use this method to send static .WEBP, animated .TGS, or video .WEBM stickers. On success, the sent Message is returned."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'direct_messages_topic_id': direct_messages_topic_id,
            'ephemeral_message_parameters': ephemeral_message_parameters,
            'emoji': emoji,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'suggested_post_parameters': suggested_post_parameters,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup,
        }
        files = {
            'sticker': sticker_,
        }
        files = {k: v for k, v in files.items() if v is not None}
        return await self.request('sendSticker', payload, files=files if files else None)

    
    async def get_sticker_set(self, name: str) -> StickerSet:
        """Use this method to get a sticker set. On success, a StickerSet object is returned."""
        payload = {
            'name': name,
        }
        return await self.request('getStickerSet', payload)

    
    async def get_custom_emoji_stickers(self, custom_emoji_ids: list[str]) -> list[Sticker]:
        """Use this method to get information about custom emoji stickers by their identifiers. Returns an Array of Sticker objects."""
        payload = {
            'custom_emoji_ids': custom_emoji_ids,
        }
        return await self.request('getCustomEmojiStickers', payload)

    
    async def upload_sticker_file(self, user_id: int, sticker_: InputFile, sticker_format: str) -> File:
        """Use this method to upload a file with a sticker for later use in the createNewStickerSet, addStickerToSet, or replaceStickerInSet methods (the file can be used multiple times). Returns the uploaded File on success."""
        payload = {
            'user_id': user_id,
            'sticker_format': sticker_format,
        }
        files = {
            'sticker': sticker_,
        }
        files = {k: v for k, v in files.items() if v is not None}
        return await self.request('uploadStickerFile', payload, files=files if files else None)

    
    async def create_new_sticker_set(self, user_id: int, name: str, title: str, stickers: list[InputSticker], sticker_type: str | None = None, needs_repainting: bool | None = None) -> bool:
        """Use this method to create a new sticker set owned by a user. The bot will be able to edit the sticker set thus created. Returns True on success."""
        payload = {
            'user_id': user_id,
            'name': name,
            'title': title,
            'stickers': stickers,
            'sticker_type': sticker_type,
            'needs_repainting': needs_repainting,
        }
        return await self.request('createNewStickerSet', payload)

    
    async def add_sticker_to_set(self, user_id: int, name: str, sticker_: InputSticker) -> bool:
        """Use this method to add a new sticker to a set created by the bot. Emoji sticker sets can have up to 200 stickers. Other sticker sets can have up to 120 stickers. Returns True on success."""
        payload = {
            'user_id': user_id,
            'name': name,
        }
        files = {
            'sticker': sticker_,
        }
        files = {k: v for k, v in files.items() if v is not None}
        return await self.request('addStickerToSet', payload, files=files if files else None)

    
    async def set_sticker_position_in_set(self, sticker_: str, position: int) -> bool:
        """Use this method to move a sticker in a set created by the bot to a specific position. Returns True on success."""
        payload = {
            'position': position,
        }
        files = {
            'sticker': sticker_,
        }
        files = {k: v for k, v in files.items() if v is not None}
        return await self.request('setStickerPositionInSet', payload, files=files if files else None)

    
    async def delete_sticker_from_set(self, sticker_: str) -> bool:
        """Use this method to delete a sticker from a set created by the bot. Returns True on success."""
        payload = {
        }
        files = {
            'sticker': sticker_,
        }
        files = {k: v for k, v in files.items() if v is not None}
        return await self.request('deleteStickerFromSet', payload, files=files if files else None)

    
    async def replace_sticker_in_set(self, user_id: int, name: str, old_sticker: str, sticker_: InputSticker) -> bool:
        """Use this method to replace an existing sticker in a sticker set with a new one. The method is equivalent to calling deleteStickerFromSet, then addStickerToSet, then setStickerPositionInSet. Returns True on success."""
        payload = {
            'user_id': user_id,
            'name': name,
            'old_sticker': old_sticker,
        }
        files = {
            'sticker': sticker_,
        }
        files = {k: v for k, v in files.items() if v is not None}
        return await self.request('replaceStickerInSet', payload, files=files if files else None)

    
    async def set_sticker_emoji_list(self, sticker_: str, emoji_list: list[str]) -> bool:
        """Use this method to change the list of emoji assigned to a regular or custom emoji sticker. The sticker must belong to a sticker set created by the bot. Returns True on success."""
        payload = {
            'emoji_list': emoji_list,
        }
        files = {
            'sticker': sticker_,
        }
        files = {k: v for k, v in files.items() if v is not None}
        return await self.request('setStickerEmojiList', payload, files=files if files else None)

    
    async def set_sticker_keywords(self, sticker_: str, keywords: list[str] | None = None) -> bool:
        """Use this method to change search keywords assigned to a regular or custom emoji sticker. The sticker must belong to a sticker set created by the bot. Returns True on success."""
        payload = {
            'keywords': keywords,
        }
        files = {
            'sticker': sticker_,
        }
        files = {k: v for k, v in files.items() if v is not None}
        return await self.request('setStickerKeywords', payload, files=files if files else None)

    
    async def set_sticker_mask_position(self, sticker_: str, mask_position: MaskPosition | None = None) -> bool:
        """Use this method to change the mask position of a mask sticker. The sticker must belong to a sticker set that was created by the bot. Returns True on success."""
        payload = {
            'mask_position': mask_position,
        }
        files = {
            'sticker': sticker_,
        }
        files = {k: v for k, v in files.items() if v is not None}
        return await self.request('setStickerMaskPosition', payload, files=files if files else None)

    
    async def set_sticker_set_title(self, name: str, title: str) -> bool:
        """Use this method to set the title of a created sticker set. Returns True on success."""
        payload = {
            'name': name,
            'title': title,
        }
        return await self.request('setStickerSetTitle', payload)

    
    async def set_sticker_set_thumbnail(self, name: str, user_id: int, format: str, thumbnail: InputFile | str | None = None) -> bool:
        """Use this method to set the thumbnail of a regular or mask sticker set. The format of the thumbnail file must match the format of the stickers in the set. Returns True on success."""
        payload = {
            'name': name,
            'user_id': user_id,
            'thumbnail': thumbnail,
            'format': format,
        }
        return await self.request('setStickerSetThumbnail', payload)

    
    async def set_custom_emoji_sticker_set_thumbnail(self, name: str, custom_emoji_id: str | None = None) -> bool:
        """Use this method to set the thumbnail of a custom emoji sticker set. Returns True on success."""
        payload = {
            'name': name,
            'custom_emoji_id': custom_emoji_id,
        }
        return await self.request('setCustomEmojiStickerSetThumbnail', payload)

    
    async def delete_sticker_set(self, name: str) -> bool:
        """Use this method to delete a sticker set that was created by the bot. Returns True on success."""
        payload = {
            'name': name,
        }
        return await self.request('deleteStickerSet', payload)

    
    async def send_rich_message(self, chat_id: int | str, rich_message: InputRichMessage, business_connection_id: str | None = None, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, ephemeral_message_parameters: EphemeralMessageParameters | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: ReplyKeyboardMarkup | ForceReply | ReplyKeyboardRemove | InlineKeyboardMarkup | None = None) -> Message:
        """Use this method to send rich messages. If the message contains a block with a media element, then the bot must have the right to send the media to the chat. On success, the sent Message is returned."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'direct_messages_topic_id': direct_messages_topic_id,
            'ephemeral_message_parameters': ephemeral_message_parameters,
            'rich_message': rich_message,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'suggested_post_parameters': suggested_post_parameters,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup,
        }
        return await self.request('sendRichMessage', payload)

    
    async def send_rich_message_draft(self, chat_id: int, draft_id: int, rich_message: InputRichMessage, message_thread_id: int | None = None, can_stop: bool | None = None, keep_on_stop: bool | None = None) -> bool:
        """Use this method to stream a partial rich message to a user while the message is being generated. Note that the streamed draft is ephemeral and acts as a temporary 30-second preview - once the output is finalized, you must call sendRichMessage with the complete message to persist it in the user's chat. Returns True on success."""
        payload = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'draft_id': draft_id,
            'rich_message': rich_message,
            'can_stop': can_stop,
            'keep_on_stop': keep_on_stop,
        }
        return await self.request('sendRichMessageDraft', payload)

    
    async def answer_inline_query(self, inline_query_id: str, results: list[InlineQueryResult], cache_time: int | None = None, is_personal: bool | None = None, next_offset: str | None = None, button: InlineQueryResultsButton | None = None) -> bool:
        """Use this method to send answers to an inline query. On success, True is returned. No more than 50 results per query are allowed."""
        payload = {
            'inline_query_id': inline_query_id,
            'results': results,
            'cache_time': cache_time,
            'is_personal': is_personal,
            'next_offset': next_offset,
            'button': button,
        }
        return await self.request('answerInlineQuery', payload)

    
    async def send_invoice(self, chat_id: int | str, title: str, description: str, payload: str, currency: str, prices: list[LabeledPrice], message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, provider_token: str | None = None, max_tip_amount: int | None = None, suggested_tip_amounts: list[int] | None = None, start_parameter: str | None = None, provider_data: str | None = None, photo_url: str | None = None, photo_size: int | None = None, photo_width: int | None = None, photo_height: int | None = None, need_name: bool | None = None, need_phone_number: bool | None = None, need_email: bool | None = None, need_shipping_address: bool | None = None, send_phone_number_to_provider: bool | None = None, send_email_to_provider: bool | None = None, is_flexible: bool | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: InlineKeyboardMarkup | None = None) -> Message:
        """Use this method to send invoices. On success, the sent Message is returned."""
        payload = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'direct_messages_topic_id': direct_messages_topic_id,
            'title': title,
            'description': description,
            'payload': payload,
            'provider_token': provider_token,
            'currency': currency,
            'prices': prices,
            'max_tip_amount': max_tip_amount,
            'suggested_tip_amounts': suggested_tip_amounts,
            'start_parameter': start_parameter,
            'provider_data': provider_data,
            'photo_url': photo_url,
            'photo_size': photo_size,
            'photo_width': photo_width,
            'photo_height': photo_height,
            'need_name': need_name,
            'need_phone_number': need_phone_number,
            'need_email': need_email,
            'need_shipping_address': need_shipping_address,
            'send_phone_number_to_provider': send_phone_number_to_provider,
            'send_email_to_provider': send_email_to_provider,
            'is_flexible': is_flexible,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'suggested_post_parameters': suggested_post_parameters,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup,
        }
        return await self.request('sendInvoice', payload)

    
    async def create_invoice_link(self, title: str, description: str, payload: str, currency: str, prices: list[LabeledPrice], business_connection_id: str | None = None, provider_token: str | None = None, subscription_period: int | None = None, max_tip_amount: int | None = None, suggested_tip_amounts: list[int] | None = None, provider_data: str | None = None, photo_url: str | None = None, photo_size: int | None = None, photo_width: int | None = None, photo_height: int | None = None, need_name: bool | None = None, need_phone_number: bool | None = None, need_email: bool | None = None, need_shipping_address: bool | None = None, send_phone_number_to_provider: bool | None = None, send_email_to_provider: bool | None = None, is_flexible: bool | None = None) -> str:
        """Use this method to create a link for an invoice. Returns the created invoice link as String on success."""
        payload = {
            'business_connection_id': business_connection_id,
            'title': title,
            'description': description,
            'payload': payload,
            'provider_token': provider_token,
            'currency': currency,
            'prices': prices,
            'subscription_period': subscription_period,
            'max_tip_amount': max_tip_amount,
            'suggested_tip_amounts': suggested_tip_amounts,
            'provider_data': provider_data,
            'photo_url': photo_url,
            'photo_size': photo_size,
            'photo_width': photo_width,
            'photo_height': photo_height,
            'need_name': need_name,
            'need_phone_number': need_phone_number,
            'need_email': need_email,
            'need_shipping_address': need_shipping_address,
            'send_phone_number_to_provider': send_phone_number_to_provider,
            'send_email_to_provider': send_email_to_provider,
            'is_flexible': is_flexible,
        }
        return await self.request('createInvoiceLink', payload)

    
    async def answer_shipping_query(self, shipping_query_id: str, ok: bool, shipping_options: list[ShippingOption] | None = None, error_message: str | None = None) -> bool:
        """If you sent an invoice requesting a shipping address and the parameter is_flexible was specified, the Bot API will send an Update with a shipping_query field to the bot. Use this method to reply to shipping queries. On success, True is returned."""
        payload = {
            'shipping_query_id': shipping_query_id,
            'ok': ok,
            'shipping_options': shipping_options,
            'error_message': error_message,
        }
        return await self.request('answerShippingQuery', payload)

    
    async def answer_pre_checkout_query(self, pre_checkout_query_id: str, ok: bool, error_message: str | None = None) -> bool:
        """Once the user has confirmed their payment and shipping details, the Bot API sends the final confirmation in the form of an Update with the field pre_checkout_query. Use this method to respond to such pre-checkout queries. On success, True is returned. Note: The Bot API must receive an answer within 10 seconds after the pre-checkout query was sent."""
        payload = {
            'pre_checkout_query_id': pre_checkout_query_id,
            'ok': ok,
            'error_message': error_message,
        }
        return await self.request('answerPreCheckoutQuery', payload)

    
    async def get_my_star_balance(self) -> StarAmount:
        """A method to get the current Telegram Stars balance of the bot. Requires no parameters. On success, returns a StarAmount object."""
        payload = {
        }
        return await self.request('getMyStarBalance', payload)

    
    async def get_star_transactions(self, offset: int | None = None, limit: int | None = None) -> StarTransactions:
        """Returns the bot's Telegram Star transactions in chronological order. On success, returns a StarTransactions object."""
        payload = {
            'offset': offset,
            'limit': limit,
        }
        return await self.request('getStarTransactions', payload)

    
    async def refund_star_payment(self, user_id: int, telegram_payment_charge_id: str) -> bool:
        """Refunds a successful payment in Telegram Stars. Returns True on success."""
        payload = {
            'user_id': user_id,
            'telegram_payment_charge_id': telegram_payment_charge_id,
        }
        return await self.request('refundStarPayment', payload)

    
    async def edit_user_star_subscription(self, user_id: int, telegram_payment_charge_id: str, is_canceled: bool) -> bool:
        """Allows the bot to cancel or re-enable extension of a subscription paid in Telegram Stars. Returns True on success."""
        payload = {
            'user_id': user_id,
            'telegram_payment_charge_id': telegram_payment_charge_id,
            'is_canceled': is_canceled,
        }
        return await self.request('editUserStarSubscription', payload)

    
    async def set_passport_data_errors(self, user_id: int, errors: list[PassportElementError]) -> bool:
        """Informs a user that some of the Telegram Passport elements they provided contains errors. The user will not be able to re-submit their Passport to you until the errors are fixed (the contents of the field for which you returned the error must change). Returns True on success. Use this if the data submitted by the user doesn't satisfy the standards your service requires for any reason. For example, if a birthday date seems invalid, a submitted document is blurry, a scan shows evidence of tampering, etc. Supply some details in the error message to make sure the user knows how to correct the issues."""
        payload = {
            'user_id': user_id,
            'errors': errors,
        }
        return await self.request('setPassportDataErrors', payload)

    
    async def send_game(self, chat_id: int | str, game_short_name: str, business_connection_id: str | None = None, message_thread_id: int | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: InlineKeyboardMarkup | None = None) -> Message:
        """Use this method to send a game. On success, the sent Message is returned."""
        payload = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'game_short_name': game_short_name,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup,
        }
        return await self.request('sendGame', payload)

    
    async def set_game_score(self, user_id: int, score: int, force: bool | None = None, disable_edit_message: bool | None = None, chat_id: int | None = None, message_id: int | None = None, inline_message_id: str | None = None) -> Message | bool:
        """Use this method to set the score of the specified user in a game message. On success, if the message is not an inline message, the Message is returned, otherwise True is returned. Returns an error, if the new score is not greater than the user's current score in the chat and force is False."""
        payload = {
            'user_id': user_id,
            'score': score,
            'force': force,
            'disable_edit_message': disable_edit_message,
            'chat_id': chat_id,
            'message_id': message_id,
            'inline_message_id': inline_message_id,
        }
        return await self.request('setGameScore', payload)

    
    async def get_game_high_scores(self, user_id: int, chat_id: int | None = None, message_id: int | None = None, inline_message_id: str | None = None) -> list[GameHighScore]:
        """Use this method to get data for high score tables. Will return the score of the specified user and several of their neighbors in a game. Returns an Array of GameHighScore objects."""
        payload = {
            'user_id': user_id,
            'chat_id': chat_id,
            'message_id': message_id,
            'inline_message_id': inline_message_id,
        }
        return await self.request('getGameHighScores', payload)

    