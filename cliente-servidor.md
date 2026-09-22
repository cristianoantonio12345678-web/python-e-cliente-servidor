# Relatório: Arquitetura Cliente-Servidor (cliente1.py e servidor.py)

## 1. Visão geral
Os dois arquivos implementam um sistema de chat em rede usando **sockets TCP** e **threads**, seguindo o modelo cliente-servidor.

## 2. servidor.py — o lado servidor
- **Criação do socket**: `socket.socket(socket.AF_INET, socket.SOCK_STREAM)` cria um socket TCP/IPv4.
- **Bind e listen**: associa o socket a `127.0.0.1:5000` e entra em modo de escuta.
- **Loop de aceitação**: `accept()` bloqueia até um cliente conectar; a conexão é guardada em `clientes`.
- **Multithreading**: cada cliente ganha sua própria thread (`gerenciar_cliente`), permitindo várias conexões simultâneas.
- **Broadcast**: `enviar_para_todos` repassa mensagens a todos os clientes, exceto quem enviou.
- **Tratamento de desconexão**: erros no `recv()` removem o cliente da lista (`remover_cliente`).

## 3. cliente1.py — o lado cliente
- **Conexão**: cria o socket e usa `connect()` com o IP/porta do servidor.
- **Thread de recebimento**: `receber_mensagens` escuta o servidor continuamente.
- **Thread principal**: captura o que o usuário digita e envia via `send()`.
- **Encerramento**: digitar "sair" fecha a conexão.

## 4. Como as partes se comunicam
1. Servidor sobe e escuta na porta 5000.
2. Cliente conecta nesse IP/porta.
3. Mensagens do cliente são redistribuídas pelo servidor aos demais.
4. Cada cliente recebe em tempo real via sua thread de escuta.

## 5. Ponto de atenção
Há inconsistência de IP:
- `servidor.py` usa `HOST = '127.0.0.1'` (só localhost).
- `cliente1.py` tenta conectar em `HOST = '172.28.131.232'`.

Se forem a mesma máquina, o cliente deve usar `127.0.0.1`. Se forem máquinas diferentes, o servidor precisa usar o IP real da rede (ou `'0.0.0.0'`).