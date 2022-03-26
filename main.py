from app.views import zap, viva_real
from fastapi import FastAPI

app = FastAPI()
app.include_router(zap.zap_view)
app.include_router(viva_real.viva_real_view)

