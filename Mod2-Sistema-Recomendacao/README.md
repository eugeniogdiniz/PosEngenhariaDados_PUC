
# 🔥 Projeto Spark com Docker (Standalone)

Este projeto configura um ambiente Apache Spark com Docker, utilizando os contêineres da Bitnami para rodar um script Python (`mongo_spark.py`) com PySpark.

---

## 📁 Estrutura do Projeto

```
Mod2-Sistema-Recomendacao/
│
├── docker-compose.yml
├── src/
│   └── mongo_spark.py
└── README.md
```

---

## ⚙️ Requisitos

- Docker
- Docker Compose

---

## 🐳 Subindo o Spark com Docker

### 1. Clone o repositório ou acesse a pasta do projeto

```bash
cd Mod2-Sistema-Recomendacao
```

### 2. Verifique se seu `mongo_spark.py` está no diretório `src/`

O caminho completo deve ser:

```
./src/mongo_spark.py
```

### 3. Arquivo `docker-compose.yml`

```yaml
services:
  spark-master:
    image: bitnami/spark:latest
    container_name: spark-master
    environment:
      - SPARK_MODE=master
    ports:
      - "7077:7077"
      - "9090:8080"
    volumes:
      - ./src:/opt/bitnami/spark/scripts

  spark-worker:
    image: bitnami/spark:latest
    container_name: spark-worker
    environment:
      - SPARK_MODE=worker
      - SPARK_MASTER_URL=spark://spark-master:7077
    depends_on:
      - spark-master
    volumes:
      - ./src:/opt/bitnami/spark/scripts
```

---

### 4. Subindo os contêineres

```bash
docker compose up -d
```

---

## 🚀 Executando seu script PySpark

Com os contêineres rodando, execute o script `mongo_spark.py` no container do Spark Master:

```bash
docker exec -it spark-master spark-submit /opt/bitnami/spark/scripts/mongo_spark.py
```

---

## ✅ Verificando o painel do Spark

Acesse a interface web do Spark no navegador:

```
http://localhost:9090
```

---

## 📌 Dicas

- Use `docker compose logs -f` para visualizar os logs.
- Use `docker compose down` para encerrar os contêineres.
- Adicione bibliotecas extras no Dockerfile se necessário.

---

## 🧪 Exemplo de Script PySpark (Opcional)

```python
# mongo_spark.py
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("TestSpark").getOrCreate()

data = [("João", 30), ("Maria", 25), ("José", 28)]
df = spark.createDataFrame(data, ["nome", "idade"])

df.show()
```

---

## ✨ Resultado Esperado

```bash
+-----+-----+
| nome|idade|
+-----+-----+
| João|   30|
|Maria|   25|
| José|   28|
+-----+-----+
```

---

## 🧹 Encerrando o ambiente

```bash
docker compose down
```

---

Feito com 💡 e Docker.
