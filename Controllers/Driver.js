const sqlite3 = require('sqlite3').verbose();

exports.getAllDrivers = (req, res) => {
    const sql = 'SELECT * FROM drivers';
    const db = new sqlite3.Database('../Source/Formula1.sqlite');
    db.all(sql, [], (err, rows) => {
      if (err) {
        throw err;
      }
      res.json(rows);
    });
  };
  