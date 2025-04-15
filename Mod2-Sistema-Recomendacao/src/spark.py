from pyspark.sql import SparkSession

# Criar uma SparkSession
spark = SparkSession.builder \
    .appName("Teste Spark Básico") \
    .master("local[*]") \
    .getOrCreate()

# Criar um DataFrame de exemplo
data = [
    ("João", 28),
    ("Maria", 35),
    ("Pedro", 23),
    ("Ana", 40)
]
colunas = ["Nome", "Idade"]
df = spark.createDataFrame(data, colunas)

# Mostrar o DataFrame original
print("📋 DataFrame Original:")
df.show()

# Filtrar apenas pessoas com idade > 30
df_filtrado = df.filter(df.Idade > 30)

# Mostrar resultado do filtro
print("🔍 Pessoas com idade maior que 30:")
df_filtrado.show()

# Encerrar sessão
spark.stop()
