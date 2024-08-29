# WhatsApp Messaging Automation
Este projeto automatiza o envio de mensagens via WhatsApp utilizando a API do WhatsApp Business. As mensagens são personalizadas para cada destinatário, conforme os dados extraídos de um arquivo Excel.

## Estrutura do Projeto
### Arquivos
- **datas.yaml**: Arquivo de configuração contendo as variáveis de ambiente necessárias para a execução do script.
- **opens.py**: Script que realiza a leitura de um arquivo Excel contendo as informações dos destinatários.
- **post_api.py**: Script principal que carrega as configurações, gera o corpo da mensagem e realiza a requisição à API do WhatsApp para enviar as mensagens.
  
### datas.yaml
Este arquivo YAML deve ser configurado com suas credenciais e informações específicas:

```yaml
Copiar código

access_token: $seu_token
URL: $sua_URL
path: $seu_caminho

access_token: O token de autenticação da API do WhatsApp.
URL: A URL da API para enviar a mensagem.
path: O caminho do arquivo Excel que contém os dados dos destinatários.
```
### opens.py
O script opens.py contém a classe ReadArchive, que é responsável por:

- Ler o arquivo Excel especificado.
- Extrair os dados das colunas nome, numero, e valor.
 
### post_api.py
O script principal que:

- Carrega as configurações do arquivo datas.yaml.
- Constrói o payload da mensagem com base nos dados extraídos.
- Envia as mensagens via API do WhatsApp.
  
## Requisitos
Python 3.x
Bibliotecas: Consulte o arquivo requirements.txt
Instale as dependências com: 

```
Copiar código

pip install -r requirements.txt
```

### Executando o Projeto
Preencha o arquivo datas.yaml com suas informações.
Coloque o arquivo Excel com os dados dos destinatários no caminho especificado no datas.yaml.

Execute o script principal:
```
Copiar código

python post_api.py
```

## Observações
- O arquivo Excel deve corresponder com as colunas passadas no script, não necessariamente "nome, numero e valor", mas podendo ser manipulada de acordo com sua necessidade.
- Certifique-se de que o token de acesso (access_token) e a URL da API estão corretos no arquivo datas.yaml.
  
## Contribuição
Se quiser contribuir para o projeto, sinta-se à vontade para abrir uma pull request ou relatar issues.


### Licença
Este projeto é licenciado sob a GNU Affero General Public License v3.0 (AGPL-3.0)
