from uuid import UUID

from injector import singleton, inject
from typing import Optional

from translator_api.entities import RefCodesDTO


@singleton
class ReflectionInMemoryService(object):

    """
    SELECT r.reflection_id, native_lang.code, foreign_lang.code
    FROM reflection r
    JOIN languages native_lang ON r.native_language_id = native_lang.language_id
    JOIN languages foreign_lang ON r.foreign_language_id = foreign_lang.language_id
    ORDER BY native_lang.code, foreign_lang.code;
    """

    REFLECTIONS = {
        UUID('c83f0d81-2a71-41ca-a9e1-922d68e46165'): RefCodesDTO.new(native_code='de', foreign_code='en'),
        UUID('99d8dff3-d376-413a-9a1b-27260658af37'): RefCodesDTO.new(native_code='de', foreign_code='es'),
        UUID('cc21ec00-4b88-4acf-8a4c-daac9f121a61'): RefCodesDTO.new(native_code='de', foreign_code='fr'),
        UUID('9c1cdb35-3cd8-45c8-9497-2b6227689439'): RefCodesDTO.new(native_code='de', foreign_code='it'),
        UUID('dcd7df63-c046-4f81-9524-bfb5f8eee447'): RefCodesDTO.new(native_code='de', foreign_code='ru'),
        UUID('df8ac92a-30ef-45d0-bf1d-ee407cc59157'): RefCodesDTO.new(native_code='en', foreign_code='de'),
        UUID('816fa369-f23a-4453-a53b-defebb72384c'): RefCodesDTO.new(native_code='en', foreign_code='es'),
        UUID('3ed47dbf-9564-48aa-a754-b9abec6d16e7'): RefCodesDTO.new(native_code='en', foreign_code='fr'),
        UUID('27c66154-5959-4cc3-b776-358a18ebbd11'): RefCodesDTO.new(native_code='en', foreign_code='it'),
        UUID('bdf7921b-3b5d-4646-943e-43f88c71b394'): RefCodesDTO.new(native_code='en', foreign_code='ru'),
        UUID('ac71b0d8-b1f3-461d-9a2e-804b53767bf1'): RefCodesDTO.new(native_code='es', foreign_code='de'),
        UUID('8542ff22-026f-45be-8be8-9c7296912fd6'): RefCodesDTO.new(native_code='es', foreign_code='en'),
        UUID('5a3828df-af35-412f-b727-40d65fdf8239'): RefCodesDTO.new(native_code='es', foreign_code='fr'),
        UUID('7d8cf9e6-5d5e-400a-a5aa-dc02d90d838d'): RefCodesDTO.new(native_code='es', foreign_code='it'),
        UUID('6aeacf06-97f4-4a10-88ef-7c75f95ca696'): RefCodesDTO.new(native_code='es', foreign_code='ru'),
        UUID('2291d411-9773-4677-8c97-eafd4514d3cd'): RefCodesDTO.new(native_code='fr', foreign_code='de'),
        UUID('e013acce-8a87-4a05-bedc-7ede4490aaf5'): RefCodesDTO.new(native_code='fr', foreign_code='en'),
        UUID('e8aea3f6-f2a7-421e-9950-221238054d05'): RefCodesDTO.new(native_code='fr', foreign_code='es'),
        UUID('dff1d268-b098-461f-981c-9f283570f24e'): RefCodesDTO.new(native_code='fr', foreign_code='it'),
        UUID('d85c1843-0608-40bb-8d68-df52afa20e92'): RefCodesDTO.new(native_code='fr', foreign_code='ru'),
        UUID('3bd7ccca-0f1e-42de-8dde-45014bafa392'): RefCodesDTO.new(native_code='it', foreign_code='de'),
        UUID('d60f04e1-2490-463f-9b2e-6a10c221b4d8'): RefCodesDTO.new(native_code='it', foreign_code='en'),
        UUID('dcebadfb-e181-48a6-8365-ce8e13ae72c0'): RefCodesDTO.new(native_code='it', foreign_code='es'),
        UUID('c5855d1c-af0f-408b-98d9-463b4d85561f'): RefCodesDTO.new(native_code='it', foreign_code='fr'),
        UUID('c19375c7-60c4-4b94-abe3-60bc51bd93e2'): RefCodesDTO.new(native_code='it', foreign_code='ru'),
        UUID('57b514dc-92b7-4657-ab14-e3f5418e2509'): RefCodesDTO.new(native_code='ru', foreign_code='de'),
        UUID('01838288-daec-45fb-831c-89a25502ec6a'): RefCodesDTO.new(native_code='ru', foreign_code='en'),
        UUID('ecc570fb-2776-48d7-8068-0c36c53933b7'): RefCodesDTO.new(native_code='ru', foreign_code='es'),
        UUID('6b98e622-4764-4c16-815a-68d34c2d832e'): RefCodesDTO.new(native_code='ru', foreign_code='fr'),
        UUID('54f3ff5b-a457-4295-ab99-4352547fa14f'): RefCodesDTO.new(native_code='ru', foreign_code='it')
    }

    @inject
    def __init__(self) -> None:
        pass

    async def get_codes_for_reflection(self, reflection_id: UUID) -> Optional[RefCodesDTO]:
        return self.REFLECTIONS.get(reflection_id)
