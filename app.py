# github user activity
import requests

# set up the CLI to request username

program_active = True

github_api_url = 'https://api.github.com/users/'
while(program_active):
    search_type = input("What do you want to do? View user events, or user info? type events or info. OR type exit to stop the program: ")
    
    if (search_type.upper() == "EXIT"):
        program_active = False
        continue

    username_input = input("Please enter the github user. OR - type exit to exit the program: ")

    if (search_type.upper() == "EVENTS"):
        try:
            req = requests.get(f"https://api.github.com/users/{username_input}/events")

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

        continue

    if (search_type.upper() == "INFO"):
        try:
            print(f"{github_api_url}{username_input}")
            req = requests.get(f"https://api.github.com/users/{username_input}")

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
             
            id = json["id"]
            url = json["url"]
            user_name = json["name"]
            user_company = json["company"]
            user_location = json["location"]
            user_bio = json["bio"]
            user_public_repos = json["public_repos"]
            user_followers = json["followers"]

            created_at = json["created_at"]
                
            print(f'User ID: {id} \n URL: {url} \n Username: {user_name} \n Company: {user_company} \n Location: {user_location} \n Bio: {user_bio} \n Public repos: {user_public_repos} \n Followers: {user_followers} \n Created at: {created_at} ')      
        except:
            print("could not get github user info")

        continue


