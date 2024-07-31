const router = require('express').Router();
const ConstructorController = require('../Controllers/Constructor');


router.get('/',ConstructorController.getAllConstructors);

module.exports = router;