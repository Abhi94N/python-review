secretsmanager = SecretsManager("arn:aws:secretsmanager:us-west-2:860100747351:secret:RDSConfig-JMVgcU")
print(secretsmanager.db_secret)
print(type(secretsmanager.db_secret['dbname']))
print(secretsmanager.rds_connection_string)