# HandasaimSchedule
Client for the Handasaim School schedule. Using serverless functions and Svelte


# Development - 
run front end - 
```
cd frontend
npm install
npm run dev
```
start serverless function localy-
```
cd api
python3 -m venv env
source env/bin/activate
pip3 install -r requirments
functions_framework --target get_req --port 8000 --debug
```
