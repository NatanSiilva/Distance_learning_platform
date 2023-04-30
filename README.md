## Plataforma de Aprendizagem a Distância
Este projeto é uma plataforma de aprendizagem a distância desenvolvida com o framework Django. A plataforma permite que os usuários se cadastrem como alunos ou instrutores e tenham acesso a diversos recursos educacionais, incluindo aulas, questionários e fóruns.

## Instalação

- Clone o repositório:
git clone https://github.com/NatanSiilva/Distance_learning_platform.git

- Crie e ative um ambiente virtual:
python -m venv venv
source venv/bin/activate   # no Windows: venv\Scripts\activate

- Instale as dependências:
pip install -r requirements.txt

- Crie as tabelas do banco de dados:
python manage.py migrate

- Crie um usuário administrador:
python manage.py createsuperuser

- Execute o servidor de desenvolvimento:
python manage.py runserver

# Funcionalidades
A plataforma de aprendizagem a distância possui as seguintes funcionalidades:

- Cadastro de usuários como alunos ou instrutores
- Possibilidade de um instrutor criar turmas e adicionar alunos
- Criação de aulas, questionários e fóruns
- Participação em questionários e fóruns
- Visualização do progresso do aluno em cada turma

# Licença

Este projeto está licenciado sob a licença MIT - consulte o arquivo LICENSE para obter mais detalhes.
