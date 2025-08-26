// TODO: Corrigir o código com base no enunciado


[HttpPost]
public async Task<IActionResult> Import([FromBody] Pedido pedido)
{
    // Nesse ponto os "ifs" do código podem ser resumidos em apenas um, já que eles possuem o mesmo retorno
    if (pedido.Id == null || pedido.Valor < 0)
        return BadRequest();

    // Como no enunciado não me passou o "_pedidoService" sendo inicializado, eu resolvi inicializa-lo nessa linha
    PedidoService _pedidoService = new PedidoService();
    _pedidoService.Salvar(pedido);
    // Aqui é a função assincrona que realiza o disparo de emails
    Task.Run(async () =>
    {
        // Aqui eu fiquei na duvida se era pra criar o service de envio de emails,
        // então eu fiz uma "falsa chamada" para simular um processo assincrono real
        await _emailService.SendMailAsync("Seu pedido foi salvo com sucesso!");
    });
    // Alteração do status Ok() para Created(),
    // como é um Post para salvar dados, o retorno tem que ser Created()
    return Created();
}


//Problemas técnicos encontrados:
//1- Os "ifs" do código podem ser resumidos em apenas um.

//2- Para salvar um pedido, a melhor solução seria fazer o autoincremento do Id no próprio banco,
//   para evitar pedidos com Ids duplicados e melhorar a rastreabilidade dos mesmos.

//3- O _pedidoService não é criado da maneira correta.

//4- O status Ok não está de acordo com a ação do post, o correto seria Created()

//5- Para o disparo assíncrono de mensagem, eu escolhi utilizar o Task.Run(),
//   chamando um evento de disparo de email. Esse evento seria criado como um "EmailService"
//   e faria o envio dos emails de maneira assincrona.