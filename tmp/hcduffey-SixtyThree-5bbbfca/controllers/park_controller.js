const express = require('express');
const { default: mongoose } = require('mongoose');
const router = express.Router()

const db = require('../models')
// ROUTES

// index route
router.get('/', async(req, res, next) => {
    try {
        const badges = await db.Badge.find({})
        const context = {badges: badges}
        res.render('./parks/index.ejs', context)
    }
    catch(err) {
        console.log("Error in park index: " + err);
        return next();
    }
});

// show route
router.get('/:id', async(req, res, next) => {
    try {
        const id = req.params.id
        const badges = await db.Badge.find({})
        const parks = await db.Park.find({})

        const ratings = await db.Rating.find({park: parks[id]}).populate('user');
        let beenToPark = false;

        let currentUserId = "";
        if(req.session && req.session.currentUser) {
            currentUserId = req.session.currentUser.id;
            const currentUser = await db.User.findById(currentUserId);
            const parksVisited = currentUser.parks;
            
            if(parksVisited.includes(parks[id]._id)) {
                beenToPark = true;
            }
        }

        const context = {parks: parks, badges: badges, ratings: ratings, currentUserId: currentUserId, id:id, beenToPark: beenToPark}
        res.render('./parks/show.ejs', context)
    }
    catch(err) {
        console.log("Error in park show: " + err);
        return next();
    }
});

// create/refresh parks route
// NOTE: We may or may not need this
router.post('/', async(req, res, next) => {
    try {
        res.send("In park post");
    }
    catch(err) {
        console.log("Error in park post: " + err);
        return next();
    }
});

// put route
router.put('/:id', async(req, res, next) => {
    try {
        res.send("In park put");
    }
    catch(err) {
        console.log("Error in park put: " + err);
        return next();
    }
});

module.exports = router;