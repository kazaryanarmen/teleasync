from .objects.update import Update
import asyncio
import inspect

class EventRouter:
    def __init__(self):
        self.message_handlers = []
        self.command_handlers = {}
        self.edited_message_handlers = []
        self.channel_post_handlers = []
        self.edited_channel_post_handlers = []
        self.business_connection_handlers = []
        self.business_message_handlers = []
        self.edited_business_message_handlers = []
        self.deleted_business_messages_handlers = []
        self.guest_message_handlers = []
        self.message_reaction_handlers = []
        self.message_reaction_count_handlers = []
        self.inline_query_handlers = []
        self.chosen_inline_result_handlers = []
        self.callback_query_handlers = []
        self.shipping_query_handlers = []
        self.pre_checkout_query_handlers = []
        self.successful_payment_handlers = []
        self.purchased_paid_media_handlers = []
        self.poll_handlers = []
        self.poll_answer_handlers = []
        self.my_chat_member_handlers = []
        self.chat_member_handlers = []
        self.chat_join_request_handlers = []
        self.chat_boost_handlers = []
        self.removed_chat_boost_handlers = []
        self.managed_bot_handlers = []
        self.subscription_handlers = []
        self.stopped_message_generation_handlers = []

    def message(self):
        def decorator(func):
            self.message_handlers.append(func)
            return func
        return decorator

    def command(self, commands: str | list[str]):
        if isinstance(commands, str):
            commands = [commands]
        def decorator(func):
            for cmd in commands:
                cmd = cmd.lstrip('/').lower()
                if cmd not in self.command_handlers:
                    self.command_handlers[cmd] = []
                self.command_handlers[cmd].append(func)
            return func
        return decorator

    def edited_message(self):
        def decorator(func):
            self.edited_message_handlers.append(func)
            return func
        return decorator

    def channel_post(self):
        def decorator(func):
            self.channel_post_handlers.append(func)
            return func
        return decorator

    def edited_channel_post(self):
        def decorator(func):
            self.edited_channel_post_handlers.append(func)
            return func
        return decorator

    def business_connection(self):
        def decorator(func):
            self.business_connection_handlers.append(func)
            return func
        return decorator

    def business_message(self):
        def decorator(func):
            self.business_message_handlers.append(func)
            return func
        return decorator

    def edited_business_message(self):
        def decorator(func):
            self.edited_business_message_handlers.append(func)
            return func
        return decorator

    def deleted_business_messages(self):
        def decorator(func):
            self.deleted_business_messages_handlers.append(func)
            return func
        return decorator

    def guest_message(self):
        def decorator(func):
            self.guest_message_handlers.append(func)
            return func
        return decorator

    def message_reaction(self):
        def decorator(func):
            self.message_reaction_handlers.append(func)
            return func
        return decorator

    def message_reaction_count(self):
        def decorator(func):
            self.message_reaction_count_handlers.append(func)
            return func
        return decorator

    def inline_query(self):
        def decorator(func):
            self.inline_query_handlers.append(func)
            return func
        return decorator

    def chosen_inline_result(self):
        def decorator(func):
            self.chosen_inline_result_handlers.append(func)
            return func
        return decorator

    def callback_query(self):
        def decorator(func):
            self.callback_query_handlers.append(func)
            return func
        return decorator

    def shipping_query(self):
        def decorator(func):
            self.shipping_query_handlers.append(func)
            return func
        return decorator

    def pre_checkout_query(self):
        def decorator(func):
            self.pre_checkout_query_handlers.append(func)
            return func
        return decorator

    def successful_payment(self):
        def decorator(func):
            self.successful_payment_handlers.append(func)
            return func
        return decorator

    def purchased_paid_media(self):
        def decorator(func):
            self.purchased_paid_media_handlers.append(func)
            return func
        return decorator

    def poll(self):
        def decorator(func):
            self.poll_handlers.append(func)
            return func
        return decorator

    def poll_answer(self):
        def decorator(func):
            self.poll_answer_handlers.append(func)
            return func
        return decorator

    def my_chat_member(self):
        def decorator(func):
            self.my_chat_member_handlers.append(func)
            return func
        return decorator

    def chat_member(self):
        def decorator(func):
            self.chat_member_handlers.append(func)
            return func
        return decorator

    def chat_join_request(self):
        def decorator(func):
            self.chat_join_request_handlers.append(func)
            return func
        return decorator

    def chat_boost(self):
        def decorator(func):
            self.chat_boost_handlers.append(func)
            return func
        return decorator

    def removed_chat_boost(self):
        def decorator(func):
            self.removed_chat_boost_handlers.append(func)
            return func
        return decorator

    def managed_bot(self):
        def decorator(func):
            self.managed_bot_handlers.append(func)
            return func
        return decorator

    def subscription(self):
        def decorator(func):
            self.subscription_handlers.append(func)
            return func
        return decorator

    def stopped_message_generation(self):
        def decorator(func):
            self.stopped_message_generation_handlers.append(func)
            return func
        return decorator

    async def _execute_handler(self, handler, *args, **kwargs):
        if inspect.iscoroutinefunction(handler):
            return await handler(*args, **kwargs)
        else:
            return handler(*args, **kwargs)

    async def feed(self, update_data: dict | str | list) -> None:
        if isinstance(update_data, list):
            for item in update_data:
                await self.feed(item)
            return

        if isinstance(update_data, str):
            import json
            update_data = json.loads(update_data)
            
        update = Update.from_dict(update_data)
        if not update:
            return

        if update.message:
            message_text = update.message.text or update.message.caption or ""
            if message_text.startswith('/'):
                parts = message_text.split(maxsplit=1)
                cmd_name = parts[0][1:].lower()
                if '@' in cmd_name:
                    cmd_name = cmd_name.split('@')[0]
                if cmd_name in self.command_handlers:
                    for handler in self.command_handlers[cmd_name]:
                        await self._execute_handler(handler, update.message)
            
            for handler in self.message_handlers:
                await self._execute_handler(handler, update.message)
                
        if update.edited_message:
            for handler in self.edited_message_handlers:
                await self._execute_handler(handler, update.edited_message)
        if update.channel_post:
            for handler in self.channel_post_handlers:
                await self._execute_handler(handler, update.channel_post)
        if update.edited_channel_post:
            for handler in self.edited_channel_post_handlers:
                await self._execute_handler(handler, update.edited_channel_post)
        if update.business_connection:
            for handler in self.business_connection_handlers:
                await self._execute_handler(handler, update.business_connection)
        if update.business_message:
            for handler in self.business_message_handlers:
                await self._execute_handler(handler, update.business_message)
        if update.edited_business_message:
            for handler in self.edited_business_message_handlers:
                await self._execute_handler(handler, update.edited_business_message)
        if update.deleted_business_messages:
            for handler in self.deleted_business_messages_handlers:
                await self._execute_handler(handler, update.deleted_business_messages)
        if update.guest_message:
            for handler in self.guest_message_handlers:
                await self._execute_handler(handler, update.guest_message)
        if update.message_reaction:
            for handler in self.message_reaction_handlers:
                await self._execute_handler(handler, update.message_reaction)
        if update.message_reaction_count:
            for handler in self.message_reaction_count_handlers:
                await self._execute_handler(handler, update.message_reaction_count)
        if update.inline_query:
            for handler in self.inline_query_handlers:
                await self._execute_handler(handler, update.inline_query)
        if update.chosen_inline_result:
            for handler in self.chosen_inline_result_handlers:
                await self._execute_handler(handler, update.chosen_inline_result)
        if update.callback_query:
            for handler in self.callback_query_handlers:
                await self._execute_handler(handler, update.callback_query)
        if update.shipping_query:
            for handler in self.shipping_query_handlers:
                await self._execute_handler(handler, update.shipping_query)
        if update.pre_checkout_query:
            for handler in self.pre_checkout_query_handlers:
                await self._execute_handler(handler, update.pre_checkout_query)
        if update.message.successful_payment:
            for handler in self.successful_payment_handlers:
                await self._execute_handler(handler, update.successful_payment)
        if update.purchased_paid_media:
            for handler in self.purchased_paid_media_handlers:
                await self._execute_handler(handler, update.purchased_paid_media)
        if update.poll:
            for handler in self.poll_handlers:
                await self._execute_handler(handler, update.poll)
        if update.poll_answer:
            for handler in self.poll_answer_handlers:
                await self._execute_handler(handler, update.poll_answer)
        if update.my_chat_member:
            for handler in self.my_chat_member_handlers:
                await self._execute_handler(handler, update.my_chat_member)
        if update.chat_member:
            for handler in self.chat_member_handlers:
                await self._execute_handler(handler, update.chat_member)
        if update.chat_join_request:
            for handler in self.chat_join_request_handlers:
                await self._execute_handler(handler, update.chat_join_request)
        if update.chat_boost:
            for handler in self.chat_boost_handlers:
                await self._execute_handler(handler, update.chat_boost)
        if update.removed_chat_boost:
            for handler in self.removed_chat_boost_handlers:
                await self._execute_handler(handler, update.removed_chat_boost)
        if update.managed_bot:
            for handler in self.managed_bot_handlers:
                await self._execute_handler(handler, update.managed_bot)
        if update.subscription:
            for handler in self.subscription_handlers:
                await self._execute_handler(handler, update.subscription)
        if update.stopped_message_generation:
            for handler in self.stopped_message_generation_handlers:
                await self._execute_handler(handler, update.stopped_message_generation)