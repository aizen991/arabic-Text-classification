### problem
Imagine we are going to develop a question/answer application.  We selected Arab native speakers because of lack of competition. Then, we decide to start developing a system that defines users' interests and displays the content relative to them.
Technically we should classify each question/answer before put it in our database. Then start tracking users to define their interests (for example by collecting their feeds about a question/answer that is already classified) and finally execute the query to get needed content.
### solution
respository contain a pretained model and dataset for arabic text classification project, the model will be  useful as core of a recommended system based on text,
### what's news 
- Add "gaming" cclass : add 6500 articles scraped from https://www.vga4a.com/ using selenium.
- Change the number of epochs from 6 to 12 and minimize the learning rate to 0.0001.
- Add training history images.

### classes
['Beauty', 'Culture', 'Finance', 'Gaming', 'Medical', 'Politics', 'Religion', 'Sports', 'Tech']
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


