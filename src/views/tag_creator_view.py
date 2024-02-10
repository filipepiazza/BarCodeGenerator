from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controller.tag_creator_controller import TagCreatorController

class TagCreatorView:
    '''
    responsability for interacting with http
    '''

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        product_code = body["product_code"]

        #logica de regra de negocio
        tag_creator_controller = TagCreatorController()
        formatted_response = tag_creator_controller.create(product_code)

        # retorno http
        return HttpResponse(status_code=200, body=formatted_response)
