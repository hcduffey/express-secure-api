const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const badgeSchema = Schema({
    name: {
        type: String,
        trim: true,
        required: [true, 'a name is required for badges']
    },
    avatar: {
        type: String,
        required: [true, 'a avatar image is required for badges']
    }
}, {timestamps: true});

const Badge = mongoose.model("Badge", badgeSchema);
module.exports = Badge;
