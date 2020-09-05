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


class DiscardCall(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``117``
        - ID: ``0xb2cbc1c0``

    Parameters:
        peer: :obj:`InputPhoneCall <pyrogram.raw.base.InputPhoneCall>`
        duration: ``int`` ``32-bit``
        reason: :obj:`PhoneCallDiscardReason <pyrogram.raw.base.PhoneCallDiscardReason>`
        connection_id: ``int`` ``64-bit``
        video (optional): ``bool``

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "duration", "reason", "connection_id", "video"]

    ID = 0xb2cbc1c0
    QUALNAME = "functions.phone.DiscardCall"

    def __init__(self, *, peer: "raw.base.InputPhoneCall", duration: int, reason: "raw.base.PhoneCallDiscardReason", connection_id: int, video: Union[None, bool] = None) -> None:
        self.peer = peer  # InputPhoneCall
        self.duration = duration  # int
        self.reason = reason  # PhoneCallDiscardReason
        self.connection_id = connection_id  # long
        self.video = video  # flags.0?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "DiscardCall":
        flags = Int.read(data)
        
        video = True if flags & (1 << 0) else False
        peer = TLObject.read(data)
        
        duration = Int.read(data)
        
        reason = TLObject.read(data)
        
        connection_id = Long.read(data)
        
        return DiscardCall(peer=peer, duration=duration, reason=reason, connection_id=connection_id, video=video)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.video is not None else 0
        data.write(Int(flags))
        
        data.write(self.peer.write())
        
        data.write(Int(self.duration))
        
        data.write(self.reason.write())
        
        data.write(Long(self.connection_id))
        
        return data.getvalue()
