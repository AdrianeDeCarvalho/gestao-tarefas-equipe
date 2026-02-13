# 📝 Gestão de Tarefas de Equipe

Este é um projeto desenvolvido com o framework **Django** para gerenciar o fluxo de atividades de uma equipe. O sistema permite o cadastro de tarefas com diferentes níveis de prioridade e controle de status de conclusão, servindo como uma ferramenta de organização interna de processos.

---

## 🚀 Funcionalidades
* **Gestão via Painel Administrativo:** Controle total de criação, edição e exclusão de tarefas através do Django Admin customizado.
* **Visualização Dinâmica:** Lista de tarefas renderizada no front-end com diferenciação visual.
* **Priorização Inteligente:** Sistema de escolhas para níveis de prioridade (Baixa, Média e Alta).
* **Feedback Visual:**
    * ✅ **Tarefas Concluídas:** Exibidas em verde e com efeito tachado.
    * ⏳ **Tarefas Pendentes:** Exibidas em vermelho e negrito.

---

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.12
* **Framework:** Django 6.0
* **Banco de Dados:** SQLite
* **Front-end:** HTML5 e CSS3

---

## 🏗️ Arquitetura e Conceitos Aplicados
Neste projeto, apliquei os pilares fundamentais do desenvolvimento Back-end com Django:

1.  **Padrão MVT (Model-View-Template):** Separação clara entre a lógica de dados, regras de negócio e interface.
2.  **ORM (Object-Relational Mapping):** Manipulação eficiente do banco de dados através de classes Python, sem necessidade de SQL manual.
3.  **Template Engine:** Uso de lógica de programação (`{% if %}`, `{% for %}`) e métodos especiais como `get_prioridade_display` dentro do HTML.



---

## 🔧 Como rodar o projeto localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/AdrianeDeCarvalho/gestao-tarefas-equipe.git](https://github.com/AdrianeDeCarvalho/gestao-tarefas-equipe.git)

2. **Crie e ative o ambiente virtual:**
```bash
python -m venv venv
# No Windows:
.\venv\Scripts\activate
```

3. **Instale as dependências:**
```bash
pip install django
```

4. **Execute as migrações:**
```bash
python manage.py migrate
```

5. **Inicie o servidor:**
```bash
python manage.py runserver
```

Acesse no navegador:``` http://127.0.0.1:8000/ ```
