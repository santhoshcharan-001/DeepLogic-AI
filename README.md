# DeepLogic-AI

According to the problem statement, we have to enable the new users to get registered. 
After registering, users can get logged into the application and then they will have two options such as: 
1. Upload a pdf to extract the text in it.
2. Check the history of the user about the pdf's uploaded by them.

Initially, to implement User Authentication, I have used django's inbuilt user authentication. And
To then to extract the text from the pdf, we have many modules in python to extract the text, but those are not feasible directly in our case.
Because, a pdf everytime not only consists of text, but also sometimes consists of photos having text. 
So, i thought of an idea which will be feasible in this case i.e 
### Firstly, convert the pdf pages into images using poppler module which helps us convert the pdf pages to images.
### And then, to extract the text from the image, I have utilised the module Pytesseract which helps us to extract text from the images.
