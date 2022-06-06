const express = require('express')
const router = express.Router()

const db = require('../models')

router.post('/', async(req, res, next) => {
    try {
        if(req.session && req.session.currentUser) {
            const newRating = await db.Rating.create({rating: req.body.rating, comment: req.body.comment, user: req.session.currentUser.id, park: req.body.park});
            return res.redirect('back');
        }
        else {
            return res.redirect('/login');
        }
    }
    catch(err) {
        console.error("Error in rating create: " + err);
        return next();
    }
});

router.delete('/:id', async(req, res, next) => {
    try {
        if(req.session && req.session.currentUser) {
            const ratingToDelete = await db.Rating.findById(req.params.id);

            if(ratingToDelete.user == req.session.currentUser.id) {
                await db.Rating.findByIdAndDelete(req.params.id);
            }

            return res.redirect('back');
        }
        else {
            return res.redirect('/login');
        }
    }
    catch(err) {
        console.error("Error in rating delete: " + err);
        return next();
    }
});

module.exports = router;
