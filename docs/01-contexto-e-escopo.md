# 01. Contexto e escopo

## O Portal B2B

Portal distribuído com microsserviços comunicando por Kafka (Redpanda). Cada grupo da turma cuida de um ou mais serviços.

## O que é de Demanda (firme, vem do diagrama)

- Demanda única
- Demanda recorrente (frequência e quantidade)
- Publicar `demanda_criada` e `demanda_recorrente_gerada`
- Banco próprio (schema `demanda`)

## O que o grupo levantou, e a situação de cada item

| Responsabilidade | Situação |
|---|---|
| Análise e previsão de demanda | Em aberto: definir profundidade (ver pauta D3) |
| Avaliação de necessidade de reposição | Em aberto: depende de `estoque_atualizado` (pauta D4) |
| Alertas de alta/baixa demanda | Em aberto: evento Kafka, notificação é de "Sistemas Externos (futuro)" |
| Acompanhamento de status de compra | Parcial: status do pedido é do grupo de Pedidos (`pedido_atualizado`) |
| Processamento e gestão de pedidos de compra | **Fora do escopo**: serviço 7 (Pedidos) |
| Controle de orçamento de compras | Em aberto: não aparece no diagrama (pauta D1) |
| Relatórios e histórico de compras | Parcial: histórico de demandas é nosso; pedidos são do grupo de Pedidos |

## Fora de escopo

Pedidos, matching, negociação, logística, autenticação, telas.

## Dúvida central

O nome do grupo é "Compra e Demanda", mas o diagrama só tem o serviço de Demanda. Ver pauta D1.
