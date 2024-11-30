
-- Crear la tabla User
CREATE TABLE IF NOT EXISTS User (
    id BINARY(16) PRIMARY KEY,                     -- Utilizamos BINARY(16) para almacenar UUIDs de manera más eficiente
    first_name VARCHAR(100) NOT NULL,              -- Ajustar el tamaño máximo según la necesidad
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,            -- Ajustar el tamaño máximo según la necesidad
    password VARCHAR(100) NOT NULL,                -- Asegúrate de que esté hasheada y ajusta el tamaño necesario
    is_admin TINYINT(1) DEFAULT 0,                 -- Utilizando TINYINT(1) para compatibilidad más amplia
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Cambiamos a TIMESTAMP
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Crear la tabla Place
CREATE TABLE IF NOT EXISTS Place (
    id BINARY(16) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    owner_id BINARY(16),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (owner_id) REFERENCES User(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Crear la tabla Review
CREATE TABLE IF NOT EXISTS Review (
    id BINARY(16) PRIMARY KEY,
    text TEXT NOT NULL,
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5), -- Aseguramos que la calificación esté entre 1 y 5
    user_id BINARY(16),
    place_id BINARY(16),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE,
    FOREIGN KEY (place_id) REFERENCES Place(id) ON DELETE CASCADE,
    UNIQUE (user_id, place_id) -- Asegura que un usuario no pueda dejar múltiples reseñas en el mismo lugar
) ENGINE=InnoDB;

-- Crear la tabla Amenity
CREATE TABLE IF NOT EXISTS Amenity (
    id BINARY(16) PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;
