# 0.2.0

### Changed (Breaking Changes)
* Object fields `photo_`, `video_`, `document_`, `audio_`, `sticker_`, `animation_`, `voice_` have been renamed to `photo`, `video`, etc.
* Closing the HTTP client: `aclose()` method. The `close()` method is now strictly for the Telegram API.
* Router handlers are now stored in `router._handlers` instead of `router.<event>_handlers`.
* Synchronous handlers are now executed in a separate thread.

### Fixed
* `successful_payment` and post-event processing in the router.
* Parsing of nested lists (`InlineKeyboardMarkup`, `ReplyKeyboardMarkup`).
* `CallbackQuery.message` is now `Message`/`InaccessibleMessage`.
* Passing `file_id`/URL in `send_photo` and other methods.
* An error in a single update or handler no longer stops the bot.
* The bot token is now masked/hidden in `httpx` logs.

### Added
* `InputFile` for uploading local files, and `attach://` support for media groups.
* Router filters (`content_types`, `text`, `regex`, `chat_types`, etc.).
* `concurrency` parameter in `start_polling_from` (defaults to 1).
* Parsing of union types (`ChatMember`, `MessageOrigin`, `ReactionType`, etc.).