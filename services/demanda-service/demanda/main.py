from fastapi import FastAPI

app = FastAPI(title="demanda-service", version="0.1.0")


@app.get("/saude")
def saude():
    return {"status": "ok", "servico": "demanda-service"}


# TODO (ver docs/04-plano-de-trabalho.md):
# - POST   /api/v1/demandas        criar (comprador vem do token JWT)
# - GET    /api/v1/demandas        listar
# - GET    /api/v1/demandas/{id}   consultar
# - DELETE /api/v1/demandas/{id}   cancelar
