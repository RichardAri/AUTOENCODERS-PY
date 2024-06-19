from sklearn.model_selection import train_test_split

#Dividimos el conjunto de datos en entrenamiento y prueba
X_train, X_test = train_test_split(datos, test_size=0.2, random_state=42)

#Dividimos el conjunto de entrenamiento en entrenamiento y validacion
X_train, X_val = train_test_split(X_train, test_size=0.2, random_state=42)

#Separamos las caracteristicas y las etiquetas
Y_train = X_train['Class']
X_train = X_train.drop(['Class'], axis=1)
X_train = X_train.values

Y_val = X_val['Class']
X_val = X_val.drop(['Class'], axis=1)
X_val = X_val.values

Y_test = X_test['Class']
X_test = X_test.drop(['Class'], axis=1)
X_test = X_test.values

#Mostramos las dimensiones de los conjuntos de datos
print("Entrenamiento:", X_train.shape, Y_train.shape)
print("Validación:", X_val.shape, Y_val.shape)
print("Prueba:", X_test.shape, Y_test.shape)
