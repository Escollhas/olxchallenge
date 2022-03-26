from app.controller.execute import get_real_state
from app.services.pagination import make_pagination
from fastapi import APIRouter

viva_real_view = APIRouter()


@viva_real_view.get("/viva_real/", status_code=200)
async def viva(page_number: int = 1, page_size: int = 20):
    real_state = get_real_state()
    response = make_pagination(real_state, page_number, page_size)
    return response
