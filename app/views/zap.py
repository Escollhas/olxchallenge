from fastapi import APIRouter

zap_view = APIRouter()


@zap_view.get("/zap/")
async def zap():
    return "Zap imoveis"
