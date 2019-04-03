var mysql = require('mysql');
var express = require('express');
var app = express();
var port = 9201;

var connection = mysql.createConnection({
    host     : 'localhost',
    user     : 'monitor',
    password : 'password',
    database : 'monitoring'
});

connection.connect(function(err) {
    if (err) throw err;
    console.log("Connected!");
});

app.get('/', (req, res) => res.send('Hello World!'))
app.get('/:deviceId', (req, res) => {
    connection.query("SELECT * FROM Sensor WHERE DeviceID=" + req.params.deviceId, function (err, result, fields) {
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(result, null, 3));
    })
});

app.get('/:deviceId/:temp/:humi', (req, res) => {
    var query = "INSERT INTO Sensor (DeviceID, Humidity, Temperature) VALUES ("+ req.params.deviceId+","
    + req.params.humi+","
    + req.params.temp+")";

    connection.query(query, function (err, result, fields) {
        // if (err) throw err;
        res.sendStatus(200)
    })
});

app.listen(port, () => console.log(`Example app listening on port ${port}!`))
