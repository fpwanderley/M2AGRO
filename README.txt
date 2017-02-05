Teste técnico para vaga de Desenvolvedor Python/Django na M2AGRO
Lista de requisitos entregue via email por Maíra Rabelo.

Inicializado em: 03/02/2017.
Autor: Felipe Wanderley.

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

Como instalar e utilizar a API:

1 - Configurar o BD na máquina:
    O primeiro passo é realizar as configurações referentes ao BD na máquina.

    1.1 - O SGBD sendo utilizado nesse projeto é o PostGreSQL. Por isso é necessário instalá-lo antes de tudo:
    1.2 - É necessário também criar um usuário com permissões de login com os seguintes parâmetros:
        login: m2agro
        password: m2agro
    1.3 - Este projeto possui um comando make para criação do BD, e realização das migrações necessárias. Uma vez na
    pasta \M2Agro\M2Agro:
        >> make initiate_db

2 - Ativar o servidor de desenvolvimento:
    Para realizar os testes nas API's desenvolvidas é necessário ativar o servidor de desenvolvimento oferecido pelo
    próprio Django. Esse projeto também possui um comando make pra ativá-lo. Uma vez na pasta \M2Agro\M2Agro:
        >> make run

3 - Utilizar cada uma das API's:
    Todas as APIs solicitadas na descrição foram implementadas para a interface REST-json, utilizando o Django Rest
    Framework. Para testá-las, basta buscar por sua URL, método HTTP e formatação do payload. Essas informações estão
    presentes em cada um dos métodos implementados em \M2Agro\API\views.py.


>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

Idéias Complementares:
1 - Quanto à implementação de uma API SOAP, eu criaria outro App dentro do projeto, mas sem a criação dos modelos já
criados. Esse novo App seria basicamente para incluir views e respectivos métodos para recebimento e envio dos XMLs.
Para me auxiliar na manipulação desses XMLs eu utilizaria a lib PyXB, a qual já me foi útil anteriormente ao implementar
um sistema de emissão de notas fiscais.

2 - Quanto ao cálculo do custo médio de um determinado produto, o método criado foi um pouco além do que foi pedido na
descrição do projeto, possibilitando que o desenvolvedor possa utilizá-lo para calcular o custo médio referente a qualquer
mês desejado, não apenas o mês anterior. No entanto, o funcionamento padrão do método obedece ao que foi pedido na descrição
do projeto.

3 - O modelo ServiceProduct foi criado para a inclusão dos dados 'quantity' e 'total_cost' de um determinado Product em
um Service. Apesar de esse modelo não ter sido mencionado na descrição, sua criação foi considerada adequada à situação.

4 - Quanto ao Teste de Lógica, a sua implementação foi realizada por meio da criação de uma matriz que obedecesse ao que
estava descrito no teste. Acredito que faria mais sentido a utilização de matriz ao invés de criar uma tabela no BD para
isso. Se for imprescindível o uso de BD para realização desse quesito, favor informar.

