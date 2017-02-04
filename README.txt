Teste técnico para vaga de Desenvolvedor Python/Django na M2AGRO
Lista de requisitos entregue via email por Maíra Rabelo.

Inicializado em: 03/02/2017.
Autor: Felipe Wanderley.

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

