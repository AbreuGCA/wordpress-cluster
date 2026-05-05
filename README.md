# Visão Geral do Projeto

O objetivo deste trabalho é realizar testes de carga em um ambiente com múltiplas instâncias do WordPress. O teste de carga permite modelar o uso esperado do software simulando múltiplos usuários simultâneos. Com isso, é possível medir a qualidade do serviço através do desempenho percebido pelo usuário final.

## Componentes Principais

- **Locust**: Ferramenta de teste de carga em Python para gerar carga em sites.
- **WordPress Cluster**: Múltiplas instâncias do WordPress rodando em contêineres Docker.
- **Nginx**: Balanceador de carga, distribuindo requisições entre as instâncias.
- **MySQL**: Banco de dados compartilhado para todas as instâncias do WordPress.

---

## 🏗️ Arquitetura do Sistema

A infraestrutura é composta por:

- **Balanceador de Carga (Nginx)**: Escuta na porta 80 e distribui o tráfego para o pool de servidores wordpress1, wordpress2 e wordpress3.
- **Servidores de Aplicação**: Três instâncias independentes do WordPress (v5.4.2).
- **Banco de Dados**: Uma única instância MySQL 5.7.
- **Gerador de Carga (Locust)**: Simula o comportamento dos usuários através de scripts Python.

---

## 🛠️ Configuração e Instalação

### 1. Estrutura de Pastas

Certifique-se de que os arquivos estão organizados da seguinte forma:

- `docker-compose.yml`: Define os serviços e volumes.
- `nginx.conf`: Configuração do proxy reverso e upstream.
- `locust-scripts/locustfile.py`: Script com os cenários de teste.
- `/html`: Pasta compartilhada para os arquivos do WordPress.

### 2. Variáveis de Ambiente do Locust

O Locust utiliza as seguintes variáveis configuradas no `docker-compose.yml`:

- `ATTACKED_HOST`: URL do site a ser testado (neste caso, http://nginx).
- `LOCUST_FILE`: O script de teste utilizado.
- `LOCUST_OPTS`: Opções adicionais como número de usuários e taxa de subida.

---

## 🧪 Execução dos Testes

### Iniciando o Ambiente

Para subir todos os serviços, execute:

```bash
docker-compose up -d
```

### Acessando o Locust

Abra o navegador em [http://localhost:8089](http://localhost:8089).

- Defina o Número de Usuários e a Taxa de Subida (Hatch Rate).
- Inicie o teste.

### Cenários de Teste Exigidos

Conforme os requisitos da atividade, os testes devem cobrir:

- **Cenário A**: Blog post com imagem de aproximadamente 1MB.
- **Cenário B**: Blog post com texto de aproximadamente 400KB.
- **Cenário C**: Blog post com imagem de 300KB.

---

## 📊 Entregáveis e Métricas

Cada cenário deve ser executado variando os seguintes parâmetros:

- **Usuários Simultâneos**: 10, 100 e 1000.
- **Instâncias WordPress**: 1, 2 e 3.

### Métricas Coletadas

Os resultados devem ser apresentados em gráficos, analisando:

- **Tempo de Resposta (s)** no eixo Y em função do número de usuários/instâncias.
- **Requisições por Segundo (RPS)** no eixo Y em função do número de usuários/instâncias.

> **Nota:** Utilize a interface do Locust para exportar os dados em CSV e gerar as visualizações conforme os modelos sugeridos no roteiro.
