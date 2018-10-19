
//inicializa instancia de XMLHtppRequest
var xhr = new XMLHttpRequest();

//define url da requisição
var url_request = "https://www.sistemagestaoonline.com.br/sistema/rest/api_sgo.wsconsultaestoque"

//monta requisição POST sincrona
xhr.open('POST', url_request, false);

//define body
var chave = "et53r4g934j90tj39gjhy93jy39jg93=gb"
var produtoReferencia = "123"

var params = JSON.stringify({ "Chave": chave,"ProdutoReferencia":produtoReferencia });

//define header
http.setRequestHeader("Content-type", "application/json");

//executa requisição
xhr.send(params);
 
//interpreta e printa resultado
xhr.onreadystatechange = processRequest;
 
function processRequest(e) {
    
    if (xhr.readyState == 4 && xhr.status == 200) {
         var response = JSON.parse(xhr.responseText);
        alert(response.EstoqueAtual);
    } 
}