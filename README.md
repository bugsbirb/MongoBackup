# 🍃 Mongo DB Backup
> Repeatedly backs up a database in a choosen interval of time to Dropbox!


## .env
```env
mongo_uri=

# For db_names you have to list it like pizza,chicken,donken or it'll break :3
db_names=

dropbox_key=
interval=
retry_time=
keep_files_locally= True
# [keep_files_locally] This is if you want to keep the files on the workspace (This will still send to workspace)
dropbox_app_key=
dropbox_app_secret=

# For the refresh token follow this tutorial: https://github.com/FranklinThaker/Dropbox-API-Uninterrupted-Access
dropbox_refresh_token= ""



```

## Dropbox API Key [TUT]
### 1. Create an app in your Dropbox account


  > Go to https://www.dropbox.com/developers/apps/create
  > Authorize, if you weren’t.
  > Choose Scoped access on the first step.
  > Choose Full Dropbox access on the second.
  > Give your app a name. That name will become a folder in your Dropbox account.
  > Push ‘Create app’ button.
### 2. Set permissions


 > You’ll be presented with your app’s settings.
 > Go to the Permissions tab.
 > Set permission as on the screenshot. Read access is required, write access is required if in your workflow you need to create or change files.
 > Press "Submit" at the bottom.

### 3. Generate access token
> Scroll down to ‘OAuth 2’ block
> Set access token expiration to "No expiration". 
> Press ‘Generate’ button near ‘Generated access token’ text.
> After the token is generated you’ll see a string of letters and numbers, which looks something like this:
