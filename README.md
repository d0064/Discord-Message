# ReactionBot - Discord Message Responder

## Overview

`bot.py` is a simple Discord bot script designed to send messages to users who react to a specific message. This can be useful for automated responses or follow-ups in a Discord server.

## Requirements

Before running the script, make sure you have the following:

- Python 3.x installed
- `discord.py` library installed (`pip install discord.py`)

## Setup

1. **Get Discord Bot Token:**
   - Create a new Discord bot on the [Discord Developer Portal](https://discord.com/developers/applications).
   - Copy the bot token.

2. **Get Guild ID, Channel ID, and Message ID:**
   - In your Discord client, right-click on the server (guild) name and click "Copy Server ID" to get the Guild ID.
   - Right-click on the desired channel and click "Copy Channel ID" to get the Channel ID.
   - Find the message you want to track, right-click on it, and click "Copy Message ID." Get the Message ID (Only the number is needed`).

3. **Configure the Script:**
   - Open `bot.py` in a text editor.
   - Replace the placeholder values in the script with your Discord bot token, Guild ID, Channel ID, and Message ID.

```python
# Replace these values with your own
TOKEN = 'your_bot_token_here'
GUILD_ID = 123456789012345678  # Replace with your Guild ID
CHANNEL_ID = 123456789012345678  # Replace with your Channel ID
MESSAGE_ID = 123456789012345678  # Replace with your Message ID
