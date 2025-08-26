
# Desafio Técnico – Integração C# e Python

## ⏱ Duração sugerida: 3h30

Este desafio avalia sua capacidade de interpretar código legado, tomar decisões técnicas e integrar sistemas em diferentes linguagens.

---

## 📁 Estrutura

- `/csharp` – Contém o código legado em C# que precisa ser corrigido e o arquivo para o teste
- `/python` – Contém o arquivo para implementar o código em Python e o arquivo para o teste


---

## ✅ Tarefas

### Parte 1 – C# (correção e testes)

Você recebeu o seguinte código legado em um controller de API:

```csharp
[HttpPost]
public async Task<IActionResult> Import([FromBody] Pedido pedido)
{
    if (pedido.Id == null)
        return BadRequest();

    if (pedido.Valor < 0)
        return BadRequest();

    _pedidoService.Salvar(pedido);
    return Ok();
}
```

#### Tarefas:

1. Liste todos os problemas técnicos ou lógicos que você identifica no código.
2. Reescreva o código corrigindo os problemas e aplicando boas práticas.
3. Implemente **1 teste de unidade** e **1 teste de integração mínima**.
4. Suponha que após importar pedidos, o sistema precisa publicar uma **mensagem de evento assíncrona**.
   - Descreva como você implementaria isso (sem usar bibliotecas prontas).
   - Apresente a estrutura básica da lógica.

---

### Parte 2 – Python (enriquecimento com fallback)

Você deve criar uma função `enrich_order(order: dict) -> dict` que:

- Valida a entrada
- Simula chamada externa para enriquecer os dados
- Em caso de falha, busca os dados de um **cache local com expiração de 5 minutos**
- Sempre retorna o pedido com o campo `"cliente_nome"`

#### Tarefas:

1. Implemente a função `enrich_order`.
2. Crie um sistema de **cache local com expiração** (dicionário simples).
3. Escreva testes cobrindo:
   - Sucesso no enriquecimento
   - Fallback em caso de erro
   - Expiração de cache
4. Explique como lidaria com **concorrência** se vários processos chamassem a função ao mesmo tempo.

---

### Parte 3 – Raciocínio Técnico

Responda às seguintes perguntas diretamente neste arquivo (README.md):

1. Que problemas você antecipa ao integrar os dois módulos?
Resposta: O maior problema seria em manter um bom desempenho e uma boa observabilidade entre os módulos.
2. Como garantiria **consistência de dados** entre os serviços, considerando que o envio de mensagens é assíncrono?
Resposta: O ideal seria implementar um sistema de filas para os serviços, garantindo que os dados não tenha perca de sequencia em alto numero de requisições.
3. Como garantiria **observabilidade** (ex: logs e rastreabilidade)?
Resposta: Para cada evento de erro, seria ideal emitir um log de erro e centralizar em algum serviço externo, como o "new relic" por exemplo.
4. Como prepararia esse sistema para escalar horizontalmente sem perder rastreabilidade e tolerância a falhas?
Resposta: Configuração do "nginx" como proxy reverso para balanceamento de carga, garantindo que os headers de rastreabilidade não sejam perdidos.

---

## 🔒 Regras

- **Proibido o uso de ferramentas de IA** (ChatGPT, Copilot, etc.)
- As decisões técnicas devem ser **justificadas com clareza**
- O código deve ser **organizado e funcional**
- Envie a solução em um repositório com os diretórios `/csharp` e `/python`

---

## 🧪 Avaliação

| Critério                                  | Peso |
|-------------------------------------------|------|
| Clareza nas decisões técnicas             | 30%  |
| Correção e qualidade do código            | 25%  |
| Capacidade de diagnosticar problemas      | 20%  |
| Organização e explicação das respostas    | 15%  |
| Boas práticas de testes, cache e logging  | 10%  |
