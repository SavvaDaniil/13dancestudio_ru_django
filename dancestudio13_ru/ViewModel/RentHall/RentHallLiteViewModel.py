


from dataclasses import dataclass


@dataclass
class RentHallLiteViewModel:
    id: int
    name: str
    count_of_images: int
    posterSrc0: str
    posterSrc1: str
    posterSrc2: str