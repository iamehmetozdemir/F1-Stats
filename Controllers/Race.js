const sqlite3 = require('sqlite3').verbose();

exports.getAllRaces = (req, res) => {
    const sql = 'SELECT * FROM races';
    const db = new sqlite3.Database('../Source/Formula1.sqlite');
    db.all(sql, [], (err, rows) => {
      if (err) {
        throw err;
      }
      res.json(rows);
    });
  };