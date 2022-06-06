require('./config/db.connection');
require('dotenv').config();

const db = require('./models');

const axios = require('axios');

async function getOnePark(parkCode) {
    try {
        const park = await axios.get(`https://developer.nps.gov/api/v1/parks?api_key=${process.env.NPS_API_KEY}&parkCode=${parkCode}`);

        const parkRecord = {
            name: park.data.data[0].name,
            parkCode: park.data.data[0].parkCode,
            lat: park.data.data[0].latitude,
            long: park.data.data[0].longitude,
            state: park.data.data[0].states,
            imageUrl: park.data.data[0].images[0].url
        }
        console.info(parkRecord);

        console.warn(`Remaining API Calls: ${park.headers['x-ratelimit-remaining']}`);
    }
    catch(err) {
        console.error('error in getting park: ' + err);
    }
}

async function getAllParksAndSeed() {
    try {
        const park = await axios.get(`https://developer.nps.gov/api/v1/parks?api_key=${process.env.NPS_API_KEY}&limit=466`);
        const parkData = park.data.data;
        let totalAdded = 0;

        for(let i=0; i < parkData.length; i++) {
            if(parkData[i].designation.includes('National Park') 
            || parkData[i].designation.includes('National and State Parks') 
            || parkData[i].parkCode === 'npsa') 
            {
                let newRecord = {
                    name: parkData[i].name,
                    parkCode: parkData[i].parkCode,
                    lat: parkData[i].latitude,
                    long: parkData[i].longitude,
                    city: parkData[i].addresses[0].city,
                    state: parkData[i].addresses[0].stateCode,
                    imageUrl: parkData[i].images[0].url,
                    description: parkData[i].description
                }

                let addedPark = await db.Park.create(newRecord);
                totalAdded++;
            }
        }

        console.info(`Added ${totalAdded} parks to the database...`);
        console.warn(`Remaining API Calls: ${park.headers['x-ratelimit-remaining']}`);
    }
    catch(err) {
        console.error('error in getting parks: ' + err);
    }
}

async function clearDBAndSeeDB() {
    try {
        let clearedParks = await db.Park.deleteMany({});
        console.info(clearedParks);
        await getAllParksAndSeed();
    }
    catch(err) {
        console.err("error in clearing parks collection: " + err);
    }
}

async function seedBadgeNames() {
    try {
        let parks = await db.Park.find({});

        for(let i = 0; i < parks.length; i++){
            //console.log(`/images/Badges/${parks[i].name.replace(/ /g, "_")}_National_Park_.png`);
            let newBadge = await db.Badge.create({name: parks[i].name, avatar:`/images/Badges/${parks[i].name.replace(/ /g, "_")}_National_Park_.png`});
        }
    }
    catch(err) {
        console.log(err);
    }
}

async function clearBadgeDB() {
    try {
        let clearedBadges = await db.Badge.deleteMany({});
        console.info(clearedBadges);
        //await seedBadgeNames();
    }
    catch(err) {
        console.err("error in clearing parks collection: " + err);
    }
}

//getOnePark('acad');
// clearDBAndSeeDB();

//clearBadgeDB();
seedBadgeNames();