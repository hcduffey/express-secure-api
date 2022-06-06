module.exports = {
    Badge: require('./Badge'),
    Park: require('./Park'),
    Rating: require('./Rating'),
    User: require('./User')
};

// TEST CODE - It may be useful to keep in the comments as a reference

// This is requiring in the connection that's linking to my Mongo Atlas
// require('../config/db.connection')

// const Park = require('./Park');
// const User = require('./User');
// const Rating = require('./Rating');


// User.create({
//     name: "Cliff Duffey",
//     email: "cliff@test.com",
//     password: "notapassword"
// }).then((response) => console.log(response));

// Park.create({
//     name: "Test Park",
//     imageUrl: "http://www.google.com",
//     city: "Alexandria",
//     state: "Virginia",
//     lat: "123",
//     long: "123",
//     parkCode: "tp"
// }).then((response) => console.log(response));

// Park.create({
//     name: "Second Park",
//     imageUrl: "http://www.google.com",
//     city: "Alexandria",
//     state: "Virginia",
//     lat: "123",
//     long: "123",
//     parkCode: "tp"
// }).then((response) => console.log(response));


// User.updateOne({name: "Cliff Duffey"}, {email: "cliff@updated.com"}).then((response) => console.log(response));
// async function addParkToUser() {
//     try {
//         let parktoAdd = await Park.findOne({name: "Second Park"});
//         let usertoUpdate = await User.findOne({name: "Cliff Duffey"});
//         usertoUpdate.parks.push(parktoAdd);
//         usertoUpdate.save();
//     }
//     catch(err) {
//         console.log(err);
//     }
// }

// addParkToUser();

// User.find({name: "Cliff Duffey"}).then((response) => console.log(response));

// async function createRating() {
//     try {
//         let parktoRate = await Park.findOne({name: "Test Park"});
//         let user = await User.findOne({name: "Cliff Duffey"});

//         let newRating = await Rating.create({rating: 5, comment: "Good park", park: parktoRate, user: user});
//         console.log(newRating);
//     }
//     catch(err) {
//         console.log(err);
//     }
// }

// createRating();