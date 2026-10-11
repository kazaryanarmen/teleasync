from __future__ import annotations
from pathlib import Path
from typing import BinaryIO


class InputFile:
    """Файл для загрузки через multipart/form-data.

    InputFile("photo.jpg")                      # путь на диске (читается потоком)
    InputFile(b"...", filename="photo.jpg")     # байты
    InputFile(open("a.pdf", "rb"))              # файловый объект (не закрывается библиотекой)
    """

    def __init__(self, file: str | Path | bytes | BinaryIO, filename: str | None = None, content_type: str | None = None):
        self.file = file
        self.content_type = content_type
        self._handle = None

        if filename:
            self.filename = filename
        elif isinstance(file, (str, Path)):
            self.filename = Path(file).name
        else:
            name = getattr(file, "name", None)
            self.filename = Path(name).name if isinstance(name, str) else "file"

    def to_httpx(self) -> tuple:
        """Формат httpx для files=: (filename, content[, content_type])."""
        if isinstance(self.file, (str, Path)):
            self.close()
            self._handle = open(self.file, "rb")
            content = self._handle
        elif isinstance(self.file, (bytes, bytearray)):
            content = bytes(self.file)
        else:
            content = self.file

        if self.content_type:
            return (self.filename, content, self.content_type)
        return (self.filename, content)

    def close(self) -> None:
        """Закрывает только файл, открытый самой библиотекой."""
        if self._handle is not None:
            self._handle.close()
            self._handle = None

    @classmethod
    def from_dict(cls, data):
        return None