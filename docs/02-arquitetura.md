# 02. Arquitetura

## Visão geral

- `demanda-service`: API REST (via API Gateway) + produtor/consumidor Kafka + banco próprio (schema `demanda`).
- Todas as mensagens entre serviços passam pelo Kafka (Redpanda).

## API REST (proposta)

| Método | Rota | Descrição |
|---|---|---|
| POST | `/api/v1/demandas` | Cria demanda. O comprador vem do token JWT, nunca do corpo. |
| GET | `/api/v1/demandas` | Lista as demandas do comprador |
| GET | `/api/v1/demandas/{id}` | Consulta uma demanda |
| DELETE | `/api/v1/demandas/{id}` | Cancela a demanda |

Escopo exigido no token: `BUYER`. A empresa vem do claim `tenant_id`.

## Banco (schema `demanda`, a combinar com o grupo de Banco de Dados)

- `demanda`: dados da demanda (tipo, produto, quantidade, destino, prazo, preço máximo, frequência, status)
- `produto_referencia`: cópia local dos produtos, alimentada por `produto_cadastrado`
- `outbox`: eventos a publicar, gravados na mesma transação da demanda
- `processed_events`: `eventId` já processados (idempotência)

## Padrões da turma a seguir

Envelope de eventos, chave da mensagem = `aggregateId`, payload em camelCase, números com até 2 casas,
`correlationId`, retry (3 tentativas) e DLT. **Confirmar no `contrato-eventos.md` do kit de infra**,
pois estas regras foram repassadas por um membro do grupo.

## Pontos de sistemas distribuídos para o relatório

Idempotência, ordem de eventos, falha do broker (outbox), consistência eventual da cópia de produtos.
