const express = require('express');
const path = require('path');
const app = express();
const mssql = require('mssql');

// change timeout to 10 minutes

const config = {
  "user": 'sa',
  "password": 'iamehmetozdemir',
  "server": 'IAMEHMETOZDEMIR\\SQLEXPRESS',
  "database": 'Formula',
  "port": 1433, 
  "dialect": "mssql",
  "dialectOptions": {
      "instanceName": "SQLEXPRESS"
  },
  "options": {
    "trustServerCertificate": true,
  } 
};

mssql.connect(config, function (err) {
  if (err) console.log(err);
  else console.log('Connected to SQL Server');
});




app.use('/constructor', require('./Routers/Constructor'));
app.use('/driver', require('./Routers/Driver'));
app.use('/race', require('./Routers/Race'));
app.use('/season', require('./Routers/Season'));



    app.listen(3000, () => {
    console.log('Server started on http://localhost:3000');
  });