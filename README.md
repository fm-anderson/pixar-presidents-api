# President Memory Game API

This API serves as the backend for the [President Memory Game](https://presidents.fm-anderson.com/), a fun and interactive memory card game featuring U.S. presidents as Pixar characters. The game challenges players to match cards featuring funny U.S. Presidents avatars.

**Play the game here →** https://presidents.fm-anderson.com/

**`GET` all presidents →** https://pixar-presidents-api.vercel.app/

## Description

The President Memory Game API provides endpoints to retrieve information about U.S. presidents, which is used to populate the game's cards with avatars and details of the presidents. The API is built using Flask and supports rate limiting to prevent abuse.

## Endpoints

`GET /`: Get a list of U.S. presidents with their basic information.
```python
https://pixar-presidents-api.vercel.app/
```
`GET /<int:president_id>`: Get details about a specific U.S. president using their ID.

```python
https://pixar-presidents-api.vercel.app/<int:president_id>
```

## Contributing

If you find any issues with the API or want to contribute new features, you can either fork the repository and submit a pull request with the fixed code or create a new issue.

## A note to anyone taking the time to check this project.

I have experience developing applications with React, MongoDB, and Node. Venturing into the world of Python is quite an exciting shift for me. I'm comfortable developing APIs with Node or anything JS related, but I decided to use Python for this project due to its simplicity. It's like discovering a whole new world of coding. I can see why people love this language so much, and I hope I can get better at it with time.

Consider this space a playground of experimentation and discovery. If you're an experienced Python developer stumbling upon this project, your insights and suggestions are always welcomed! Feel free to reach out with your thoughts, ideas, or simply to say hello! We're here to learn, share, and uplift one another.

Cheers!
