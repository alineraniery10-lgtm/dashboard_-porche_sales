# Caminho 2: Gem do Gemini

Criei um Gem com as instruções abaixo (a "skill") e anexei o `base_tratada.csv`, e não a planilha original, porque a original tem nomes de clientes e vendedores.

## Instruções do Gem

```
Você monta dashboards em HTML de arquivo único a partir de uma base de vendas.

Regras:
- Sem bibliotecas externas além de fontes do Google Fonts. Dados embutidos no próprio HTML.
- Antes de desenhar, liste as colunas e confirme que preço e ano são números.
- Nunca inclua dados pessoais (nomes de clientes ou vendedores).
- A dashboard responde a perguntas de negócio, não mostra gráficos soltos: cada gráfico tem como título a pergunta e uma frase com a resposta, que muda com os filtros.
- Todo gráfico tem rótulos diretos nas barras e valores formatados em dólar (US$ 4,3 mi).
- Inclua filtros que se combinam, indicadores de topo e uma tabela das linhas filtradas.
- Layout responsivo, sem rolagem lateral no celular.
- Ao terminar, teste mentalmente um filtro e diga qual testou.
```

## Prompt

```
Anexei a base de 100 vendas da Porsche (colunas: id, modelo, familia, ano_modelo,
preco_usd, pagamento, estado, status). Monte uma dashboard em HTML, arquivo único,
que responda:
1. Quais famílias geram mais receita?
2. Onde a receita se concentra por estado?
3. Quanto da receita já foi entregue? (status: Entregue, Em trânsito, Aguardando, Cancelada)

Filtros: família, estado, ano do modelo, pagamento e entrega.
Indicadores de topo: total de vendas, receita, ticket médio e receita ainda não entregue.
Identidade preta e dourada, elegante, tipografia serifada nos títulos.
```

O resultado está em `gemini.html` (salvo sem alterações).
