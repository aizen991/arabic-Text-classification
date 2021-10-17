### problem
Imagine we are going to develop a question/answer application and we select Arabic native speakers because of lack of competition, then we decide to start developing a system that defines users' interests and displays the content relative to them.
Technically we should classify each content before put it in our database, after that start tracking users to define their interests,(For example by collecting users' feedbacks on the already classified content), and finally, execute the query to get the needed content.
### solution
respository contain a pre-trained model and dataset for arabic text classification project, the model will be very useful as core of a recommended system based on text,
### what's news 
- Add new class 'beauty': add 6500 articles scraped from www.sayidati.com using selenium.
- Change the number of epochs from 6 to 10 and minimize the learning rate to 0.0001.
- Add training history images.
### summary
![alt text](https://github.com/aizen991/arabic-text-classification/blob/main/Screenshot%20from%202021-10-02%2019-07-42.png)
### history
loss            |  accuracy
:-------------------------:|:-------------------------:
![alt text](https://github.com/aizen991/conclusion/blob/add-beauty-class/loss.png) | ![alt text](https://github.com/aizen991/conclusion/blob/add-beauty-class/accurancy.png)




### quick start

```
pip3 install -r requirements.txt
```
```
python3 example_prediction.py "أثبتنا أمام السيتي أننا فريق صلب دفاعيا، نعم الانتصار مهم، ولكنه مجرد بداية، ويجب مواصلة العمل بهدوء، وسعداء بالطبع بعودة الجماهير، اللاعب رقم 12، لأنهم يمثلون شغف وطاقة كرة القدم"
```


