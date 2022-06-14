from typing import List
from dancestudio13_ru.Repository.RentHallRepository import RentHallRepository
from dancestudio13_ru.ViewModel.RentHall.RentHallLiteViewModel import RentHallLiteViewModel

class RentHallFacade:

    def listAllLiteActive(self) -> List[RentHallLiteViewModel]:
        rentHallRepository = RentHallRepository()
        rentHalls = rentHallRepository.listAllActive()
        rentHallLiteViewModels = []

        for rentHall in rentHalls:
            posterSrc0 = rentHall.getPosterSrc0()
            posterSrc1 = rentHall.getPosterSrc1()
            posterSrc2 = rentHall.getPosterSrc2()
            count_of_images = 0
            if posterSrc0 is not None:
                count_of_images += 1
            if posterSrc1 is not None:
                count_of_images += 1
            if posterSrc2 is not None:
                count_of_images += 1

            rentHallLiteViewModels.append(
                RentHallLiteViewModel(
                    id=rentHall.id,
                    name=rentHall.name,
                    count_of_images=count_of_images,
                    posterSrc0=posterSrc0,
                    posterSrc1=posterSrc1,
                    posterSrc2=posterSrc2
                )
            )
        return rentHallLiteViewModels