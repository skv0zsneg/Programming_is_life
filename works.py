import enum


class ApiTypes(enum.Enum):
    """Перечисление типов API."""
    REST = (0, 'REST')
    SOAP = (1, 'SOAP')

    def __init__(self, _id, name):
        self._id = _id
        self._name = name


class ApiWrapper:
    def __init__(
            self,
            status_code=None,
            claim_id=None
    ):
        """Базовый класс для обертки API.

        :param status_code: Статус код вернувшейся заявки.
        :param claim_id: ID заявки.
        """
        self.status_code = status_code
        self.claim_id = claim_id


class RestApi(ApiWrapper):
    def __init__(self, obj):
        """Класс для работы с REST API.

        :param obj: Объект ответа REST API.
        """
        self._obj = obj
        super().__init__(
            claim_id=self.get_claims()
        )

    def get_claims(self):
        """Парсинг заявок"""
        return self._obj + '__get_claims__'


class SoapApi(ApiWrapper):
    def __init__(self, obj):
        """Парсинг от SOAP API.

        :param obj: Объект ответа SOAP API.
        """
        super().__init__(obj.lower())


def api_response(obj, api_type: ApiTypes) -> ApiWrapper:
    """Фабричный метод.

    :param obj: Объект парсинга.
    :param api_type: Тип API.
    """
    factory_dict = {
        ApiTypes.REST: RestApi,
        ApiTypes.SOAP: SoapApi
    }

    return factory_dict[api_type](obj)


if __name__ == "__main__":
    rest = api_response('TeXt', ApiTypes.REST)
    soap = api_response('TeXt', ApiTypes.SOAP)

    print(rest.parsed_obj)
    print(rest.claim_id)

    print(soap.parsed_obj)
