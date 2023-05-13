# HandasaimSchedule
## This Branch is a legacy branch which was used when the project used Github Action Cron to fetch the schedule. As of writing this, the project uses Vercel Serverless functions for the backend instead. This is more efficient and allows a better overall user experience. This branch works, to use it enable the Actions workflows in actions tab.
Client for the daily updates of the Handasaim School schedule. Using Github Actions as the backend and Svelte frontend.
Every hour a cron github actions creates a json file with the current schedule and builds the static frontend.

# Development - 
At any time the school can change the format of the schedule. In case of changes to the .xlsx file on GDrive, the config in backend/main.py needs to be changed:

In the XLSX file check if the empty cell that starts the table is correct and the cell that has the date.
Make sure that XLSX_URL hasn't changed. If it did, find the new one by going to the school site Google Sheet Schedule and set the XLSX_url to the url with the export?format=xlsx query without the id. i.e: 
https://docs.google.com/spreadsheets/d/1Eq3CQgjbVGXv0DXgsztmfax6JWu8iYH3/export?format=xlsx~~edit#gid=153628457~~

run front end locally- 
```
cd frontend
npm install
npm run dev
```

create current schedule.json locally
```
cd backend
python3 -m venv env
source env/bin/activate
pip3 install -r requirments
python3 main.py
```
