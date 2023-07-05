# Meta
Meta is a script built in python which is used to covertly communicate over public channels using stegnography techniques. It hides a user's secret message in an image file which then can be uploaded to a subreddit specified by the user using Reddit API. The project is built keeping the idea of covert communication in mind but in the open internet. The traffic on a network can be seen as a regular internet traffic visiting popular social media website like Reddit. It can later be developed as an add-on for Data exfiltration via C2 channels.


**How to Install**

```
git clone https://github.com/ch3atk0d3/Meta.git
cd Meta
pip3 install -r requirements.txt
```



**API keys configuration**

- Get the API keys from - https://www.reddit.com/prefs/apps
- Next get the following from there - Client_ID and Client_secret
- Specify the following in the clients_secret.json before executing the script.
- Once done, save the file and continue with the steps in the usage.


```
{
    "client_id":"XXXXXXXXXXXXXX",
    "client_secret":"XXXXXXXXXXXX",
    "username":"XXXXXXXXXXXX",
    "password":"XXXXXXXXX",
    "user_agent":"pythonpraw"
}

```

**Usage**

```
# For hiding secret message in an image file

python3 meta.py -i <image file name> -o output.png

# For extracting secret message from stego file

python3 meta.py -o output.png

```

**Follow me on**

Invent your Shit - https://inventyourshit.com

Twitter - @InventShit

