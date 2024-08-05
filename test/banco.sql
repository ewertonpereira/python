CREATE TABLE tipo_transacao(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(20) NOT NULL
    );
    
INSERT INTO tipo_transacao(nome) VALUES ('receita'),('gastos'),('investimentos');

CREATE TABLE categorias(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    tipo_transacao_id INT,
    FOREIGN KEY (tipo_transacao_id) REFERENCES tipo_transacao(id)
);

INSERT INTO categorias (nome, tipo_transacao_id) VALUES('agua', 2),
INSERT INTO categorias (nome, tipo_transacao_id) VALUES('mercado', 2),
INSERT INTO categorias (nome, tipo_transacao_id) VALUES('transporte', ),
INSERT INTO categorias (nome, tipo_transacao_id) VALUES('', ),
INSERT INTO categorias (nome, tipo_transacao_id) VALUES('', ),