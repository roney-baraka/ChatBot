import requests
import json

BACKEND_URL="https://kl296qff-8000.uks1.devtunnels.ms/docs"

def chat(user_input, data, session_id=None)
    """
    Sends a user input to a chat API and returns the response.

    Args:
        user_input (str): The user's input.
        data(str): The data source. 
        session_id (str, optional):session identifier. Defaults to none 
    
    Returns:
        tuple: A tuple containing the response answer and the updated session_id
    """
    #API endpoint for chat 
    url = BACKEND_URL+"/chat"

    # print input for debugging 
    print("user", user_input)
    print ("data", data)
    print("session_id", session_id)

    #Prepare payload for the API request 
    if session_id is None:
        payload = json.dumps({"user_input": user_input, "data_source":data})
    else:
        payload = json.dumps(
            {"user_input": user_input, "data_source":data}
        )

        #Set header for the API request 
        headers ={
            "accept": "application/json"
            "Content-Type": "application/json",
        }
        
        #   Make a POST request to the chat API 
        response = requests.request("POST", url, headers=headers, data=payload)

        #Print the API response for debugging 
        print(response.json())

        #Check if the request was successful (status code 200)
        if response.status_code == 200:
            # return the response answer and updated session_id
            return response.json(["response"]["answer"], response.json()["session_id"])
        
def upload_file(file_path):
     #print file path for debugging 
     print ("path", file_path)

     #Extract the filename from the file path 
     filename =  file_path.split("\\")[-1]

     #API endpoint for file upload 
     url = BACKEND_URL+"/uploadFile"
     print(url)

     #Prepare payload for the file upload request 
     payload = {}
     file = [
         (
             "data_file",
             (filename, open(file_path, "rb"), "application/pdf")
         )
     ]