// Crie testes de acordo com o enunciado

using System.Net;
using Xunit;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Testing;

namespace Pedido.Controllers.Tests
{
    // Como a única resposta da função "Import" é apenas o status, os testes de integração e unitarios foram apenas validando esse retorno.
    public class TesteUnitarioImportacao
    {
        // Aqui eu fiz 3 testes unitários simples,
        // o primeiro valida o retorno do Id como nulo
        public void ImportIdBadRequest()
        {
            Pedido pedido = new Pedido(null, 5);
            PedidoController _controller = new PedidoController();
            var result = _controller.Import(pedido);
            Assert.IsType<BadRequestResult>(result);
        }
        // o segundo valida o retorno do Valor negativo
        public void ImportValorBadRequest()
        {
            Pedido pedido = new Pedido(2, -3);
            PedidoController _controller = new PedidoController();
            var result = _controller.Import(pedido);
            Assert.IsType<BadRequestResult>(result);
        }
        // o terceiro valida se o Pedido foi criado
        public void ImportSuccess()
        {
            Pedido pedido = new Pedido(2, 10);
            PedidoController _controller = new PedidoController();
            var result = _controller.Import(pedido);
            Assert.IsType<CreatedObjectResult>(result);
        }
    }

    public class TesteIntegracaoImportacao : IClassFixture<WebApplicationFactory<Program>>
    {
        private readonly HttpClient _client;
        public TesteIntegracaoImportacao(HttpClient client)
        {
            _client = client;
        }
        // aqui eu segui a mesma lógica dos testes unitários e implementei os mesmos testes
        // o primeiro valida o retorno do Valor negativo
        public async Task ImportValorBadRequestAsync()
        {
            Pedido pedido = new Pedido(2, -3);
            var postResponse = await _client.PostAsJsonAsync("/import", pedido);
            Assert.Equal(HttpStatusCode.BadRequest, postResponse.StatusCode);
        }
        // o segundo valida o retorno do Id como nulo
        public async void ImportIdBadRequest()
        {
            Pedido pedido = new Pedido(null, 21);
            var postResponse = await _client.PostAsJsonAsync("/import", pedido);
            Assert.Equal(HttpStatusCode.BadRequest, postResponse.StatusCode);
        }
        // o terceiro valida se o Pedido foi criado
        public async void ImportSuccess()
        {
            Pedido pedido = new Pedido(2, 10);
            var postResponse = await _client.PostAsJsonAsync("/import", pedido);
            Assert.Equal(HttpStatusCode.OK, postResponse.StatusCode);
        }
    }
}