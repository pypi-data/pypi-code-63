#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2020 Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Union, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class GetWebPage(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``117``
        - ID: ``0x32ca8f91``

    Parameters:
        url: ``str``
        hash: ``int`` ``32-bit``

    Returns:
        :obj:`WebPage <pyrogram.raw.base.WebPage>`
    """

    __slots__: List[str] = ["url", "hash"]

    ID = 0x32ca8f91
    QUALNAME = "functions.messages.GetWebPage"

    def __init__(self, *, url: str, hash: int) -> None:
        self.url = url  # string
        self.hash = hash  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GetWebPage":
        # No flags
        
        url = String.read(data)
        
        hash = Int.read(data)
        
        return GetWebPage(url=url, hash=hash)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(String(self.url))
        
        data.write(Int(self.hash))
        
        return data.getvalue()
