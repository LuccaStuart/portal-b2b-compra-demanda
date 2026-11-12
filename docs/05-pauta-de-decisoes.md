# 05. Pauta de decisões

## Para o professor

- **D1.** "Compra e Demanda" cobre só o serviço de Demanda, ou também orçamento, histórico e status de compra? Os pedidos ficam com Mercado/Pedidos?
- **D2.** O que é obrigatório entregar: código rodando, documentação, relatório, apresentação, testes?
- **D3.** Qual a profundidade esperada para previsão de demanda e alertas?
- **D5.** Outbox, DLT, retry e JSON Schema são obrigatórios para todos os grupos?

## Para os outros grupos

- **D4.** Fornecimento: a Demanda deve consumir `estoque_atualizado`?
- **D6.** Mercado: campos necessários em `demanda_criada` e `demanda_recorrente_gerada`; precisa de `demanda_cancelada`?
- **D7.** Autenticação: HS256 ou RS256; issuer, audience e claims.
- **D8.** Infraestrutura: porta, schema, tópicos, DLT, gateway.
- **D9.** Banco de Dados: quem escreve o DDL do schema `demanda`.
- **D10.** Produtos: o comprador pode cadastrar produto? Se puder, a demanda pode ser de produto ainda inexistente.

## Decididas

(nenhuma ainda)
