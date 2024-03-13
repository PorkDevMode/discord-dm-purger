# discord-dm-purger
A dm purging tool to get rid of all messages for a specific user.

# Guide (EXE BUILD)

* Get latest build from githubs releases page and download the exe
* Run the exe (no python required)
* Enter your discord token, scroll down to see how to get it
* Enter the persons dms you want to purge, and copy their userid into the program
* Enjoy

# Guide (Python Build)

* Get the latest version of python installed
* Run this command in a command prompt "pip install discord discord.py-self"
* Download main.py
* Run main.py
* Enter your discord token, scroll down to see how to get it
* Enter the persons dms you want to purge, and copy their userid into the program
* Enjoy

# Guide (Discord Token Retrieval)

You can get your discord token by pressing ctrl-shift-i in the discord app or website, going to console and copy / pasting this:

(
    webpackChunkdiscord_app.push(
        [
            [''],
            {},
            e => {
                m=[];
                for(let c in e.c)
                    m.push(e.c[c])
            }
        ]
    ),
    m
).find(
    m => m?.exports?.default?.getToken !== void 0
).exports.default.getToken()
