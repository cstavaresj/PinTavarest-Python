# 📘 PinTavarest-Python

Este repositório contém um projeto desenvolvido em **Python** utilizando o framework **Flask** e o **Flask-SQLAlchemy** para integração com banco de dados. O projeto, chamado "PinTavarest", é um site simples que imita o Pinterest, permitindo que usuários criem contas, façam login e publiquem imagens. Este projeto foi desenvolvido como parte do mini curso [*Criação de Sites em Python*](https://blp.hashtagtreinamentos.com/python/minicurso/criacao-sites-python) oferecido pela **Hashtag Treinamentos**.

---

## 🛠️ Requisitos

- **Python** (versão 3.x) instalado.
- **Flask** e **Flask-SQLAlchemy** instalados (`pip install flask flask-sqlalchemy`).
- Banco de dados compatível com SQLAlchemy (ex.: SQLite para simplicidade ou MySQL).
- Navegador web (Chrome, Firefox, etc.) para acessar o site.

---

## 📂 Estrutura do Repositório

O repositório contém os seguintes arquivos e pastas: `main.py` é o arquivo principal que contém a lógica do site com Flask; `criar_banco.py` é o script para criar o banco de dados com as tabelas necessárias.

---

## ▶️ Como Executar os Códigos

1. **Configurar o Ambiente:**
   - Certifique-se de que o Python está instalado.
   - Crie e ative um ambiente virtual (opcional, mas recomendado):  
     - `python -m venv venv`  
     - No Windows: `venv\Scripts\activate`  
     - No Linux/macOS: `source venv/bin/activate`
   - Instale as dependências: `pip install flask flask-sqlalchemy`.

2. **Criar o Banco de Dados:**
   - Execute o script `criar_banco.py` para criar o banco de dados e as tabelas:  
     - `python criar_banco.py`

3. **Executar o Site:**
   - Execute o arquivo principal: `python main.py`.
   - O Flask iniciará o servidor local (geralmente em `http://127.0.0.1:5000`).

4. **Acessar o Site:**
   - Abra o navegador e acesse `http://127.0.0.1:5000`.
   - Crie uma conta, faça login e comece a publicar imagens.

---

## 📥 Como Baixar o Repositório

1. Clique no botão verde "Code" no topo da página do GitHub.
2. Selecione "Download ZIP" e extraia o arquivo no seu computador.
3. Ou use o Git: `git clone https://github.com/cstavaresj/PinTavarest-Python.git`

---
