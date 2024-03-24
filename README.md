# MailReader Sever 

The project is devided into two sections, the Mialreader server, which serves you data gotten from google through googles gmail api,

* You need need to replace the contents of the credentials.json file with your own credentials that you got from google, Google gives you a credentail that you can use to test apps, without this credential the mail server won't run
* The mails server also allows you to send text and get an audio file back which you can use
* Note: The server is not authenticated to be able to handle secure web traffic, at best this application should be used on your local network and not published unless modified to be able to handle secure web traffic among other things
* 
# Front end application

The Front end application basically shows you how you can combine the two functionalities of the Mailserver to get a simple application working, the Front end uses HTML, CSS and JS 


# What I Learned

* I learned how to use googles Gmail api to request for emails data
* I learned how to use flask to start a server
* I learned how path traversal in python works
* I usually use the fetch function in JavaScript for API calls but I was able to learn about another function that JavaScript offer, which is XMLHttpRequest
* I also worked a bit with pythons pyttsx3 to turn the text to audio files that can be sent to the client
* I learned abit about how audio files can handled using arrayBuffer function in XMLHttpRequest to recieve the file as an arrayBuffer those making handling the file file easier
