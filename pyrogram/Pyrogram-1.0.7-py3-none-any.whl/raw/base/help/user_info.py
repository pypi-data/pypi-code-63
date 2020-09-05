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

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

UserInfo = Union[raw.types.help.UserInfo, raw.types.help.UserInfoEmpty]


# noinspection PyRedeclaration
class UserInfo:  # type: ignore
    """This base type has 2 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`help.UserInfo <pyrogram.raw.types.help.UserInfo>`
            - :obj:`help.UserInfoEmpty <pyrogram.raw.types.help.UserInfoEmpty>`

    See Also:
        This object can be returned by 2 methods:

        .. hlist::
            :columns: 2

            - :obj:`help.GetUserInfo <pyrogram.raw.functions.help.GetUserInfo>`
            - :obj:`help.EditUserInfo <pyrogram.raw.functions.help.EditUserInfo>`
    """

    QUALNAME = "pyrogram.raw.base.help.UserInfo"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/user-info")
