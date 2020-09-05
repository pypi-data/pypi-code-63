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


class ChannelAdminLogEvent(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.ChannelAdminLogEvent`.

    Details:
        - Layer: ``117``
        - ID: ``0x3b5a3e40``

    Parameters:
        id: ``int`` ``64-bit``
        date: ``int`` ``32-bit``
        user_id: ``int`` ``32-bit``
        action: :obj:`ChannelAdminLogEventAction <pyrogram.raw.base.ChannelAdminLogEventAction>`
    """

    __slots__: List[str] = ["id", "date", "user_id", "action"]

    ID = 0x3b5a3e40
    QUALNAME = "types.ChannelAdminLogEvent"

    def __init__(self, *, id: int, date: int, user_id: int, action: "raw.base.ChannelAdminLogEventAction") -> None:
        self.id = id  # long
        self.date = date  # int
        self.user_id = user_id  # int
        self.action = action  # ChannelAdminLogEventAction

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ChannelAdminLogEvent":
        # No flags
        
        id = Long.read(data)
        
        date = Int.read(data)
        
        user_id = Int.read(data)
        
        action = TLObject.read(data)
        
        return ChannelAdminLogEvent(id=id, date=date, user_id=user_id, action=action)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(Long(self.id))
        
        data.write(Int(self.date))
        
        data.write(Int(self.user_id))
        
        data.write(self.action.write())
        
        return data.getvalue()
