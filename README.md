### problem
Imagine we are going to develop a question/answer application.  We selected Arab native speakers because of lack of competition. Then, we decide to start developing a system that defines users' interests and displays the content relative to them.
Technically we should classify each question/answer before put it in our database, then start tracking users to define their interests, finally execute the query to get needed content.
### solution
respository contain a pretained model and dataset for arabic text classification project, the model will be very useful as core of a recommended system based on text,
### what's news 
add new class 'beauty' 
### summary
![alt text](https://github.com/aizen991/arabic-text-classification/blob/main/Screenshot%20from%202021-10-02%2019-07-42.png)
### history
loss            |  accuracy
:-------------------------:|:-------------------------:
![alt text](https://github.com/aizen991/conclusion/blob/add-beauty-class/Screenshot%20from%202021-10-16%2013-39-36.png) | ![alt text](https://github.com/aizen991/conclusion/blob/add-beauty-class/Screenshot%20from%202021-10-16%2013-45-55.png)




### quick start

```
pip3 install -r requirements.txt
```
```
python3 example_prediction.py
```


