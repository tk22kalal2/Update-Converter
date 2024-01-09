from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BASE_SITE

START_MESSAGE = '''😎**Hello, {}

I Am %s , Bulk Link Converter Bot. I Can Convert Links Directly From Your zxlink.in Account,

Just Send me Any Post with Other Links. I will Convert Those Links Using Your API and Send them Back To You

1. Go To 👉 https://zxlink.in/member/tools/api

2. Than Copy API Key

3. Than Type /shortener_api than give a single space and than paste your API Key (see example to understand more...)
/shortener_api(space)API Key
(See Example.👇)
Example: `/shortener_api cbd63775f798fe0e58c67a56e6ce8b70c495cda4`

💁‍♀️ Hit 👉 /help To Get Help.

➕ Hit 👉 /footer To Get Help About Adding your Custom Footer to bot.

➕ Hit 👉 /header To Get Help About Adding your Custom Footer to bot.**

If You Want Any **Other Shortner** Link Converter Bot Instead Of zxlink.in than **contact** at 👉 @J_shree_ram (all **shortners** support available.)
''' % BASE_SITE

HELP_MESSAGE = '''
Hey! My name is {firstname}. I am a Link Shortener Bot, here to make your Work Easy and Help you to Earn more

I have lots of handy features, such as 

- [Hyperlink](https://t.me/{username})
- Buttons convert support
- Header and Footer Text support
- Replace Username
- Banner Image

Helpful commands:

- /start: Starts me! You've probably already used this.
- /help: Sends this message; I'll tell you more about myself!

If you have any bugs or questions on how to use me, contact to @J_shree_ram.

Below are some features I provide'''


ABOUT_TEXT = """
**My Details:**

`🤖 Name:` ** {} **
    
`📝 Language:` [Python 3](https://www.python.org/)
`🧰 Framework:` [Pyrogram](https://github.com/pyrogram/pyrogram)
`👨‍💻 Developer:` [Dev](t.me/J_shree_ram)
`📢 Support:` {}
"""


HELP_REPLY_MARKUP = InlineKeyboardMarkup([

    [
        InlineKeyboardButton('Home', callback_data='start_command')
    ]
])


ABOUT_REPLY_MARKUP = InlineKeyboardMarkup([[InlineKeyboardButton('Home', callback_data='start_command'), InlineKeyboardButton('Help', callback_data='help_command')], [InlineKeyboardButton('Close', callback_data='delete')]])


START_MESSAGE_REPLY_MARKUP = InlineKeyboardMarkup([[InlineKeyboardButton('↗️Connect', url=f'https://{BASE_SITE}/member/tools/api'), InlineKeyboardButton('⚙️Help', callback_data='help_command')], [InlineKeyboardButton('🧑‍💻About', callback_data='about_command'), InlineKeyboardButton('❌Close', callback_data='delete')]])



BACK_REPLY_MARKUP = InlineKeyboardMarkup([[InlineKeyboardButton('Back', callback_data='start_command')]])


USER_ABOUT_MESSAGE = """
- Shortener Website: {base_site}

- {base_site} API: {shortener_api}

- Username: @{username}

- Header Text: 
{header_text}

- Footer Text: 
{footer_text}

- Banner Image: {banner_image}
"""


SHORTENER_API_MESSAGE = """To add or update your Shortner Website API, `/shortener_api api`
            
Ex: `/shortener_api xxx`
            
Shortener API of your preferred shortener API.

Current Website: {base_site}

Current Shortener API: `{shortener_api}`"""

HEADER_MESSAGE = """Reply to the Header Text You Want

This Text will be added to the top of every message caption or text

To Remove Header Text: `/header remove`"""

FOOTER_MESSAGE = """Reply to the Footer Text You Want

This Text will be added to the bottom of every message caption or text

To Remove Footer Text: `/footer remove`"""

USERNAME_TEXT = """Current Username: {username}

Usage: `/username your_username`

For just removing the username from the post: 
`/username none`

This username will be automatically replaced with other usernames in the post

To remove current username, `/username remove`"""

BANNER_IMAGE = """Current Banner Image URL: {banner_image}

Usage: `/banner_image image_url`

This image will be automatically replaced with other images in the post

To remove custom image, `/banner_image remove`

Eg: `/banner_image https://www.nicepng.com/png/detail/436-4369539_movie-logo-film.png`"""

