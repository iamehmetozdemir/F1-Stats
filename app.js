const express = require('express');
const path = require('path');
const app = express();
const sqlite3 = require('sqlite3').verbose();






app.use('/constructor', require('./Routers/Constructor'));
app.use('/driver', require('./Routers/Driver'));
app.use('/race', require('./Routers/Race'));
app.use('/season', require('./Routers/Season'));

app.get('/drivers', (req, res) => {
    const sql = 'SELECT * FROM drivers';
    const db = new sqlite3.Database('./Source/Formula1.sqlite');
    db.all(sql, [], (err, rows) => {
      if (err) {
        throw err;
      }
      res.json(rows);
    });
});
app.get('/results', (req, res) => {
    const sql = 'SELECT * FROM results';
    const db = new sqlite3.Database('./Source/Formula1.sqlite');
    db.all(sql, [], (err, rows) => {
      if (err) {
        throw err;
      }
      res.json(rows);
    })});


app.listen(8000, () => {
    console.log("Server is running...");
  });