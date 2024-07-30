const router = require('express').Router();
const RaceController = require('../Controllers/Race');

router.get('/',RaceController.getAllRaces);

module.exports = router;