# 03. Eventos e integrações

Proposta para revisão do grupo e envio ao Mercado. Formato do envelope: ver `comum/contratos/`.

## Eventos publicados

### `demanda_criada`
Produtor: demanda-service. Chave: `demandaId`. Consumidor: Mercado.

| Campo | Tipo | Descrição |
|---|---|---|
| demandaId | texto | Identificador da demanda |
| compradorId | texto | Empresa compradora (vem do token) |
| produtoId | texto | Produto desejado (deve existir na cópia local) |
| unidade | texto | KG, TON, UN, CX ou L |
| quantidade | número | Maior que zero |
| precoMaximo | número ou null | Por unidade, em BRL, até 2 casas |
| destino | objeto | `{cidade, uf}` (a Logística precisa do destino) |
| prazoDesejado | data e hora ou null | Até quando precisa receber |
| tipo | texto | `UNICA` ou `RECORRENTE` |
| frequencia | texto ou null | Para `RECORRENTE`: periodicidade (ex.: `SEMANAL`). Valores a definir |
| criadoPor | objeto | `{empresaId, usuarioId}` |
| criadoEm | data e hora | Momento da criação |

### `demanda_recorrente_gerada`
Ocorrência concreta gerada por uma demanda recorrente.

Campos: `demandaId` (recorrente de origem), `ocorrenciaId`, `compradorId`, `produtoId`, `unidade`, `quantidade`,
`precoMaximo`, `destino`, `prazoDesejado`, `geradoEm`, `proximaOcorrenciaEm`.

### `demanda_cancelada` (proposto)
Campos: `demandaId`, `compradorId`, `motivo` (opcional), `canceladoEm`, `canceladoPor`.

## Eventos consumidos

| Evento | Origem | Uso |
|---|---|---|
| `produto_cadastrado` | Fornecimento e Produtos | Preencher `produto_referencia` |
| `produto_atualizado`, `produto_excluido` | Fornecimento e Produtos | Propostos, sem tópico ainda |
| `estoque_atualizado` | Fornecimento | A confirmar se a Demanda deve consumir (reposição) |
| `pedido_atualizado` | Pedidos | A confirmar, só se formos mostrar status de compra |

## O que pedir a cada grupo

- **Mercado/Pedidos:** os campos acima servem? Precisam de `demanda_cancelada`? O `destino` precisa chegar no `pedido_criado` para a Logística.
- **Fornecimento e Produtos:** tópicos `produto_atualizado`/`produto_excluido` vão existir? Demanda deve consumir `estoque_atualizado`?
- **Autenticação:** HS256 ou RS256? Issuer e audience? Claim `tenant_id`?
- **Infraestrutura:** porta, schema e usuário do banco; criação dos tópicos e de `demanda.dlt`; rotas no gateway.
- **Banco de Dados:** quem escreve o DDL do schema `demanda`.
- **UX/UI:** telas de cadastro, lista e alertas de demanda.
- **Teste:** endpoints e payloads de exemplo.
