### Installation

1. Clone the repository:

2. Create a virtual environment and install the required packages:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Run the application using Uvicorn:

```
uvicorn main:app --reload --port 8000
```

The application should now be running at `http://localhost:8000`.

### Usage

Please obtain the cookies mentioned here from an authorized session on bard.google.com. The cookies can be used to send POST requests to the /ask endpoint along with a message in a JSON payload. It is important that the session_id, which is your \_\_Secure-1PSID cookie, is included in the request.

Example request using cURL:

```
curl -X POST "http://localhost:8000/ask" -H "accept: application/json" -H "Content-Type: application/json" -d '{"session_id":"your-session-id","message":"What is the meaning of life?"}'
```

Example request using Postman:

1. Open Postman and select the "POST" method

2. Enter the URL: `http://localhost:8000/ask`

3. Select the "Headers" tab and add a new key-value pair: `Content-Type: application/json`

4. Select the "Body" tab, choose the "raw" option, and input the following JSON payload:

   ```json
   {
     "session_id": "your-session-id",
     "message": "What is the meaning of life?"
   }
   ```

5. Click "Send" to submit the request.

You should receive a JSON response from Google Bard containing the response message.

Note: If you want to protect the `/ask` endpoint with an authentication key, you can set the `USER_AUTH_KEY` environment variable to a string value of your choice. The authentication key will be compared against the `Authorization` header of incoming requests.

## License

The code provided in this project is available for anyone to use for any purpose without any restrictions or warranties.

## Acknowledgments

- Google for creating Google Bard
- FastAPI for providing a simple and efficient web framework
