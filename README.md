# To-Do List API 📝

A simple and efficient RESTful API for managing a to-do list. This backend service allows users to create, read, update, and delete tasks.

-----

## 🌟 Features

  * **Create a new task**: Add a new item to your to-do list.
  * **Get all tasks**: Retrieve a complete list of all tasks.
  * **Get a specific task**: Fetch a single task by its unique ID.
  * **Update a task**: Modify the content or status of an existing task.
  * **Delete a task**: Remove a task from the list.
  * **Status management**: Mark tasks as 'pending' or 'completed'.

-----

## 🛠️ Technologies Used

  * **Backend**: Node.js, Express.js
  * **Database**: MongoDB with Mongoose (or specify your database, e.g., PostgreSQL, MySQL)
  * **Testing**: Jest, Supertest (or specify your testing framework)
  * **Environment Variables**: Dotenv

-----

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have the following installed on your machine:

  * Node.js (v14 or higher)
  * npm (or yarn)
  * MongoDB (or your chosen database)

### Installation

1.  **Clone the repository**

    ```sh
    git clone https://github.com/AYUSHIPATEL123/TODOLISTAPI.git
    ```

2.  **Navigate to the project directory**

    ```sh
    cd TODOLISTAPI
    ```

3.  **Install NPM packages**

    ```sh
    npm install
    ```

4.  **Create a `.env` file** in the root of the project and add your environment variables.

    ```env
    PORT=3000
    MONGO_URI=your_mongodb_connection_string
    ```

5.  **Start the server**

    ```sh
    npm start
    ```

    The API should now be running on `http://localhost:3000`.

-----

## 📋 API Endpoints

Here are the available endpoints for this API.

| HTTP Method | Endpoint          | Description                 |
| :---------- | :---------------- | :-------------------------- |
| `GET`       | `/api/tasks`      | Get all tasks               |
| `GET`       | `/api/tasks/:id`  | Get a single task by ID     |
| `POST`      | `/api/tasks`      | Create a new task           |
| `PUT`       | `/api/tasks/:id`  | Update an existing task     |
| `DELETE`    | `/api/tasks/:id`  | Delete a task               |

### Example Request Body for `POST /api/tasks`

```json
{
  "title": "Finish the README file",
  "description": "Complete all sections of the project's README.",
  "completed": false
}
```

-----

## 🤝 How to Contribute

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

-----

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

-----

\<p align="center"\>
Developed by \<b\>AYUSHI PATEL\</b\>
\</p\>
