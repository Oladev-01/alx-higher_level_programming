
# 0x14. JavaScript - Web Scraping
## ALX: Scripting, API, Javascript

## Learning Objectives

In this project, we will explore the following concepts:

- Why JavaScript programming is amazing
- How to manipulate JSON data
- How to use `request` and `fetch` API
- How to read and write a file using the `fs` module
- And other related topics

## Requirements

- All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
- Your code should use the `ps` (semistandard) style guide
- You must use `request` for making HTTP requests
- You must use `fs` for file system operations
- The length of your files will be tested using `wc`

## Project Tasks

### Task 0: Read me
- Write a script that reads and prints the content of a file.
- The first argument is the file path.
- The content of the file must be read in `utf-8`.
- If an error occurred during the reading, print the error object.

### Task 1: Write me
- Write a script that writes a string to a file.
- The first argument is the file path.
- The second argument is the string to write.
- The content of the file must be written in `utf-8`.
- If an error occurred during the writing, print the error object.

### Task 2: Status code
- Write a script that display the status code of a `GET` request.
- The first argument is the URL to request (GET).
- The status code must be printed like this: `code: <status code>`.
- You must use the module `request`.

### Task 3: Star wars movie title
- Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
- The first argument is the episode number.
- You must use the Star Wars API with the endpoint `https://swapi-api.hbtn.io/api/films/:id`.
- You must use the module `request`.

### Task 4: Star wars Wedge Antilles
- Write a script that prints the number of movies where the character “Wedge Antilles” is present.
- The character ID is `18` - use the Star Wars API `https://swapi-api.hbtn.io/api/people/18`.
- You must use the module `request`.

### Task 5: Loripsum
- Write a script that gets the contents of a webpage and stores it in a file.
- The first argument is the URL to request.
- The second argument is the file path to store the body response.
- The file must be encoded in `utf-8`.
- You must use the module `request`.

### Task 6: How many completed?
- Write a script that computes the number of tasks completed by user id.
- The first argument is the API URL.
- Only print users with completed task.

### Task 7: Who was playing in this movie?
- Write a script that prints all characters of a Star Wars movie:
- The first argument is the Movie ID - example: `3` = “Return of the Jedi”.
- Display one character name by line.
- You must use the Star Wars API.
- You must use the module `request`.

### Task 8: Right order
- Write a script that prints all characters of a Star Wars movie in the right order:
- The first argument is the Movie ID - example: `3` = “Return of the Jedi”.
- Display one character name by line.
- You must use the Star Wars API.
- You must use the module `request`.

## Usage

To run any of the scripts, use the following command format:

```bash
node <script_name> <arguments>
```

For example, to run the first task:

```bash
node 0-readme.js <file_path>
```

## Author

- MOJIBOLA OLALEKAN

---

