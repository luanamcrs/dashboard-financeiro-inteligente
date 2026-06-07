CREATE TABLE IF NOT EXISTS transactions (
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    descricao VARCHAR(255),
    categoria VARCHAR(100),
    valor NUMERIC(10,2) NOT NULL
);