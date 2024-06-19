# Nuevo autoencoder: 29-20-14-10-14-20-29, relu-tanh-relu-tanh-relu
encoder = Dense(20, activation='relu')(capa_entrada)
encoder = Dense(14, activation='tanh')(encoder)
encoder = Dense(10, activation='relu')(encoder)
decoder = Dense(14, activation='tanh')(encoder)
decoder = Dense(20, activation='relu')(decoder)
decoder = Dense(29, activation='relu')(decoder)

autoencoder = Model(inputs=capa_entrada, outputs=decoder)
