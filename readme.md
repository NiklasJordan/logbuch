# 📓 Logbuch – simple, email-based static site generator

Logbuch is a stupid simple static site generator feeded by old-fashion emails.

![Screenshot of Logbuch](/screenshot.png)

The entire idea behind Logbuch is to have a stupid simple entry to post new content and the advantages of a static pages. Without all the complexity of caring about updates or managing content through the backend.

Abilities and Features:

* Completely platform independently for hosting and email.
* Simple HTML template based on Jinja2.
* Just <100 lines of Python.
* Compiles down to purely static files; JavaScript-free.

| :point_up: DISCLAIMER                                                                       |
|:--------------------------------------------------------------------------------------------|
| This project was created due to my own needs. I do not guarantee that it is free of bugs. The script is just <100 lines of dirty (I mean really dirty!) Python code and I recommend you to take a look in there yourself before you use it for yourself.              |

## The story behind

Often content management systems are very complex, both in development and in management and maintenance. I love technology without a lot of bells and whistles and was looking for a way to start a photo blog very simply and without platform dependency. 

My plan: I just send an email with my post somewhere and the pictures in the attachment. Magic happens and bang... static page is generated. Unfortunately, I have not found such a thing and therefore now developed this for myself. Logbuch is simple, comprehensible and platform independent.

## How it works?

This is the very simple procedure:
1. Send an email with defined subject and your post content to a defined email adress.
2. The script is looking automatically for new emails in the inbox with the defines subject.
3. If there is a new email, the script extracts the content, saves the attachements and
4. generate the static files including the new post and save them into the /site/ directory.

Pretty simple, right?!

## Get started

### Installation

Just copy the files on your server:

´´´
$ git clone https://github.com/NiklasJordan/Logbuch.git
´´´

### Configuration

Rename the ´config-copy.json´ to ´config.json´ and fill out and customize it with your data.

### Add a cronjob (optional)

To achieve a fully automated process, I recommend creating a cronjob that runs site.py at regular intervals to scan the inbox for new posts and regenerate the page if necessary.

That's all. Now you can start with your postings.

## Usage

Just send an email with the defined subject from your config.json with your content to your defined target email adress. If you added a cronjob, you have nothing else to do. Otherwise, you have to run the ´site.py´.

### Use a iOS shortcut (optional)

I'm using a simple iOS shortcut to generate and send the emails. This let me select one or more photos and open a modal for the text, afterwards it's sends automatically to the right adress and with the right subject.

## Next steps

I would like to implement the following features:

* [ ] Add infinite scrolling for better performance
* [ ] Compress the photos before saving
* [ ] Add a RSS feed

## License

Copyright (c) 2022 Niklas Jordan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
