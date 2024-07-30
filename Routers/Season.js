const router = require('express').Router();
const SeasonController = require('../Controllers/Season');

router.get('/',SeasonController.getAllSeasons);

module.exports = router;