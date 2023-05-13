# HandasaimSchedule
Client for the daily updates of the Handasaim School schedule. Hosted on Vercel. Python Serverless functions provide the `/api/schedule` endpoint which returns the schedule as json (cached by backend for ~16.6 minutes). 

# Development - 
At any time the school can change the format of the schedule. In case of changes to the .xlsx file on GDrive, the config in backend/main.py needs to be changed:

In the XLSX file check if the empty cell that starts the table is correct and the cell that has the date.
Make sure that XLSX_URL hasn't changed. If it did, find the new one by going to the school site Google Sheet Schedule and set the XLSX_url to the url with the export?format=xlsx query without the id. i.e: 
https://docs.google.com/spreadsheets/d/1Eq3CQgjbVGXv0DXgsztmfax6JWu8iYH3/export?format=xlsx ~~edit#gid=153628457~~

## Fork the repo and deploy:
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FBnux256%2FHandasaimSchedule%2F&project-name=handasaim-schedule&repository-name=HandasaimSchedule)

## Local development:
To run locally with the Vercel CLI, easiest way to run the entire stack:
(Must have Python and Node installed)
```
npm install -g vercel
vercel dev
```

To run only front end locally- 
```
cd frontend
npm install
npm run dev
```

To run only api: 
```
python -m venv env

# on Linux:
source env/bin/activate
# on Windows Powershell:
venv\Scripts\Activate.ps1

pip install -r requirments
python api/index.py
```
