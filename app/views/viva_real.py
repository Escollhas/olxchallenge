from fastapi import APIRouter

viva_real_view = APIRouter()


@viva_real_view.get("/viva_real/")
async def viva():
    return "Viva imóveis"

