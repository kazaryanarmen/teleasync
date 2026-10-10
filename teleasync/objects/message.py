from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .animation import Animation
    
    from .audio import Audio
    
    from .chat import Chat
    
    from .chat_background import ChatBackground
    
    from .chat_boost_added import ChatBoostAdded
    
    from .chat_owner_changed import ChatOwnerChanged
    
    from .chat_owner_left import ChatOwnerLeft
    
    from .chat_shared import ChatShared
    
    from .checklist import Checklist
    
    from .checklist_tasks_added import ChecklistTasksAdded
    
    from .checklist_tasks_done import ChecklistTasksDone
    
    from .community_chat_added import CommunityChatAdded
    
    from .community_chat_joined import CommunityChatJoined
    
    from .community_chat_removed import CommunityChatRemoved
    
    from .contact import Contact
    
    from .dice import Dice
    
    from .direct_message_price_changed import DirectMessagePriceChanged
    
    from .direct_messages_topic import DirectMessagesTopic
    
    from .document import Document
    
    from .external_reply_info import ExternalReplyInfo
    
    from .forum_topic_closed import ForumTopicClosed
    
    from .forum_topic_created import ForumTopicCreated
    
    from .forum_topic_edited import ForumTopicEdited
    
    from .forum_topic_reopened import ForumTopicReopened
    
    from .game import Game
    
    from .general_forum_topic_hidden import GeneralForumTopicHidden
    
    from .general_forum_topic_unhidden import GeneralForumTopicUnhidden
    
    from .gift_info import GiftInfo
    
    from .giveaway import Giveaway
    
    from .giveaway_completed import GiveawayCompleted
    
    from .giveaway_created import GiveawayCreated
    
    from .giveaway_winners import GiveawayWinners
    
    from .inline_keyboard_markup import InlineKeyboardMarkup
    
    from .invoice import Invoice
    
    from .link_preview_options import LinkPreviewOptions
    
    from .live_photo import LivePhoto
    
    from .location import Location
    
    from .managed_bot_created import ManagedBotCreated
    
    from .maybe_inaccessible_message import MaybeInaccessibleMessage
    
    from .message_auto_delete_timer_changed import MessageAutoDeleteTimerChanged
    
    from .message_entity import MessageEntity
    
    from .message_origin import MessageOrigin
    
    from .paid_media_info import PaidMediaInfo
    
    from .paid_message_price_changed import PaidMessagePriceChanged
    
    from .passport_data import PassportData
    
    from .photo_size import PhotoSize
    
    from .poll import Poll
    
    from .poll_option_added import PollOptionAdded
    
    from .poll_option_deleted import PollOptionDeleted
    
    from .proximity_alert_triggered import ProximityAlertTriggered
    
    from .refunded_payment import RefundedPayment
    
    from .rich_message import RichMessage
    
    from .sticker import Sticker
    
    from .story import Story
    
    from .successful_payment import SuccessfulPayment
    
    from .suggested_post_approval_failed import SuggestedPostApprovalFailed
    
    from .suggested_post_approved import SuggestedPostApproved
    
    from .suggested_post_declined import SuggestedPostDeclined
    
    from .suggested_post_info import SuggestedPostInfo
    
    from .suggested_post_paid import SuggestedPostPaid
    
    from .suggested_post_refunded import SuggestedPostRefunded
    
    from .text_quote import TextQuote
    
    from .unique_gift_info import UniqueGiftInfo
    
    from .user import User
    
    from .users_shared import UsersShared
    
    from .venue import Venue
    
    from .video import Video
    
    from .video_chat_ended import VideoChatEnded
    
    from .video_chat_participants_invited import VideoChatParticipantsInvited
    
    from .video_chat_scheduled import VideoChatScheduled
    
    from .video_chat_started import VideoChatStarted
    
    from .video_note import VideoNote
    
    from .voice import Voice
    
    from .web_app_data import WebAppData
    
    from .write_access_allowed import WriteAccessAllowed
    


class Message:
    """This object represents a message."""

    def __init__(self, message_id: int, date: int, chat: Chat, message_thread_id: int | None = None, direct_messages_topic: DirectMessagesTopic | None = None, from_: User | None = None, sender_chat: Chat | None = None, sender_boost_count: int | None = None, sender_business_bot: User | None = None, sender_tag: str | None = None, receiver_user: User | None = None, ephemeral_message_id: int | None = None, guest_query_id: str | None = None, business_connection_id: str | None = None, forward_origin: MessageOrigin | None = None, is_topic_message: bool | None = None, is_automatic_forward: bool | None = None, reply_to_message: Message | None = None, external_reply: ExternalReplyInfo | None = None, quote: TextQuote | None = None, reply_to_story: Story | None = None, reply_to_checklist_task_id: int | None = None, reply_to_poll_option_id: str | None = None, via_bot: User | None = None, guest_bot_caller_user: User | None = None, guest_bot_caller_chat: Chat | None = None, edit_date: int | None = None, has_protected_content: bool | None = None, is_from_offline: bool | None = None, is_paid_post: bool | None = None, media_group_id: str | None = None, author_signature: str | None = None, paid_star_count: int | None = None, text: str | None = None, entities: list[MessageEntity] | None = None, link_preview_options: LinkPreviewOptions | None = None, suggested_post_info: SuggestedPostInfo | None = None, effect_id: str | None = None, rich_message: RichMessage | None = None, animation_: Animation | None = None, audio_: Audio | None = None, document_: Document | None = None, live_photo: LivePhoto | None = None, paid_media: PaidMediaInfo | None = None, photo_: list[PhotoSize] | None = None, sticker_: Sticker | None = None, story: Story | None = None, video_: Video | None = None, video_note: VideoNote | None = None, voice_: Voice | None = None, caption: str | None = None, caption_entities: list[MessageEntity] | None = None, show_caption_above_media: bool | None = None, has_media_spoiler: bool | None = None, checklist: Checklist | None = None, contact: Contact | None = None, dice: Dice | None = None, game: Game | None = None, poll: Poll | None = None, venue: Venue | None = None, location: Location | None = None, new_chat_members: list[User] | None = None, left_chat_member: User | None = None, chat_owner_left: ChatOwnerLeft | None = None, chat_owner_changed: ChatOwnerChanged | None = None, new_chat_title: str | None = None, new_chat_photo: list[PhotoSize] | None = None, delete_chat_photo: bool | None = None, group_chat_created: bool | None = None, supergroup_chat_created: bool | None = None, channel_chat_created: bool | None = None, message_auto_delete_timer_changed: MessageAutoDeleteTimerChanged | None = None, migrate_to_chat_id: int | None = None, migrate_from_chat_id: int | None = None, pinned_message: MaybeInaccessibleMessage | None = None, invoice: Invoice | None = None, successful_payment: SuccessfulPayment | None = None, refunded_payment: RefundedPayment | None = None, users_shared: UsersShared | None = None, chat_shared: ChatShared | None = None, gift: GiftInfo | None = None, unique_gift: UniqueGiftInfo | None = None, gift_upgrade_sent: GiftInfo | None = None, connected_website: str | None = None, write_access_allowed: WriteAccessAllowed | None = None, passport_data: PassportData | None = None, proximity_alert_triggered: ProximityAlertTriggered | None = None, boost_added: ChatBoostAdded | None = None, chat_background_set: ChatBackground | None = None, checklist_tasks_done: ChecklistTasksDone | None = None, checklist_tasks_added: ChecklistTasksAdded | None = None, community_chat_added: CommunityChatAdded | None = None, community_chat_joined: CommunityChatJoined | None = None, community_chat_removed: CommunityChatRemoved | None = None, direct_message_price_changed: DirectMessagePriceChanged | None = None, forum_topic_created: ForumTopicCreated | None = None, forum_topic_edited: ForumTopicEdited | None = None, forum_topic_closed: ForumTopicClosed | None = None, forum_topic_reopened: ForumTopicReopened | None = None, general_forum_topic_hidden: GeneralForumTopicHidden | None = None, general_forum_topic_unhidden: GeneralForumTopicUnhidden | None = None, giveaway_created: GiveawayCreated | None = None, giveaway: Giveaway | None = None, giveaway_winners: GiveawayWinners | None = None, giveaway_completed: GiveawayCompleted | None = None, managed_bot_created: ManagedBotCreated | None = None, paid_message_price_changed: PaidMessagePriceChanged | None = None, poll_option_added: PollOptionAdded | None = None, poll_option_deleted: PollOptionDeleted | None = None, suggested_post_approved: SuggestedPostApproved | None = None, suggested_post_approval_failed: SuggestedPostApprovalFailed | None = None, suggested_post_declined: SuggestedPostDeclined | None = None, suggested_post_paid: SuggestedPostPaid | None = None, suggested_post_refunded: SuggestedPostRefunded | None = None, video_chat_scheduled: VideoChatScheduled | None = None, video_chat_started: VideoChatStarted | None = None, video_chat_ended: VideoChatEnded | None = None, video_chat_participants_invited: VideoChatParticipantsInvited | None = None, web_app_data: WebAppData | None = None, reply_markup: InlineKeyboardMarkup | None = None):
        self.message_id: int = message_id
        self.date: int = date
        self.chat: Chat = chat
        self.message_thread_id: int | None = message_thread_id
        self.direct_messages_topic: DirectMessagesTopic | None = direct_messages_topic
        self.from_: User | None = from_
        self.sender_chat: Chat | None = sender_chat
        self.sender_boost_count: int | None = sender_boost_count
        self.sender_business_bot: User | None = sender_business_bot
        self.sender_tag: str | None = sender_tag
        self.receiver_user: User | None = receiver_user
        self.ephemeral_message_id: int | None = ephemeral_message_id
        self.guest_query_id: str | None = guest_query_id
        self.business_connection_id: str | None = business_connection_id
        self.forward_origin: MessageOrigin | None = forward_origin
        self.is_topic_message: bool | None = is_topic_message
        self.is_automatic_forward: bool | None = is_automatic_forward
        self.reply_to_message: Message | None = reply_to_message
        self.external_reply: ExternalReplyInfo | None = external_reply
        self.quote: TextQuote | None = quote
        self.reply_to_story: Story | None = reply_to_story
        self.reply_to_checklist_task_id: int | None = reply_to_checklist_task_id
        self.reply_to_poll_option_id: str | None = reply_to_poll_option_id
        self.via_bot: User | None = via_bot
        self.guest_bot_caller_user: User | None = guest_bot_caller_user
        self.guest_bot_caller_chat: Chat | None = guest_bot_caller_chat
        self.edit_date: int | None = edit_date
        self.has_protected_content: bool | None = has_protected_content
        self.is_from_offline: bool | None = is_from_offline
        self.is_paid_post: bool | None = is_paid_post
        self.media_group_id: str | None = media_group_id
        self.author_signature: str | None = author_signature
        self.paid_star_count: int | None = paid_star_count
        self.text: str | None = text
        self.entities: list[MessageEntity] | None = entities
        self.link_preview_options: LinkPreviewOptions | None = link_preview_options
        self.suggested_post_info: SuggestedPostInfo | None = suggested_post_info
        self.effect_id: str | None = effect_id
        self.rich_message: RichMessage | None = rich_message
        self.animation_: Animation | None = animation_
        self.audio_: Audio | None = audio_
        self.document_: Document | None = document_
        self.live_photo: LivePhoto | None = live_photo
        self.paid_media: PaidMediaInfo | None = paid_media
        self.photo_: list[PhotoSize] | None = photo_
        self.sticker_: Sticker | None = sticker_
        self.story: Story | None = story
        self.video_: Video | None = video_
        self.video_note: VideoNote | None = video_note
        self.voice_: Voice | None = voice_
        self.caption: str | None = caption
        self.caption_entities: list[MessageEntity] | None = caption_entities
        self.show_caption_above_media: bool | None = show_caption_above_media
        self.has_media_spoiler: bool | None = has_media_spoiler
        self.checklist: Checklist | None = checklist
        self.contact: Contact | None = contact
        self.dice: Dice | None = dice
        self.game: Game | None = game
        self.poll: Poll | None = poll
        self.venue: Venue | None = venue
        self.location: Location | None = location
        self.new_chat_members: list[User] | None = new_chat_members
        self.left_chat_member: User | None = left_chat_member
        self.chat_owner_left: ChatOwnerLeft | None = chat_owner_left
        self.chat_owner_changed: ChatOwnerChanged | None = chat_owner_changed
        self.new_chat_title: str | None = new_chat_title
        self.new_chat_photo: list[PhotoSize] | None = new_chat_photo
        self.delete_chat_photo: bool | None = delete_chat_photo
        self.group_chat_created: bool | None = group_chat_created
        self.supergroup_chat_created: bool | None = supergroup_chat_created
        self.channel_chat_created: bool | None = channel_chat_created
        self.message_auto_delete_timer_changed: MessageAutoDeleteTimerChanged | None = message_auto_delete_timer_changed
        self.migrate_to_chat_id: int | None = migrate_to_chat_id
        self.migrate_from_chat_id: int | None = migrate_from_chat_id
        self.pinned_message: MaybeInaccessibleMessage | None = pinned_message
        self.invoice: Invoice | None = invoice
        self.successful_payment: SuccessfulPayment | None = successful_payment
        self.refunded_payment: RefundedPayment | None = refunded_payment
        self.users_shared: UsersShared | None = users_shared
        self.chat_shared: ChatShared | None = chat_shared
        self.gift: GiftInfo | None = gift
        self.unique_gift: UniqueGiftInfo | None = unique_gift
        self.gift_upgrade_sent: GiftInfo | None = gift_upgrade_sent
        self.connected_website: str | None = connected_website
        self.write_access_allowed: WriteAccessAllowed | None = write_access_allowed
        self.passport_data: PassportData | None = passport_data
        self.proximity_alert_triggered: ProximityAlertTriggered | None = proximity_alert_triggered
        self.boost_added: ChatBoostAdded | None = boost_added
        self.chat_background_set: ChatBackground | None = chat_background_set
        self.checklist_tasks_done: ChecklistTasksDone | None = checklist_tasks_done
        self.checklist_tasks_added: ChecklistTasksAdded | None = checklist_tasks_added
        self.community_chat_added: CommunityChatAdded | None = community_chat_added
        self.community_chat_joined: CommunityChatJoined | None = community_chat_joined
        self.community_chat_removed: CommunityChatRemoved | None = community_chat_removed
        self.direct_message_price_changed: DirectMessagePriceChanged | None = direct_message_price_changed
        self.forum_topic_created: ForumTopicCreated | None = forum_topic_created
        self.forum_topic_edited: ForumTopicEdited | None = forum_topic_edited
        self.forum_topic_closed: ForumTopicClosed | None = forum_topic_closed
        self.forum_topic_reopened: ForumTopicReopened | None = forum_topic_reopened
        self.general_forum_topic_hidden: GeneralForumTopicHidden | None = general_forum_topic_hidden
        self.general_forum_topic_unhidden: GeneralForumTopicUnhidden | None = general_forum_topic_unhidden
        self.giveaway_created: GiveawayCreated | None = giveaway_created
        self.giveaway: Giveaway | None = giveaway
        self.giveaway_winners: GiveawayWinners | None = giveaway_winners
        self.giveaway_completed: GiveawayCompleted | None = giveaway_completed
        self.managed_bot_created: ManagedBotCreated | None = managed_bot_created
        self.paid_message_price_changed: PaidMessagePriceChanged | None = paid_message_price_changed
        self.poll_option_added: PollOptionAdded | None = poll_option_added
        self.poll_option_deleted: PollOptionDeleted | None = poll_option_deleted
        self.suggested_post_approved: SuggestedPostApproved | None = suggested_post_approved
        self.suggested_post_approval_failed: SuggestedPostApprovalFailed | None = suggested_post_approval_failed
        self.suggested_post_declined: SuggestedPostDeclined | None = suggested_post_declined
        self.suggested_post_paid: SuggestedPostPaid | None = suggested_post_paid
        self.suggested_post_refunded: SuggestedPostRefunded | None = suggested_post_refunded
        self.video_chat_scheduled: VideoChatScheduled | None = video_chat_scheduled
        self.video_chat_started: VideoChatStarted | None = video_chat_started
        self.video_chat_ended: VideoChatEnded | None = video_chat_ended
        self.video_chat_participants_invited: VideoChatParticipantsInvited | None = video_chat_participants_invited
        self.web_app_data: WebAppData | None = web_app_data
        self.reply_markup: InlineKeyboardMarkup | None = reply_markup

    def to_dict(self) -> dict:
        def _serialize(v):
            if hasattr(v, 'to_dict'):
                return v.to_dict()
            elif isinstance(v, list):
                return [_serialize(i) for i in v]
            elif isinstance(v, dict):
                return {k: _serialize(val) for k, val in v.items()}
            return v
        result = {}
        if self.message_id is not None:
            result['message_id'] = _serialize(self.message_id)
        if self.date is not None:
            result['date'] = _serialize(self.date)
        if self.chat is not None:
            result['chat'] = _serialize(self.chat)
        if self.message_thread_id is not None:
            result['message_thread_id'] = _serialize(self.message_thread_id)
        if self.direct_messages_topic is not None:
            result['direct_messages_topic'] = _serialize(self.direct_messages_topic)
        if self.from_ is not None:
            result['from'] = _serialize(self.from_)
        if self.sender_chat is not None:
            result['sender_chat'] = _serialize(self.sender_chat)
        if self.sender_boost_count is not None:
            result['sender_boost_count'] = _serialize(self.sender_boost_count)
        if self.sender_business_bot is not None:
            result['sender_business_bot'] = _serialize(self.sender_business_bot)
        if self.sender_tag is not None:
            result['sender_tag'] = _serialize(self.sender_tag)
        if self.receiver_user is not None:
            result['receiver_user'] = _serialize(self.receiver_user)
        if self.ephemeral_message_id is not None:
            result['ephemeral_message_id'] = _serialize(self.ephemeral_message_id)
        if self.guest_query_id is not None:
            result['guest_query_id'] = _serialize(self.guest_query_id)
        if self.business_connection_id is not None:
            result['business_connection_id'] = _serialize(self.business_connection_id)
        if self.forward_origin is not None:
            result['forward_origin'] = _serialize(self.forward_origin)
        if self.is_topic_message is not None:
            result['is_topic_message'] = _serialize(self.is_topic_message)
        if self.is_automatic_forward is not None:
            result['is_automatic_forward'] = _serialize(self.is_automatic_forward)
        if self.reply_to_message is not None:
            result['reply_to_message'] = _serialize(self.reply_to_message)
        if self.external_reply is not None:
            result['external_reply'] = _serialize(self.external_reply)
        if self.quote is not None:
            result['quote'] = _serialize(self.quote)
        if self.reply_to_story is not None:
            result['reply_to_story'] = _serialize(self.reply_to_story)
        if self.reply_to_checklist_task_id is not None:
            result['reply_to_checklist_task_id'] = _serialize(self.reply_to_checklist_task_id)
        if self.reply_to_poll_option_id is not None:
            result['reply_to_poll_option_id'] = _serialize(self.reply_to_poll_option_id)
        if self.via_bot is not None:
            result['via_bot'] = _serialize(self.via_bot)
        if self.guest_bot_caller_user is not None:
            result['guest_bot_caller_user'] = _serialize(self.guest_bot_caller_user)
        if self.guest_bot_caller_chat is not None:
            result['guest_bot_caller_chat'] = _serialize(self.guest_bot_caller_chat)
        if self.edit_date is not None:
            result['edit_date'] = _serialize(self.edit_date)
        if self.has_protected_content is not None:
            result['has_protected_content'] = _serialize(self.has_protected_content)
        if self.is_from_offline is not None:
            result['is_from_offline'] = _serialize(self.is_from_offline)
        if self.is_paid_post is not None:
            result['is_paid_post'] = _serialize(self.is_paid_post)
        if self.media_group_id is not None:
            result['media_group_id'] = _serialize(self.media_group_id)
        if self.author_signature is not None:
            result['author_signature'] = _serialize(self.author_signature)
        if self.paid_star_count is not None:
            result['paid_star_count'] = _serialize(self.paid_star_count)
        if self.text is not None:
            result['text'] = _serialize(self.text)
        if self.entities is not None:
            result['entities'] = _serialize(self.entities)
        if self.link_preview_options is not None:
            result['link_preview_options'] = _serialize(self.link_preview_options)
        if self.suggested_post_info is not None:
            result['suggested_post_info'] = _serialize(self.suggested_post_info)
        if self.effect_id is not None:
            result['effect_id'] = _serialize(self.effect_id)
        if self.rich_message is not None:
            result['rich_message'] = _serialize(self.rich_message)
        if self.animation_ is not None:
            result['animation'] = _serialize(self.animation_)
        if self.audio_ is not None:
            result['audio'] = _serialize(self.audio_)
        if self.document_ is not None:
            result['document'] = _serialize(self.document_)
        if self.live_photo is not None:
            result['live_photo'] = _serialize(self.live_photo)
        if self.paid_media is not None:
            result['paid_media'] = _serialize(self.paid_media)
        if self.photo_ is not None:
            result['photo'] = _serialize(self.photo_)
        if self.sticker_ is not None:
            result['sticker'] = _serialize(self.sticker_)
        if self.story is not None:
            result['story'] = _serialize(self.story)
        if self.video_ is not None:
            result['video'] = _serialize(self.video_)
        if self.video_note is not None:
            result['video_note'] = _serialize(self.video_note)
        if self.voice_ is not None:
            result['voice'] = _serialize(self.voice_)
        if self.caption is not None:
            result['caption'] = _serialize(self.caption)
        if self.caption_entities is not None:
            result['caption_entities'] = _serialize(self.caption_entities)
        if self.show_caption_above_media is not None:
            result['show_caption_above_media'] = _serialize(self.show_caption_above_media)
        if self.has_media_spoiler is not None:
            result['has_media_spoiler'] = _serialize(self.has_media_spoiler)
        if self.checklist is not None:
            result['checklist'] = _serialize(self.checklist)
        if self.contact is not None:
            result['contact'] = _serialize(self.contact)
        if self.dice is not None:
            result['dice'] = _serialize(self.dice)
        if self.game is not None:
            result['game'] = _serialize(self.game)
        if self.poll is not None:
            result['poll'] = _serialize(self.poll)
        if self.venue is not None:
            result['venue'] = _serialize(self.venue)
        if self.location is not None:
            result['location'] = _serialize(self.location)
        if self.new_chat_members is not None:
            result['new_chat_members'] = _serialize(self.new_chat_members)
        if self.left_chat_member is not None:
            result['left_chat_member'] = _serialize(self.left_chat_member)
        if self.chat_owner_left is not None:
            result['chat_owner_left'] = _serialize(self.chat_owner_left)
        if self.chat_owner_changed is not None:
            result['chat_owner_changed'] = _serialize(self.chat_owner_changed)
        if self.new_chat_title is not None:
            result['new_chat_title'] = _serialize(self.new_chat_title)
        if self.new_chat_photo is not None:
            result['new_chat_photo'] = _serialize(self.new_chat_photo)
        if self.delete_chat_photo is not None:
            result['delete_chat_photo'] = _serialize(self.delete_chat_photo)
        if self.group_chat_created is not None:
            result['group_chat_created'] = _serialize(self.group_chat_created)
        if self.supergroup_chat_created is not None:
            result['supergroup_chat_created'] = _serialize(self.supergroup_chat_created)
        if self.channel_chat_created is not None:
            result['channel_chat_created'] = _serialize(self.channel_chat_created)
        if self.message_auto_delete_timer_changed is not None:
            result['message_auto_delete_timer_changed'] = _serialize(self.message_auto_delete_timer_changed)
        if self.migrate_to_chat_id is not None:
            result['migrate_to_chat_id'] = _serialize(self.migrate_to_chat_id)
        if self.migrate_from_chat_id is not None:
            result['migrate_from_chat_id'] = _serialize(self.migrate_from_chat_id)
        if self.pinned_message is not None:
            result['pinned_message'] = _serialize(self.pinned_message)
        if self.invoice is not None:
            result['invoice'] = _serialize(self.invoice)
        if self.successful_payment is not None:
            result['successful_payment'] = _serialize(self.successful_payment)
        if self.refunded_payment is not None:
            result['refunded_payment'] = _serialize(self.refunded_payment)
        if self.users_shared is not None:
            result['users_shared'] = _serialize(self.users_shared)
        if self.chat_shared is not None:
            result['chat_shared'] = _serialize(self.chat_shared)
        if self.gift is not None:
            result['gift'] = _serialize(self.gift)
        if self.unique_gift is not None:
            result['unique_gift'] = _serialize(self.unique_gift)
        if self.gift_upgrade_sent is not None:
            result['gift_upgrade_sent'] = _serialize(self.gift_upgrade_sent)
        if self.connected_website is not None:
            result['connected_website'] = _serialize(self.connected_website)
        if self.write_access_allowed is not None:
            result['write_access_allowed'] = _serialize(self.write_access_allowed)
        if self.passport_data is not None:
            result['passport_data'] = _serialize(self.passport_data)
        if self.proximity_alert_triggered is not None:
            result['proximity_alert_triggered'] = _serialize(self.proximity_alert_triggered)
        if self.boost_added is not None:
            result['boost_added'] = _serialize(self.boost_added)
        if self.chat_background_set is not None:
            result['chat_background_set'] = _serialize(self.chat_background_set)
        if self.checklist_tasks_done is not None:
            result['checklist_tasks_done'] = _serialize(self.checklist_tasks_done)
        if self.checklist_tasks_added is not None:
            result['checklist_tasks_added'] = _serialize(self.checklist_tasks_added)
        if self.community_chat_added is not None:
            result['community_chat_added'] = _serialize(self.community_chat_added)
        if self.community_chat_joined is not None:
            result['community_chat_joined'] = _serialize(self.community_chat_joined)
        if self.community_chat_removed is not None:
            result['community_chat_removed'] = _serialize(self.community_chat_removed)
        if self.direct_message_price_changed is not None:
            result['direct_message_price_changed'] = _serialize(self.direct_message_price_changed)
        if self.forum_topic_created is not None:
            result['forum_topic_created'] = _serialize(self.forum_topic_created)
        if self.forum_topic_edited is not None:
            result['forum_topic_edited'] = _serialize(self.forum_topic_edited)
        if self.forum_topic_closed is not None:
            result['forum_topic_closed'] = _serialize(self.forum_topic_closed)
        if self.forum_topic_reopened is not None:
            result['forum_topic_reopened'] = _serialize(self.forum_topic_reopened)
        if self.general_forum_topic_hidden is not None:
            result['general_forum_topic_hidden'] = _serialize(self.general_forum_topic_hidden)
        if self.general_forum_topic_unhidden is not None:
            result['general_forum_topic_unhidden'] = _serialize(self.general_forum_topic_unhidden)
        if self.giveaway_created is not None:
            result['giveaway_created'] = _serialize(self.giveaway_created)
        if self.giveaway is not None:
            result['giveaway'] = _serialize(self.giveaway)
        if self.giveaway_winners is not None:
            result['giveaway_winners'] = _serialize(self.giveaway_winners)
        if self.giveaway_completed is not None:
            result['giveaway_completed'] = _serialize(self.giveaway_completed)
        if self.managed_bot_created is not None:
            result['managed_bot_created'] = _serialize(self.managed_bot_created)
        if self.paid_message_price_changed is not None:
            result['paid_message_price_changed'] = _serialize(self.paid_message_price_changed)
        if self.poll_option_added is not None:
            result['poll_option_added'] = _serialize(self.poll_option_added)
        if self.poll_option_deleted is not None:
            result['poll_option_deleted'] = _serialize(self.poll_option_deleted)
        if self.suggested_post_approved is not None:
            result['suggested_post_approved'] = _serialize(self.suggested_post_approved)
        if self.suggested_post_approval_failed is not None:
            result['suggested_post_approval_failed'] = _serialize(self.suggested_post_approval_failed)
        if self.suggested_post_declined is not None:
            result['suggested_post_declined'] = _serialize(self.suggested_post_declined)
        if self.suggested_post_paid is not None:
            result['suggested_post_paid'] = _serialize(self.suggested_post_paid)
        if self.suggested_post_refunded is not None:
            result['suggested_post_refunded'] = _serialize(self.suggested_post_refunded)
        if self.video_chat_scheduled is not None:
            result['video_chat_scheduled'] = _serialize(self.video_chat_scheduled)
        if self.video_chat_started is not None:
            result['video_chat_started'] = _serialize(self.video_chat_started)
        if self.video_chat_ended is not None:
            result['video_chat_ended'] = _serialize(self.video_chat_ended)
        if self.video_chat_participants_invited is not None:
            result['video_chat_participants_invited'] = _serialize(self.video_chat_participants_invited)
        if self.web_app_data is not None:
            result['web_app_data'] = _serialize(self.web_app_data)
        if self.reply_markup is not None:
            result['reply_markup'] = _serialize(self.reply_markup)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'Message' | None:
        if not data:
            return None
        from .animation import Animation
        from .audio import Audio
        from .chat import Chat
        from .chat_background import ChatBackground
        from .chat_boost_added import ChatBoostAdded
        from .chat_owner_changed import ChatOwnerChanged
        from .chat_owner_left import ChatOwnerLeft
        from .chat_shared import ChatShared
        from .checklist import Checklist
        from .checklist_tasks_added import ChecklistTasksAdded
        from .checklist_tasks_done import ChecklistTasksDone
        from .community_chat_added import CommunityChatAdded
        from .community_chat_joined import CommunityChatJoined
        from .community_chat_removed import CommunityChatRemoved
        from .contact import Contact
        from .dice import Dice
        from .direct_message_price_changed import DirectMessagePriceChanged
        from .direct_messages_topic import DirectMessagesTopic
        from .document import Document
        from .external_reply_info import ExternalReplyInfo
        from .forum_topic_closed import ForumTopicClosed
        from .forum_topic_created import ForumTopicCreated
        from .forum_topic_edited import ForumTopicEdited
        from .forum_topic_reopened import ForumTopicReopened
        from .game import Game
        from .general_forum_topic_hidden import GeneralForumTopicHidden
        from .general_forum_topic_unhidden import GeneralForumTopicUnhidden
        from .gift_info import GiftInfo
        from .giveaway import Giveaway
        from .giveaway_completed import GiveawayCompleted
        from .giveaway_created import GiveawayCreated
        from .giveaway_winners import GiveawayWinners
        from .inline_keyboard_markup import InlineKeyboardMarkup
        from .invoice import Invoice
        from .link_preview_options import LinkPreviewOptions
        from .live_photo import LivePhoto
        from .location import Location
        from .managed_bot_created import ManagedBotCreated
        from .maybe_inaccessible_message import MaybeInaccessibleMessage
        from .message_auto_delete_timer_changed import MessageAutoDeleteTimerChanged
        from .message_entity import MessageEntity
        from .message_origin import MessageOrigin
        from .paid_media_info import PaidMediaInfo
        from .paid_message_price_changed import PaidMessagePriceChanged
        from .passport_data import PassportData
        from .photo_size import PhotoSize
        from .poll import Poll
        from .poll_option_added import PollOptionAdded
        from .poll_option_deleted import PollOptionDeleted
        from .proximity_alert_triggered import ProximityAlertTriggered
        from .refunded_payment import RefundedPayment
        from .rich_message import RichMessage
        from .sticker import Sticker
        from .story import Story
        from .successful_payment import SuccessfulPayment
        from .suggested_post_approval_failed import SuggestedPostApprovalFailed
        from .suggested_post_approved import SuggestedPostApproved
        from .suggested_post_declined import SuggestedPostDeclined
        from .suggested_post_info import SuggestedPostInfo
        from .suggested_post_paid import SuggestedPostPaid
        from .suggested_post_refunded import SuggestedPostRefunded
        from .text_quote import TextQuote
        from .unique_gift_info import UniqueGiftInfo
        from .user import User
        from .users_shared import UsersShared
        from .venue import Venue
        from .video import Video
        from .video_chat_ended import VideoChatEnded
        from .video_chat_participants_invited import VideoChatParticipantsInvited
        from .video_chat_scheduled import VideoChatScheduled
        from .video_chat_started import VideoChatStarted
        from .video_note import VideoNote
        from .voice import Voice
        from .web_app_data import WebAppData
        from .write_access_allowed import WriteAccessAllowed
        return cls(
            message_id=data.get('message_id'),
            date=data.get('date'),
            chat=Chat.from_dict(data.get('chat')),
            message_thread_id=data.get('message_thread_id'),
            direct_messages_topic=DirectMessagesTopic.from_dict(data.get('direct_messages_topic')),
            from_=User.from_dict(data.get('from')),
            sender_chat=Chat.from_dict(data.get('sender_chat')),
            sender_boost_count=data.get('sender_boost_count'),
            sender_business_bot=User.from_dict(data.get('sender_business_bot')),
            sender_tag=data.get('sender_tag'),
            receiver_user=User.from_dict(data.get('receiver_user')),
            ephemeral_message_id=data.get('ephemeral_message_id'),
            guest_query_id=data.get('guest_query_id'),
            business_connection_id=data.get('business_connection_id'),
            forward_origin=MessageOrigin.from_dict(data.get('forward_origin')),
            is_topic_message=data.get('is_topic_message'),
            is_automatic_forward=data.get('is_automatic_forward'),
            reply_to_message=Message.from_dict(data.get('reply_to_message')),
            external_reply=ExternalReplyInfo.from_dict(data.get('external_reply')),
            quote=TextQuote.from_dict(data.get('quote')),
            reply_to_story=Story.from_dict(data.get('reply_to_story')),
            reply_to_checklist_task_id=data.get('reply_to_checklist_task_id'),
            reply_to_poll_option_id=data.get('reply_to_poll_option_id'),
            via_bot=User.from_dict(data.get('via_bot')),
            guest_bot_caller_user=User.from_dict(data.get('guest_bot_caller_user')),
            guest_bot_caller_chat=Chat.from_dict(data.get('guest_bot_caller_chat')),
            edit_date=data.get('edit_date'),
            has_protected_content=data.get('has_protected_content'),
            is_from_offline=data.get('is_from_offline'),
            is_paid_post=data.get('is_paid_post'),
            media_group_id=data.get('media_group_id'),
            author_signature=data.get('author_signature'),
            paid_star_count=data.get('paid_star_count'),
            text=data.get('text'),
            entities=[MessageEntity.from_dict(i) for i in data.get('entities')] if data.get('entities') else None,
            link_preview_options=LinkPreviewOptions.from_dict(data.get('link_preview_options')),
            suggested_post_info=SuggestedPostInfo.from_dict(data.get('suggested_post_info')),
            effect_id=data.get('effect_id'),
            rich_message=RichMessage.from_dict(data.get('rich_message')),
            animation_=Animation.from_dict(data.get('animation')),
            audio_=Audio.from_dict(data.get('audio')),
            document_=Document.from_dict(data.get('document')),
            live_photo=LivePhoto.from_dict(data.get('live_photo')),
            paid_media=PaidMediaInfo.from_dict(data.get('paid_media')),
            photo_=[PhotoSize.from_dict(i) for i in data.get('photo')] if data.get('photo') else None,
            sticker_=Sticker.from_dict(data.get('sticker')),
            story=Story.from_dict(data.get('story')),
            video_=Video.from_dict(data.get('video')),
            video_note=VideoNote.from_dict(data.get('video_note')),
            voice_=Voice.from_dict(data.get('voice')),
            caption=data.get('caption'),
            caption_entities=[MessageEntity.from_dict(i) for i in data.get('caption_entities')] if data.get('caption_entities') else None,
            show_caption_above_media=data.get('show_caption_above_media'),
            has_media_spoiler=data.get('has_media_spoiler'),
            checklist=Checklist.from_dict(data.get('checklist')),
            contact=Contact.from_dict(data.get('contact')),
            dice=Dice.from_dict(data.get('dice')),
            game=Game.from_dict(data.get('game')),
            poll=Poll.from_dict(data.get('poll')),
            venue=Venue.from_dict(data.get('venue')),
            location=Location.from_dict(data.get('location')),
            new_chat_members=[User.from_dict(i) for i in data.get('new_chat_members')] if data.get('new_chat_members') else None,
            left_chat_member=User.from_dict(data.get('left_chat_member')),
            chat_owner_left=ChatOwnerLeft.from_dict(data.get('chat_owner_left')),
            chat_owner_changed=ChatOwnerChanged.from_dict(data.get('chat_owner_changed')),
            new_chat_title=data.get('new_chat_title'),
            new_chat_photo=[PhotoSize.from_dict(i) for i in data.get('new_chat_photo')] if data.get('new_chat_photo') else None,
            delete_chat_photo=data.get('delete_chat_photo'),
            group_chat_created=data.get('group_chat_created'),
            supergroup_chat_created=data.get('supergroup_chat_created'),
            channel_chat_created=data.get('channel_chat_created'),
            message_auto_delete_timer_changed=MessageAutoDeleteTimerChanged.from_dict(data.get('message_auto_delete_timer_changed')),
            migrate_to_chat_id=data.get('migrate_to_chat_id'),
            migrate_from_chat_id=data.get('migrate_from_chat_id'),
            pinned_message=MaybeInaccessibleMessage.from_dict(data.get('pinned_message')),
            invoice=Invoice.from_dict(data.get('invoice')),
            successful_payment=SuccessfulPayment.from_dict(data.get('successful_payment')),
            refunded_payment=RefundedPayment.from_dict(data.get('refunded_payment')),
            users_shared=UsersShared.from_dict(data.get('users_shared')),
            chat_shared=ChatShared.from_dict(data.get('chat_shared')),
            gift=GiftInfo.from_dict(data.get('gift')),
            unique_gift=UniqueGiftInfo.from_dict(data.get('unique_gift')),
            gift_upgrade_sent=GiftInfo.from_dict(data.get('gift_upgrade_sent')),
            connected_website=data.get('connected_website'),
            write_access_allowed=WriteAccessAllowed.from_dict(data.get('write_access_allowed')),
            passport_data=PassportData.from_dict(data.get('passport_data')),
            proximity_alert_triggered=ProximityAlertTriggered.from_dict(data.get('proximity_alert_triggered')),
            boost_added=ChatBoostAdded.from_dict(data.get('boost_added')),
            chat_background_set=ChatBackground.from_dict(data.get('chat_background_set')),
            checklist_tasks_done=ChecklistTasksDone.from_dict(data.get('checklist_tasks_done')),
            checklist_tasks_added=ChecklistTasksAdded.from_dict(data.get('checklist_tasks_added')),
            community_chat_added=CommunityChatAdded.from_dict(data.get('community_chat_added')),
            community_chat_joined=CommunityChatJoined.from_dict(data.get('community_chat_joined')),
            community_chat_removed=CommunityChatRemoved.from_dict(data.get('community_chat_removed')),
            direct_message_price_changed=DirectMessagePriceChanged.from_dict(data.get('direct_message_price_changed')),
            forum_topic_created=ForumTopicCreated.from_dict(data.get('forum_topic_created')),
            forum_topic_edited=ForumTopicEdited.from_dict(data.get('forum_topic_edited')),
            forum_topic_closed=ForumTopicClosed.from_dict(data.get('forum_topic_closed')),
            forum_topic_reopened=ForumTopicReopened.from_dict(data.get('forum_topic_reopened')),
            general_forum_topic_hidden=GeneralForumTopicHidden.from_dict(data.get('general_forum_topic_hidden')),
            general_forum_topic_unhidden=GeneralForumTopicUnhidden.from_dict(data.get('general_forum_topic_unhidden')),
            giveaway_created=GiveawayCreated.from_dict(data.get('giveaway_created')),
            giveaway=Giveaway.from_dict(data.get('giveaway')),
            giveaway_winners=GiveawayWinners.from_dict(data.get('giveaway_winners')),
            giveaway_completed=GiveawayCompleted.from_dict(data.get('giveaway_completed')),
            managed_bot_created=ManagedBotCreated.from_dict(data.get('managed_bot_created')),
            paid_message_price_changed=PaidMessagePriceChanged.from_dict(data.get('paid_message_price_changed')),
            poll_option_added=PollOptionAdded.from_dict(data.get('poll_option_added')),
            poll_option_deleted=PollOptionDeleted.from_dict(data.get('poll_option_deleted')),
            suggested_post_approved=SuggestedPostApproved.from_dict(data.get('suggested_post_approved')),
            suggested_post_approval_failed=SuggestedPostApprovalFailed.from_dict(data.get('suggested_post_approval_failed')),
            suggested_post_declined=SuggestedPostDeclined.from_dict(data.get('suggested_post_declined')),
            suggested_post_paid=SuggestedPostPaid.from_dict(data.get('suggested_post_paid')),
            suggested_post_refunded=SuggestedPostRefunded.from_dict(data.get('suggested_post_refunded')),
            video_chat_scheduled=VideoChatScheduled.from_dict(data.get('video_chat_scheduled')),
            video_chat_started=VideoChatStarted.from_dict(data.get('video_chat_started')),
            video_chat_ended=VideoChatEnded.from_dict(data.get('video_chat_ended')),
            video_chat_participants_invited=VideoChatParticipantsInvited.from_dict(data.get('video_chat_participants_invited')),
            web_app_data=WebAppData.from_dict(data.get('web_app_data')),
            reply_markup=InlineKeyboardMarkup.from_dict(data.get('reply_markup')),
        )