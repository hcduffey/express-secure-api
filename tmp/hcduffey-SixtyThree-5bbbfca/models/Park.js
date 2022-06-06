const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const parkSchema = Schema({
    name: {
        type: String,
        trim: true,
        required: [true, 'a name is required for parks']
    },
    imageUrl: {
        type: String,
        trim: true,
    },
    city: {
        type: String,
        trim: true,
        required: [true, 'a city is required for parks']
    },
    state: {
        type: String,
        trim: true,
        required: [true, 'a state is required for parks']
    },
    lat: {
        type: String,
        trim: true,
    },
    long: {
        type: String,
        trim: true,
    },
    parkCode: {
        type: String,
        trim: true,
        required: [true, 'a park code is required for parks']
    },
    description: {
        type: String,
        trim: true,
    },
}, {timestamps: true});

const Park = mongoose.model("Park", parkSchema);
module.exports = Park;
