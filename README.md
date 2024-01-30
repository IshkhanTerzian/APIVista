# APIVista

## Overview

APIVista is a gaming database API developed by Ishkhan Terzian for tracking and analyzing trends in video game sales, pricing, and information across PlayStation and Xbox platforms.

## Who?

APIVista is designed and maintained by Ishkhan Terzian. Connect with me on [GitHub](https://github.com/IshkhanTerzian).

## What?

APIVista provides a robust API to access and manage data related to video games. It includes information about game titles, release dates, genres, developers, pricing, and sales. The API is designed to offer insights into gaming trends and facilitate trend analysis.

## Key Features

Comprehensive Data Access detailed information about video games, including sales, pricing, and more.
Platform Support Track trends across multiple platforms, including PlayStation and Xbox.
User-Friendly Easy-to-use API endpoints for seamless integration into applications and services.

## UML Diagram
![UML Diagram](https://github.com/IshkhanTerzian/APIVista/blob/master/APIVistoTables.png)

## Framework and Dependencies

APIVista is built using the Flask framework and utilizes SQLAlchemy for database operations and its ORM (Object-Relational Mapping) functionality. The application uses PostgreSQL as its database.


## Getting Started

### Prerequisites

- Python 3.x
- Flask
- SQLAlchemy
- PostgreSQL

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/IshkhanTerzian/APIVista.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your PostgreSQL database and update the `DATABASE_URL` in `.env` file.

### Running the Application

1. Create a `.flaskenv` file and set the following environment variables:

    ```dotenv
    FLASK_APP=app.py
    FLASK_ENV=development
    ```

2. Run the Flask application:

    ```bash
    flask run
    ```
   

## API Endpoints

### This is a general overview of the all the available endpoints for APIVista,
## For more comprehensive look, please take a look at the API documentation posted below



### Developer Routes

```htp
GET /api/developer                     -> Get all developers.
GET /api/developer/{developer_id}      -> Get a single developer by ID.
POST /api/developer                    -> Add a new developer.
PATCH /api/developer/{developer_id}    -> Update a developer by ID.
DELETE /api/developer/{developer_id}   -> Delete a developer by ID.

```

### Genre Routes

```http
GET /api/genre                   -> Get all genres.
GET /api/genre/{genre_id}        -> Get a single genre by ID.
POST /api/genre                  -> Add a new genre.
PATCH /api/genre/{genre_id}      -> Update a genre by ID.
DELETE /api/genre/{genre_id}     -> Delete a genre by ID.
```

### Platforms

```http
GET /api/platform                      -> Get all platforms.
GET /api/platform/{platform_id}        -> Get a single platform by ID.
POST /api/platform                     -> Add a new platform.
PATCH /api/platform/{platform_id}      -> Update a platform by ID.
DELETE /api/platform/{platform_id}     -> Delete a platform by ID.
```


### Games

```http
GET /api/game                    -> Get all games.
GET /api/game/{game_id}          -> Get a single game by ID.
POST /api/game                   -> Add a new game.
PATCH /api/game/{game_id}        -> Update a game by ID.
DELETE /api/game/{game_id}       -> Delete a game by ID.
```

### Pricing Routes

```http
GET /api/pricing                    -> Get all pricing information.
GET /api/pricing/{game_id}          -> Get pricing information for a single game.
POST /api/pricing/{game_id}         -> Add pricing information for a game.
PATCH /api/pricing/{game_id}        -> Update pricing information for a game.
DELETE /api/pricing/{game_id}       -> Delete pricing information for a game.
```

### Sales Routes
```http
GET /api/sales                  -> Getting all Sales information
GET /api/sales/{game_id}        -> Get Sales for a single Game
POST /api/sales/{game_id}       -> Add Sales for a Game
PATCH /api/sales/{game_id}      -> Update Sales for a Game
DELETE /api/sales/{game_id}     -> Delete Sales for a Game at a specific Year
```