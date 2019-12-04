Orientações gerais 

Criar um repositório GIT aberto e nos enviar o link para acompanhamento das atividades a fim de mostrar o processo de trabalho. 
 Critérios de Avaliação 
- Atender os requisitos descritos 
- Código limpo e organizado 
- Reaproveitamento de código 
- Criatividade 
- Documentação de código 
- Documentação do projeto (readme) 

Problema 

Recebemos vários tipos de datasets com valores e formatos diferentes. Ao receber os dados é importante fazer uma validação preliminar para verificar inconsistências. Essa avaliação é feita manualmente. Gerando uma demora no processamento.  

Solução 

Criar um sistema web, que receberá o dataset em CSV e irá validar de forma automática. Ao receber os dados o validador lerá o schema onde estarão as regras de validação e irá validar os dados baseados nesse schema. 

O schema será composto por:  o nome do campo,  o validador e uma mensagem de erro 

Dataset exemplo: link

 Requisitos:

 - Tela de upload do dataset 

 - Validador genérico baseado em um schema 

 - Salvar logs de erro no banco 

 -Tela para apresentar os logs 

Você ganhará pontos extras se: 

- A solução estiver em contêineres 

- Preparada para rodar em ambientes na nuvem 

- Testes automatizados 

Obs: Mesmo que não seja possível concluir as atividades em sua integralidade, pedimos que envie o que foi possível fazer e qual foi a linha de raciocínio para podermos considerar. 
