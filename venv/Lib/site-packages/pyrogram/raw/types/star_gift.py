#  Pyrofork - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#  Copyright (C) 2022-present Mayuri-Chan <https://github.com/Mayuri-Chan>
#
#  This file is part of Pyrofork.
#
#  Pyrofork is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrofork is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrofork.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class StarGift(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarGift`.

    Details:
        - Layer: ``207``
        - ID: ``7F853C12``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        sticker (:obj:`Document <pyrogram.raw.base.Document>`):
            N/A

        stars (``int`` ``64-bit``):
            N/A

        convert_stars (``int`` ``64-bit``):
            N/A

        limited (``bool``, *optional*):
            N/A

        sold_out (``bool``, *optional*):
            N/A

        birthday (``bool``, *optional*):
            N/A

        availability_remains (``int`` ``32-bit``, *optional*):
            N/A

        availability_total (``int`` ``32-bit``, *optional*):
            N/A

        availability_resale (``int`` ``64-bit``, *optional*):
            N/A

        first_sale_date (``int`` ``32-bit``, *optional*):
            N/A

        last_sale_date (``int`` ``32-bit``, *optional*):
            N/A

        upgrade_stars (``int`` ``64-bit``, *optional*):
            N/A

        resell_min_stars (``int`` ``64-bit``, *optional*):
            N/A

        title (``str``, *optional*):
            N/A

        released_by (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "sticker", "stars", "convert_stars", "limited", "sold_out", "birthday", "availability_remains", "availability_total", "availability_resale", "first_sale_date", "last_sale_date", "upgrade_stars", "resell_min_stars", "title", "released_by"]

    ID = 0x7f853c12
    QUALNAME = "types.StarGift"

    def __init__(self, *, id: int, sticker: "raw.base.Document", stars: int, convert_stars: int, limited: Optional[bool] = None, sold_out: Optional[bool] = None, birthday: Optional[bool] = None, availability_remains: Optional[int] = None, availability_total: Optional[int] = None, availability_resale: Optional[int] = None, first_sale_date: Optional[int] = None, last_sale_date: Optional[int] = None, upgrade_stars: Optional[int] = None, resell_min_stars: Optional[int] = None, title: Optional[str] = None, released_by: "raw.base.Peer" = None) -> None:
        self.id = id  # long
        self.sticker = sticker  # Document
        self.stars = stars  # long
        self.convert_stars = convert_stars  # long
        self.limited = limited  # flags.0?true
        self.sold_out = sold_out  # flags.1?true
        self.birthday = birthday  # flags.2?true
        self.availability_remains = availability_remains  # flags.0?int
        self.availability_total = availability_total  # flags.0?int
        self.availability_resale = availability_resale  # flags.4?long
        self.first_sale_date = first_sale_date  # flags.1?int
        self.last_sale_date = last_sale_date  # flags.1?int
        self.upgrade_stars = upgrade_stars  # flags.3?long
        self.resell_min_stars = resell_min_stars  # flags.4?long
        self.title = title  # flags.5?string
        self.released_by = released_by  # flags.6?Peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGift":
        
        flags = Int.read(b)
        
        limited = True if flags & (1 << 0) else False
        sold_out = True if flags & (1 << 1) else False
        birthday = True if flags & (1 << 2) else False
        id = Long.read(b)
        
        sticker = TLObject.read(b)
        
        stars = Long.read(b)
        
        availability_remains = Int.read(b) if flags & (1 << 0) else None
        availability_total = Int.read(b) if flags & (1 << 0) else None
        availability_resale = Long.read(b) if flags & (1 << 4) else None
        convert_stars = Long.read(b)
        
        first_sale_date = Int.read(b) if flags & (1 << 1) else None
        last_sale_date = Int.read(b) if flags & (1 << 1) else None
        upgrade_stars = Long.read(b) if flags & (1 << 3) else None
        resell_min_stars = Long.read(b) if flags & (1 << 4) else None
        title = String.read(b) if flags & (1 << 5) else None
        released_by = TLObject.read(b) if flags & (1 << 6) else None
        
        return StarGift(id=id, sticker=sticker, stars=stars, convert_stars=convert_stars, limited=limited, sold_out=sold_out, birthday=birthday, availability_remains=availability_remains, availability_total=availability_total, availability_resale=availability_resale, first_sale_date=first_sale_date, last_sale_date=last_sale_date, upgrade_stars=upgrade_stars, resell_min_stars=resell_min_stars, title=title, released_by=released_by)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.limited else 0
        flags |= (1 << 1) if self.sold_out else 0
        flags |= (1 << 2) if self.birthday else 0
        flags |= (1 << 0) if self.availability_remains is not None else 0
        flags |= (1 << 0) if self.availability_total is not None else 0
        flags |= (1 << 4) if self.availability_resale is not None else 0
        flags |= (1 << 1) if self.first_sale_date is not None else 0
        flags |= (1 << 1) if self.last_sale_date is not None else 0
        flags |= (1 << 3) if self.upgrade_stars is not None else 0
        flags |= (1 << 4) if self.resell_min_stars is not None else 0
        flags |= (1 << 5) if self.title is not None else 0
        flags |= (1 << 6) if self.released_by is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(self.sticker.write())
        
        b.write(Long(self.stars))
        
        if self.availability_remains is not None:
            b.write(Int(self.availability_remains))
        
        if self.availability_total is not None:
            b.write(Int(self.availability_total))
        
        if self.availability_resale is not None:
            b.write(Long(self.availability_resale))
        
        b.write(Long(self.convert_stars))
        
        if self.first_sale_date is not None:
            b.write(Int(self.first_sale_date))
        
        if self.last_sale_date is not None:
            b.write(Int(self.last_sale_date))
        
        if self.upgrade_stars is not None:
            b.write(Long(self.upgrade_stars))
        
        if self.resell_min_stars is not None:
            b.write(Long(self.resell_min_stars))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.released_by is not None:
            b.write(self.released_by.write())
        
        return b.getvalue()
