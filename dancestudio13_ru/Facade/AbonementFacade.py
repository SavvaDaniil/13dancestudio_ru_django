from dancestudio13_ru.Repository.AbonementRepository import AbonementRepository
from dancestudio13_ru.ViewModel.Abonement.AbonementLiteViewModel import AbonementLiteViewModel
from typing import List

class AbonementFacade:
    def listAllLiteActive(self) -> List[AbonementLiteViewModel]:
        abonementRepository = AbonementRepository()
        abonements = abonementRepository.listAllActive()
        abonmenetLiteViewModel = []

        for abonement in abonements:
            abonmenetLiteViewModel.append(
                AbonementLiteViewModel(
                    id=abonement.id,
                    name = abonement.name,
                    price= abonement.price
                )
            )

        return abonmenetLiteViewModel