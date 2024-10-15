# Streamlit Price Calculator

This is a simple price calculator that calculates the price of a product based on the quantity and the price of the product.

The app is built using Streamlit and requires a Bearer token to access the app.

There is one docker container that runs the Steamlit app and another container that runs Nginx as a reverse proxy to the Streamlit app. The Nginx is the only container that is exposed to the outside world.

## How to run the app

Start the docker containers using the following command:

```bash
docker-compose up
```

Then visit `http://localhost:8080` to access the app.
