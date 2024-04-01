# Assignment4-FastAPI


# To-Do App 
In this api there is  requests for read, add, update and remove database
# Image-based API
In this api there is face analysis is done, such as age, gender and race, just send a photo file and see the result

# How to Install:
Run this command:
```
pip install -r requirements.txt
```
# How to run:

Restore database in microsoft sql server on your system(location:'database/todo.db.bak')

Run this command:
```
uvicorn sql:app --reload
uvicorn image-api:app --reload
```
