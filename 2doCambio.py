encoder = Dense(20, activation='relu')(capa_entrada)
encoder = Dense(15, activation='relu')(encoder)
encoder = Dense(10, activation='relu')(encoder)

decoder = Dense(15, activation='relu')(encoder)
decoder = Dense(20, activation='relu')(decoder)
decoder = Dense(29, activation='sigmoid')(decoder)
