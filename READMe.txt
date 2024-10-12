Código para crear tablas en PostgreSQL

CREATE TABLE users (
    id SERIAL PRIMARY KEY,                    -- Llave primaria autoincremental
    username VARCHAR(255) NOT NULL,           -- Nombre de usuario como cadena de texto
    useremail VARCHAR(255) NOT NULL UNIQUE,   -- Email del usuario, debe ser único
    credit_card_number VARCHAR(20) NOT NULL,  -- Número de tarjeta de crédito como texto
    created_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Marca de tiempo de creación con valor por defecto de la hora actual
);
