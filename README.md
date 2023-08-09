# Automação de Envio de Email com Anexo

Este projeto é resultado da participação na "Semana do Python na Prática", organizada pela Empowerdata. O desafio proposto durante o evento foi a automação do envio de emails com dados da bolsa de valores. Além de cumprir o desafio, fui além e desenvolvi uma automação que faz parte da minha rotina de trabalho diária.

## Funcionalidades

A automação consiste em um script Python que realiza as seguintes tarefas:
- Abre o navegador e acessa o Gmail para criar um novo email
- Preenche os campos de destinatário, cópia, assunto e mensagem
- Anexa automaticamente o arquivo mais recente de uma pasta específica
- Envia o email com o anexo

## Como Utilizar

1. Clone este repositório para o seu computador usando o comando:
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
2. Instale as bibliotecas necessárias usando o comando: pip install pyautogui pyperclip
3. Abra o arquivo `automacao-prestadores.py` em um editor de código.
4. **Modifique Informações Sensíveis:** No código, remova qualquer informação sensível, como endereços de email ou senhas.
5. Execute o script manualmente para testar se ele está funcionando conforme o esperado.

## Agendamento de Tarefas no Windows

Para automatizar o envio de emails diariamente, você pode utilizar a ferramenta de Agendamento de Tarefas do Windows:

1. Abra o "Agendador de Tarefas" no Windows.
2. Crie uma nova tarefa e configure a frequência para diariamente e horário.
3. Na aba "Ações", adicione uma ação "Iniciar um Programa".
4. No campo "Programa/script", coloque o caminho para o arquivo `.bat` que você criou para executar o script Python.
5. No campo "Iniciar em (opcional):", especifique o diretório onde o arquivo .bat está localizado exemplo: (C:\AUTOMACAO\AUTOMAÇÃO-PYTHON).
6. Salve a tarefa e aguarde para que ela seja executada automaticamente todos os dias no horário selecionado (Caso queira testar, clique sobre a tarefa agendada e selecione Executar).

## Contribuição

Sinta-se à vontade para contribuir com melhorias neste projeto. Abra uma "issue" para discutir novas funcionalidades ou correções. Pull requests são bem-vindos!

## Contato

Se tiver alguma dúvida ou sugestão, entre em contato através do meu perfil no LinkedIn.

[LinkedIn](https://www.linkedin.com/in/paulo-jc-mesquita/)

