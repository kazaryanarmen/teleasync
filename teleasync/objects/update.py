from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .bot_subscription_updated import BotSubscriptionUpdated
    
    from .business_connection import BusinessConnection
    
    from .business_messages_deleted import BusinessMessagesDeleted
    
    from .callback_query import CallbackQuery
    
    from .chat_boost_removed import ChatBoostRemoved
    
    from .chat_boost_updated import ChatBoostUpdated
    
    from .chat_join_request import ChatJoinRequest
    
    from .chat_member_updated import ChatMemberUpdated
    
    from .chosen_inline_result import ChosenInlineResult
    
    from .inline_query import InlineQuery
    
    from .managed_bot_updated import ManagedBotUpdated
    
    from .message import Message
    
    from .message_generation_stopped import MessageGenerationStopped
    
    from .message_reaction_count_updated import MessageReactionCountUpdated
    
    from .message_reaction_updated import MessageReactionUpdated
    
    from .paid_media_purchased import PaidMediaPurchased
    
    from .poll import Poll
    
    from .poll_answer import PollAnswer
    
    from .pre_checkout_query import PreCheckoutQuery
    
    from .shipping_query import ShippingQuery
    


class Update:
    """This object represents an incoming update. At most one of the optional fields can be present in any given update."""

    def __init__(self, update_id: int, message: Message | None = None, edited_message: Message | None = None, channel_post: Message | None = None, edited_channel_post: Message | None = None, business_connection: BusinessConnection | None = None, business_message: Message | None = None, edited_business_message: Message | None = None, deleted_business_messages: BusinessMessagesDeleted | None = None, guest_message: Message | None = None, message_reaction: MessageReactionUpdated | None = None, message_reaction_count: MessageReactionCountUpdated | None = None, inline_query: InlineQuery | None = None, chosen_inline_result: ChosenInlineResult | None = None, callback_query: CallbackQuery | None = None, shipping_query: ShippingQuery | None = None, pre_checkout_query: PreCheckoutQuery | None = None, purchased_paid_media: PaidMediaPurchased | None = None, poll: Poll | None = None, poll_answer: PollAnswer | None = None, my_chat_member: ChatMemberUpdated | None = None, chat_member: ChatMemberUpdated | None = None, chat_join_request: ChatJoinRequest | None = None, chat_boost: ChatBoostUpdated | None = None, removed_chat_boost: ChatBoostRemoved | None = None, managed_bot: ManagedBotUpdated | None = None, subscription: BotSubscriptionUpdated | None = None, stopped_message_generation: MessageGenerationStopped | None = None):
        self.update_id: int = update_id
        self.message: Message | None = message
        self.edited_message: Message | None = edited_message
        self.channel_post: Message | None = channel_post
        self.edited_channel_post: Message | None = edited_channel_post
        self.business_connection: BusinessConnection | None = business_connection
        self.business_message: Message | None = business_message
        self.edited_business_message: Message | None = edited_business_message
        self.deleted_business_messages: BusinessMessagesDeleted | None = deleted_business_messages
        self.guest_message: Message | None = guest_message
        self.message_reaction: MessageReactionUpdated | None = message_reaction
        self.message_reaction_count: MessageReactionCountUpdated | None = message_reaction_count
        self.inline_query: InlineQuery | None = inline_query
        self.chosen_inline_result: ChosenInlineResult | None = chosen_inline_result
        self.callback_query: CallbackQuery | None = callback_query
        self.shipping_query: ShippingQuery | None = shipping_query
        self.pre_checkout_query: PreCheckoutQuery | None = pre_checkout_query
        self.purchased_paid_media: PaidMediaPurchased | None = purchased_paid_media
        self.poll: Poll | None = poll
        self.poll_answer: PollAnswer | None = poll_answer
        self.my_chat_member: ChatMemberUpdated | None = my_chat_member
        self.chat_member: ChatMemberUpdated | None = chat_member
        self.chat_join_request: ChatJoinRequest | None = chat_join_request
        self.chat_boost: ChatBoostUpdated | None = chat_boost
        self.removed_chat_boost: ChatBoostRemoved | None = removed_chat_boost
        self.managed_bot: ManagedBotUpdated | None = managed_bot
        self.subscription: BotSubscriptionUpdated | None = subscription
        self.stopped_message_generation: MessageGenerationStopped | None = stopped_message_generation

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
        if self.update_id is not None:
            result['update_id'] = _serialize(self.update_id)
        if self.message is not None:
            result['message'] = _serialize(self.message)
        if self.edited_message is not None:
            result['edited_message'] = _serialize(self.edited_message)
        if self.channel_post is not None:
            result['channel_post'] = _serialize(self.channel_post)
        if self.edited_channel_post is not None:
            result['edited_channel_post'] = _serialize(self.edited_channel_post)
        if self.business_connection is not None:
            result['business_connection'] = _serialize(self.business_connection)
        if self.business_message is not None:
            result['business_message'] = _serialize(self.business_message)
        if self.edited_business_message is not None:
            result['edited_business_message'] = _serialize(self.edited_business_message)
        if self.deleted_business_messages is not None:
            result['deleted_business_messages'] = _serialize(self.deleted_business_messages)
        if self.guest_message is not None:
            result['guest_message'] = _serialize(self.guest_message)
        if self.message_reaction is not None:
            result['message_reaction'] = _serialize(self.message_reaction)
        if self.message_reaction_count is not None:
            result['message_reaction_count'] = _serialize(self.message_reaction_count)
        if self.inline_query is not None:
            result['inline_query'] = _serialize(self.inline_query)
        if self.chosen_inline_result is not None:
            result['chosen_inline_result'] = _serialize(self.chosen_inline_result)
        if self.callback_query is not None:
            result['callback_query'] = _serialize(self.callback_query)
        if self.shipping_query is not None:
            result['shipping_query'] = _serialize(self.shipping_query)
        if self.pre_checkout_query is not None:
            result['pre_checkout_query'] = _serialize(self.pre_checkout_query)
        if self.purchased_paid_media is not None:
            result['purchased_paid_media'] = _serialize(self.purchased_paid_media)
        if self.poll is not None:
            result['poll'] = _serialize(self.poll)
        if self.poll_answer is not None:
            result['poll_answer'] = _serialize(self.poll_answer)
        if self.my_chat_member is not None:
            result['my_chat_member'] = _serialize(self.my_chat_member)
        if self.chat_member is not None:
            result['chat_member'] = _serialize(self.chat_member)
        if self.chat_join_request is not None:
            result['chat_join_request'] = _serialize(self.chat_join_request)
        if self.chat_boost is not None:
            result['chat_boost'] = _serialize(self.chat_boost)
        if self.removed_chat_boost is not None:
            result['removed_chat_boost'] = _serialize(self.removed_chat_boost)
        if self.managed_bot is not None:
            result['managed_bot'] = _serialize(self.managed_bot)
        if self.subscription is not None:
            result['subscription'] = _serialize(self.subscription)
        if self.stopped_message_generation is not None:
            result['stopped_message_generation'] = _serialize(self.stopped_message_generation)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'Update' | None:
        if not data:
            return None
        from .bot_subscription_updated import BotSubscriptionUpdated
        from .business_connection import BusinessConnection
        from .business_messages_deleted import BusinessMessagesDeleted
        from .callback_query import CallbackQuery
        from .chat_boost_removed import ChatBoostRemoved
        from .chat_boost_updated import ChatBoostUpdated
        from .chat_join_request import ChatJoinRequest
        from .chat_member_updated import ChatMemberUpdated
        from .chosen_inline_result import ChosenInlineResult
        from .inline_query import InlineQuery
        from .managed_bot_updated import ManagedBotUpdated
        from .message import Message
        from .message_generation_stopped import MessageGenerationStopped
        from .message_reaction_count_updated import MessageReactionCountUpdated
        from .message_reaction_updated import MessageReactionUpdated
        from .paid_media_purchased import PaidMediaPurchased
        from .poll import Poll
        from .poll_answer import PollAnswer
        from .pre_checkout_query import PreCheckoutQuery
        from .shipping_query import ShippingQuery
        return cls(
            update_id=data.get('update_id'),
            message=Message.from_dict(data.get('message')),
            edited_message=Message.from_dict(data.get('edited_message')),
            channel_post=Message.from_dict(data.get('channel_post')),
            edited_channel_post=Message.from_dict(data.get('edited_channel_post')),
            business_connection=BusinessConnection.from_dict(data.get('business_connection')),
            business_message=Message.from_dict(data.get('business_message')),
            edited_business_message=Message.from_dict(data.get('edited_business_message')),
            deleted_business_messages=BusinessMessagesDeleted.from_dict(data.get('deleted_business_messages')),
            guest_message=Message.from_dict(data.get('guest_message')),
            message_reaction=MessageReactionUpdated.from_dict(data.get('message_reaction')),
            message_reaction_count=MessageReactionCountUpdated.from_dict(data.get('message_reaction_count')),
            inline_query=InlineQuery.from_dict(data.get('inline_query')),
            chosen_inline_result=ChosenInlineResult.from_dict(data.get('chosen_inline_result')),
            callback_query=CallbackQuery.from_dict(data.get('callback_query')),
            shipping_query=ShippingQuery.from_dict(data.get('shipping_query')),
            pre_checkout_query=PreCheckoutQuery.from_dict(data.get('pre_checkout_query')),
            purchased_paid_media=PaidMediaPurchased.from_dict(data.get('purchased_paid_media')),
            poll=Poll.from_dict(data.get('poll')),
            poll_answer=PollAnswer.from_dict(data.get('poll_answer')),
            my_chat_member=ChatMemberUpdated.from_dict(data.get('my_chat_member')),
            chat_member=ChatMemberUpdated.from_dict(data.get('chat_member')),
            chat_join_request=ChatJoinRequest.from_dict(data.get('chat_join_request')),
            chat_boost=ChatBoostUpdated.from_dict(data.get('chat_boost')),
            removed_chat_boost=ChatBoostRemoved.from_dict(data.get('removed_chat_boost')),
            managed_bot=ManagedBotUpdated.from_dict(data.get('managed_bot')),
            subscription=BotSubscriptionUpdated.from_dict(data.get('subscription')),
            stopped_message_generation=MessageGenerationStopped.from_dict(data.get('stopped_message_generation')),
        )