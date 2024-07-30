const router = require('express').Router();
const DriverController = require('../Controllers/Driver');

router.get('/',DriverController.getAllDrivers);

module.exports = router;