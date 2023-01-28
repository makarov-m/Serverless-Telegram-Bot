# Serverless Telegram Bot

### Description
Example of serverless Telegram Bot with [AWS Lambda](https://aws.amazon.com/lambda/?nc1=h_ls). The choice of AWS Lambda was quite obvious - low expenses to run and maintain my application (on-demand usage).

What does the bot do? Nothing special, just random facts about Ferdinand Magellan in Russian. If you are curious you can try it out and write the message to https://t.me/CaptainMagellan_bot.

The repository has been created for educational purposes only.

### Working Schema 

![](pics/serverless_telegram_bot.png)

### Quick setup guide

1. Copy the repository to your local machine:
    * `git clone https://github.com/{{ username }}/Serverless-Telegram-Bot.git`
2. Go to the project directory:
    * `Serverless-Telegram-Bot`
3. Create a virtual environment
    * `python3 -m venv venv`
4. Activation of the virtual environment:
    * `source venv/bin/activate`
6. Update pip to latest version:
    * `pip install --upgrade pip`
7. Install requirements
    * `pip install -r requirements.txt`
8. Then you will need to create your bot with BotFather. I found [this link](https://medium.com/@zarakhovych.alexander/create-a-telegram-bot-through-botfather-885b3faf8658) useful.
9. After that, it is necessary to set up AWS Environment for your bot. A detailed description is provided [here](https://levelup.gitconnected.com/simple-telegram-bot-with-python-and-aws-lambda-5eab1066b466).
10. When AWS environment is ready we can upload our package. I used the option with [zip file upload](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html). 
10. The last but not least step on our list is to [create a webhook](https://youtu.be/oYMgw4M4cD0) for our bot. 
