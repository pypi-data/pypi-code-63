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


class InputPrivacyValueAllowUsers(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.InputPrivacyRule`.

    Details:
        - Layer: ``117``
        - ID: ``0x131cc67f``

    Parameters:
        users: List of :obj:`InputUser <pyrogram.raw.base.InputUser>`
    """

    __slots__: List[str] = ["users"]

    ID = 0x131cc67f
    QUALNAME = "types.InputPrivacyValueAllowUsers"

    def __init__(self, *, users: List["raw.base.InputUser"]) -> None:
        self.users = users  # Vector<InputUser>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputPrivacyValueAllowUsers":
        # No flags
        
        users = TLObject.read(data)
        
        return InputPrivacyValueAllowUsers(users=users)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(Vector(self.users))
        
        return data.getvalue()
