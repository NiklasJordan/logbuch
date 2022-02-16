import jinja2
from datetime import datetime
import csv
import json
import imaplib
import email
from email.utils import parsedate_tz, mktime_tz, formatdate
import time
import os
import dateutil.parser

with open('./config.json', 'r') as f:
    config = json.load(f)
    title = str(config['title'])
    host = str(config['host'])
    user = str(config['user'])
    password = str(config['pass'])
    from_mail = str(config['from'])
    subject = str(config['subject'])

# Connect to inbox
imap_server = imaplib.IMAP4_SSL(host=host)
imap_server.login(user, password)
imap_server.select()  # Default is `INBOX`    
    
entries = []
update = datetime.now().strftime("%d/%m/%Y %H:%M")
outputdir = './site/'
outputfile = 'index.html'

str_from = '(FROM "'+from_mail+'")'
str_subject = '(SUBJECT "'+subject+'")'

def getEntries():
    # Find all new emails in inbox
    _, message_numbers_raw = imap_server.search(None, str_from, str_subject, 'UnSeen')
    for message_number in message_numbers_raw[0].split():
        _, msg = imap_server.fetch(message_number, '(RFC822)')

        # Get data from email
        message = email.message_from_bytes(msg[0][1])

        date_raw = message["date"]
        text = message.get_payload()[0].get_payload().replace('=\r\n', '')

        # Format date into format
        date_formatted = dateutil.parser.parse(date_raw)
        date = date_formatted.strftime('%Y/%m/%d')

        # Get images and save them
        if message.is_multipart():
            images = []
            for part in message.walk():
                ctype = part.get_content_type()
                if ctype in ['image/jpeg', 'image/png']:
                    open(os.path.dirname(__file__)+'/entries/'+part.get_filename(), 'wb').write(part.get_payload(decode=True))
                    images.append(part.get_filename())

        post = []
        post.append(date)
        post.append(text)
        post.append('|'.join(images))

        print(post)

        with open(os.path.dirname(__file__)+'/entries/entries.txt', 'a') as f:
            string = str('|'.join(post))
            f.writelines(string+'\n')
            
        return True

def buildSite():           
    # opening the CSV file
    with open('entries/entries.txt', mode ='r') as file:

      # reading the CSV file
      entriesFile = csv.reader(file, delimiter='|')

      # displaying the contents of the CSV file
      for line in entriesFile:
            entries.append(line)

    # Generate HTML page        
    subs = jinja2.Environment( 
                  loader=jinja2.FileSystemLoader('./')      
                  ).get_template('template.html').render(title=title, update=update, entries=entries) 

    # lets write the substitution to a file
    with open(outputdir+outputfile,'w') as f: f.write(subs)
    
    print('Updated.')
    
if getEntries() is True:
    buildSite()
else:
    print('No new entries.')