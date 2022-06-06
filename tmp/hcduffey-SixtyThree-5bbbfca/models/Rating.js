const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const ratingSchema = Schema({
    rating: {
        type: Number,
        min: [0, 'ratings must not be below zero'],
        required: [true, 'a rating is required for ratings']
    },
    comment: {
        type: String,
        trim: true,
    },
    user: {
        type: mongoose.Schema.Types.ObjectId,
        ref: "User",
        required: [true, 'a user is required for ratings']
    },
    park: {
        type: mongoose.Schema.Types.ObjectId,
        ref: "Park",
        required: [true, 'a park is required for ratings']
    }
}, {timestamps: true});

const Rating = mongoose.model("Rating", ratingSchema);
module.exports = Rating;
