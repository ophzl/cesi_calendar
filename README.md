# CESI Calendar

This project is currently in development. Please consider it's not over yet.

## How to start

First, you need to link your google api oauth' credentials to the script by placing your credentials.json file inside 
**api** folder. According to the Google oauth' documentation, it should look like this:
```
{"web": 
    {
        "client_id":"your-client-id",
        "project_id":"your-project-id",
        "auth_uri":"https://accounts.google.com/o/oauth2/auth",
        "token_uri":"https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
        "client_secret":"your-client-secret",
        "redirect_uris":["your-redirect-uri"]
    }
}
```
Then, just add your data is **Resources** folder, just as it looks like in **Resources/fakedata.json**

## Start project
Launch project by typing:
```
python main.py Resources/name_of_your_data.json
```
Please replace *name_of_your_data.json* by your data file name.

For example, you can start project with fakedata, with this command:
```
python main.py Resources/fakedata.json
```

<footer>
Enjoy retrieving your data in your Google Calendar !
</footer>