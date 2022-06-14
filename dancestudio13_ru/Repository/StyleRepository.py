from dancestudio13_ru.models import Style
from typing import List


class StyleRepository:

    def findById(self, id_of_style: int) -> Style:
        style = Style.objects.get(id = id_of_style)
        return style

    def findByLinkShort(self, link_short: str) -> Style:
        style = Style.objects.get(link_short = link_short)
        return style

    def listAllActive(self) -> List[Style]:
        styles = Style.objects.filter(active=1).order_by("-order_number")
        return styles