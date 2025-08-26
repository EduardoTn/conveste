# Crie testes de acordo com o enunciado

# 3. Escreva testes cobrindo:
#    - Sucesso no enriquecimento
#    - Fallback em caso de erro
#    - Expiração de cache

from enricher import order
import time

# Aqui é feito o teste de sucesso do enriquecimento
# nesse teste eu passo o parametro de sucesso como "true", para a fake api me retornar um "cliente_nome" aleatorio
def test_success_order():
    new_order = {"id" : 1, "success" : True}
    cliente_nome = order.enrich_order(new_order)["cliente_nome"]
    assert cliente_nome != None
    
# Aqui é feito o teste de falha do enriquecimento, 
# nesse teste eu passo o parametro de sucesso como "false", para a fake api me retornar um valor nulo
def test_fail_order():
    new_order = {"id" : 2, "success" : False}
    cliente_nome = order.enrich_order(new_order)["cliente_nome"]
    assert cliente_nome == None

# Aqui é feito o teste de expiração dos 5 minutos de cache, 
# para isso eu utilizei um time.sleep com um tempo superior a 5 minutos 
def test_expired_order_cache():
    new_order = {"id" : 3, "success" : True}
    cliente_nome = order.enrich_order(new_order)["cliente_nome"]
    assert cliente_nome != None
    time.sleep(301)
    assert order.enrich_order(new_order)["cliente_nome"] != cliente_nome

# Aqui é feito o teste de cache, 
# nesse teste eu passo o parametro de sucesso como "true", para a fake api me retornar um "cliente_nome" aleatorio, 
# em seguida eu aguardo um tempo que esteja dentro dos 5 minutos do cache e valido se o "cliente_nome" retornado é o mesmo que foi cacheado pela função
def test_order_cache():
    new_order = {"id" : 4, "success" : True}
    cliente_nome = order.enrich_order(new_order)["cliente_nome"]
    assert cliente_nome != None
    time.sleep(2)
    new_order["success"] = False
    assert order.enrich_order(new_order)["cliente_nome"] == cliente_nome
