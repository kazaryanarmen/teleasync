class TelegramAPIError(Exception):
    """Base exception for Telegram Bot API errors."""
    def __init__(self, message: str, error_code: int | None = None):
        super().__init__(message)
        self.error_code = error_code

class TelegramNetworkError(TelegramAPIError):
    """Network errors or timeouts during API requests."""
    pass

class TelegramBadRequestError(TelegramAPIError):
    """Error 400: Bad request or parameters."""
    pass

class TelegramUnauthorizedError(TelegramAPIError):
    """Error 401: Invalid bot token."""
    pass