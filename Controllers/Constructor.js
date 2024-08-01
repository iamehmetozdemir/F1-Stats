const mssql = require('mssql');

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

mssql.connect(config)

exports.getAllConstructors =async (req, res) => {
  const sql = 'SELECT * FROM races';
  const result = await mssql.query(sql);
  const table_headers = Object.keys(result.recordset[0]);
  output = '<h1>Constructor</h1>';
  output += '<table border=1>';
  for (let i = 0; i < table_headers.length; i++) {
    output += '<th>' + table_headers[i] + '</th>';
  }
  for (let i = 0; i < result.recordset.length; i++) {
    output += '<tr>';
    for (let j = 0; j < table_headers.length; j++) {
      output += '<td>' + result.recordset[i][table_headers[j]] + '</td>';
    }
    output += '</tr>';
  }
  output += '</table>';
  res.send(output);
}