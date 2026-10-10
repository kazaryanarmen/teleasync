from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .callback_game import CallbackGame
    
    from .copy_text_button import CopyTextButton
    
    from .disabled_button import DisabledButton
    
    from .login_url import LoginUrl
    
    from .switch_inline_query_chosen_chat import SwitchInlineQueryChosenChat
    
    from .web_app_info import WebAppInfo
    


class InlineKeyboardButton:
    """This object represents one button of an inline keyboard. Exactly one of the fields other than text, icon_custom_emoji_id, and style must be used to specify the type of the button."""

    def __init__(self, text: str, icon_custom_emoji_id: str | None = None, style: str | None = None, url: str | None = None, callback_data: str | None = None, web_app: WebAppInfo | None = None, login_url: LoginUrl | None = None, switch_inline_query: str | None = None, switch_inline_query_current_chat: str | None = None, switch_inline_query_chosen_chat: SwitchInlineQueryChosenChat | None = None, copy_text: CopyTextButton | None = None, callback_game: CallbackGame | None = None, pay: bool | None = None, disabled: DisabledButton | None = None):
        self.text: str = text
        self.icon_custom_emoji_id: str | None = icon_custom_emoji_id
        self.style: str | None = style
        self.url: str | None = url
        self.callback_data: str | None = callback_data
        self.web_app: WebAppInfo | None = web_app
        self.login_url: LoginUrl | None = login_url
        self.switch_inline_query: str | None = switch_inline_query
        self.switch_inline_query_current_chat: str | None = switch_inline_query_current_chat
        self.switch_inline_query_chosen_chat: SwitchInlineQueryChosenChat | None = switch_inline_query_chosen_chat
        self.copy_text: CopyTextButton | None = copy_text
        self.callback_game: CallbackGame | None = callback_game
        self.pay: bool | None = pay
        self.disabled: DisabledButton | None = disabled

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
        if self.text is not None:
            result['text'] = _serialize(self.text)
        if self.icon_custom_emoji_id is not None:
            result['icon_custom_emoji_id'] = _serialize(self.icon_custom_emoji_id)
        if self.style is not None:
            result['style'] = _serialize(self.style)
        if self.url is not None:
            result['url'] = _serialize(self.url)
        if self.callback_data is not None:
            result['callback_data'] = _serialize(self.callback_data)
        if self.web_app is not None:
            result['web_app'] = _serialize(self.web_app)
        if self.login_url is not None:
            result['login_url'] = _serialize(self.login_url)
        if self.switch_inline_query is not None:
            result['switch_inline_query'] = _serialize(self.switch_inline_query)
        if self.switch_inline_query_current_chat is not None:
            result['switch_inline_query_current_chat'] = _serialize(self.switch_inline_query_current_chat)
        if self.switch_inline_query_chosen_chat is not None:
            result['switch_inline_query_chosen_chat'] = _serialize(self.switch_inline_query_chosen_chat)
        if self.copy_text is not None:
            result['copy_text'] = _serialize(self.copy_text)
        if self.callback_game is not None:
            result['callback_game'] = _serialize(self.callback_game)
        if self.pay is not None:
            result['pay'] = _serialize(self.pay)
        if self.disabled is not None:
            result['disabled'] = _serialize(self.disabled)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InlineKeyboardButton' | None:
        if not data:
            return None
        from .callback_game import CallbackGame
        from .copy_text_button import CopyTextButton
        from .disabled_button import DisabledButton
        from .login_url import LoginUrl
        from .switch_inline_query_chosen_chat import SwitchInlineQueryChosenChat
        from .web_app_info import WebAppInfo
        return cls(
            text=data.get('text'),
            icon_custom_emoji_id=data.get('icon_custom_emoji_id'),
            style=data.get('style'),
            url=data.get('url'),
            callback_data=data.get('callback_data'),
            web_app=WebAppInfo.from_dict(data.get('web_app')),
            login_url=LoginUrl.from_dict(data.get('login_url')),
            switch_inline_query=data.get('switch_inline_query'),
            switch_inline_query_current_chat=data.get('switch_inline_query_current_chat'),
            switch_inline_query_chosen_chat=SwitchInlineQueryChosenChat.from_dict(data.get('switch_inline_query_chosen_chat')),
            copy_text=CopyTextButton.from_dict(data.get('copy_text')),
            callback_game=CallbackGame.from_dict(data.get('callback_game')),
            pay=data.get('pay'),
            disabled=DisabledButton.from_dict(data.get('disabled')),
        )