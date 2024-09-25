# Getting Started 

## Generate API Key

Go to https://www.meshy.ai/discover and create an account.
Once logged in, generate an API key by visiting https://www.meshy.ai/api and clicking the Create API Key button.

## Add API Key to the Project
In the project root folder, create a file named .env if it doesn't already exist.

Add the following line to the .env file, replacing <API key> with the actual key you generated:

```
MESHY_API_KEY = "Bearer <API key>"
```
> Note: The Bearer prefix in the API key is mandatory and must be included for programmatic interactions with the Meshy API.