# Projeto de Automações em Python#
Este projeto consiste em um conjunto de scripts Python que realizam diversas automações, incluindo:
1. Atualização de Conteúdo em Arquivo TXT: 
O script atualizar_arquivo_txt.py lê o conteúdo de um arquivo TXT, adiciona uma mensagem de boa noite e escreve o conteúdo atualizado de volta no arquivo.
   ```bash
      with open("document2.txt") as arquivo:
          conteudo = arquivo.read()
          print(conteudo)
      
      nome_arquivo = 'document2.txt'
      with open(nome_arquivo, 'r') as arquivo:
          conteudo_atual = arquivo.read()
      
      conteudo_novo = conteudo_atual + '\nTenham uma boa noite!'
      
      with open(nome_arquivo, 'w') as arquivo:
          arquivo.write(conteudo_novo)
      
      print("Conteúdo adicionado com sucesso.")
      print(conteudo_novo).

2. Backup de Diretórios: 
O script fazer_backup.py realiza o backup de um diretório para outro, adicionando a data e hora no nome do diretório de backup. 
   ```bash
       with open("document2.txt") as arquivo:
           conteudo = arquivo.read()
           print(conteudo)
       
       nome_arquivo = 'document2.txt'
       with open(nome_arquivo, 'r') as arquivo:
           conteudo_atual = arquivo.read()
       
       conteudo_novo = conteudo_atual + '\nTenham uma boa noite!'
       
       with open(nome_arquivo, 'w') as arquivo:
           arquivo.write(conteudo_novo)
       
       print("Conteúdo adicionado com sucesso.")
       print(conteudo_novo)


3. Envio Automático de E-mails: 
O script enviar_email.py envia automaticamente um e-mail com uma mensagem de agradecimento e links para arquivos e bots usados em uma oficina.
   ```bash
   import smtplib
   import email.message
   
   def enviar_email():  
       corpo_email = """
       <p>Boa noite pessoal 😀</p>
       <p>Obrigado a todos que participaram da minha oficina "Introdução a automação com Python", meus mais sinceros agradecimentos a todos vocês</p>
       <p>Espero que tenham gostado e que tenham aprendido bastante, qualquer dúvida que vocês tiverem, podem me mandar um email que eu respondo o mais rápido possível</p>
       <p>Além disso vou encaminhar todos os arquivos e bots usados em aula, inclusive este que está enviando o email automático para todos vocês</p>
       <p>https://github.com/Jhonnee101/automacoes-em-Python.git</p>
       <p>Espero que tenham gostado e até a próxima!</p>
       """
   
       msg = email.message.Message()
       msg['Subject'] = "Introdução a automação com Python"
       msg['From'] = 'seu_email@gmail.com'
       msg['To'] = 'destinatario@gmail.com'
       password = 'sua_senha' 
       msg.add_header('Content-Type', 'text/html')
       msg.set_payload(corpo_email )
   
       s = smtplib.SMTP('smtp.gmail.com: 587')
       s.starttls()
       # Login Credentials for sending the mail
       s.login(msg['From'], password)
       s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
       print('Email enviado')






 
