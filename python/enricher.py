# Implementar a função enrich_order conforme o enunciado

### Parte 2 – Python (enriquecimento com fallback)
# Você deve criar uma função `enrich_order(order: dict) -> dict` que:
# - Valida a entrada
# - Simula chamada externa para enriquecer os dados
# - Em caso de falha, busca os dados de um **cache local com expiração de 5 minutos**
# - Sempre retorna o pedido com o campo `"cliente_nome"`

# #### Tarefas:

# 1. Implemente a função `enrich_order`.
# 2. Crie um sistema de **cache local com expiração** (dicionário simples).
# 3. Escreva testes cobrindo:
#    - Sucesso no enriquecimento
#    - Fallback em caso de erro
#    - Expiração de cache
# 4. Explique como lidaria com **concorrência** se vários processos chamassem a função ao mesmo tempo.
# RESPOSTA: 
# A solução é usar as transactions do banco de dados, enfileirando os processos e armazenando os dados já carregados em cache no sistema por um tempo limitado, evitando assim requisições excessivas.

# Nessas libs eu escolhi importar o "time" para fazer o timeOut do cache e a lib "Faker" para gerar nomes randomicos.
# A decisão da lib "Faker" foi para trazer mais consistencia aos testes unitários
import time
from faker import Faker

# Aqui eu inicializo as variaveis
fake = Faker('pt-br')
_cache = {}
cache_timeout = 300

# Aqui eu criei uma classe para simular uma falsa API, 
# nessa classe eu tenho uma função que retorna o nome do cliente caso a chave for "true", 
# caso a chave de sucesso seja "false", ele vai retornar um erro de conexão para a função que o chama
class falsa_api():
    def falsa_api_externa(id: int, success: bool) -> str:
        if success:
            return (cache.buscar_dados_cache(id) or fake.name())
        else:
            raise ConnectionError("Erro na busca")

# Essa é a classe de cache, aqui eu salvo os dados de "id", "nome", "time" na variavel _cache que foi inicializada previamente, 
# caso o dado "time" tenha expirado os 5 minutos do teste, ele faz o "Delete" do cache na hora de listar e retorna um valor nulo
class cache():
    def salvar_dados_cache(id: int, nome: str):
        _cache[id] = (nome, time.time())

    def buscar_dados_cache(id: int):
        if id in _cache:
            nome, timeout = _cache[id]
            if time.time() - timeout < cache_timeout:
                return nome
            else:
                del _cache[id]
                return None

# Essa é a classe de order, aqui que é implementado a função do teste, 
# primeiro eu comecei validando o tipo do parametro passado na função 
# e em sequencia eu valido se possui uma chave de "id" para fazer a chamada da falsa api, 
# caso passe nas validações iniciais, eu inicializo a variavel "cliente_nome" e tento chamar a falsa api para enriquecer os dados, 
# se a falsa api me retornar os dados corretamente, ele vai salvar os dados no cache e retornar o objeto "new_order", 
# porém se a falsa api retornar algum erro, a função vai tentar buscar o "cliente_nome" no cache salvo
class order():
    def enrich_order(order: dict) -> dict:
        if not isinstance(order, dict):
            raise TypeError("Erro no tipo order")
        if "id" not in order:
            raise ValueError("Order não possui id") 
        
        cliente_nome = None
        try:
            cliente_nome = falsa_api.falsa_api_externa(order["id"], order["success"])
            cache.salvar_dados_cache(order["id"], cliente_nome)
        except Exception:
            cliente_nome = cache.buscar_dados_cache(order["id"])

        new_order = order
        new_order["cliente_nome"] = cliente_nome
        return new_order