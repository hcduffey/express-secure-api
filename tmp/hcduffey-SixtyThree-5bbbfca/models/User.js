const mongoose = require('mongoose');
const validator = require('mongoose-validator')
const Schema = mongoose.Schema;

const userSchema = Schema({
    name: {
        type: String,
        trim: true,
        required: [true, 'a name is required for users']
    },
    email: {
        type: String,
        lowercase: true,
        trim: true,
        validate: [
            validator({
                validator: "isEmail",
                message: "a valid e-mail address must be entered"
            })
        ],
        require: [true, "a user must have an e-mail address"]
    },
    password: {
        type: String,
        trim: true,
        required: [true, "a user must have a password"]
    },
    avatar: {
        type: String,
        default: "/images/default_avatar.jpg"
    },
    parks: [{
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Park'
    }],
    badges: [{
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Badge'
    }]
}, {timestamps: true});

const User = mongoose.model("User", userSchema);
module.exports = User;
