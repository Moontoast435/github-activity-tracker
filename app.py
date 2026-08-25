# github user activity
import requests

# set up the CLI to request username

program_active = True

github_api_url = 'https://api.github.com/users/'
while(program_active):
    username_input = input("Please enter the github user for whom you want to see the activity. OR - type exit to exit the program: ")

    if (username_input.upper() != "EXIT"):
        try:
            req = requests.get(github_api_url + username_input + '/events')

            if (req.status_code == '403'):
                print("403: Forbidden")
                continue

            if (req.status_code == '503'):
                print("503: Service unavailable")
                continue

            if (req.status_code == '304'):
                print("304: Not modified")
                continue

            json = req.json()

            for event in json:
                id = event["id"]
                type = event["type"]

                actor_login = event["actor"]["login"]
                actor_url = event["actor"]["url"]

                repo_name = event["repo"]["name"]

                created_at = event["created_at"]
                
                print(f'Event ID: {id} \n Event Type: {type} \n Actor Login: {actor_login} \n Actor URL: {actor_url} \n Repo Name: {repo_name} \n Created At: {created_at} ')      
        except:
            print("could not get github activity")
    else:
        program_active = False


# TODO options to go back to see another user's activity or end the program
