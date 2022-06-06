const express = require('express');
const methodOverride = require('method-override')

const session = require('express-session');
const MongoStore = require('connect-mongo');

const controllers = require('./controllers')
const app = express();

const routes = require('./navLinks');
const navLinks = require('./navLinks');

require('./config/db.connection');

app.set('view engine', 'ejs')

// Middleware
app.use(express.static('public'))
app.use(methodOverride('_method'))
app.use(express.urlencoded({ extended: false }))

app.use(
    session({
        store: MongoStore.create({ mongoUrl: process.env.MONGODB_URI}),
        secret: process.env.SECRET,
        resave: false,
        saveUninitialized: false,
        cookie: {
            maxAge: 1000 * 60 * 60 * 24 * 7 * 2
        }
    })
);

app.use(navLinks);

/* SECTION Middleware */
app.use(function (req, res, next) {
    res.locals.navBarUser = req.session.currentUser;
    next();
});

// Controllers
// EXAMPLES: app.use('/products', controllers.products) 
// app.use('/reviews', controllers.reviews) 
app.use('/parks', controllers.parks);
app.use('/users', controllers.users);
app.use('/ratings', controllers.ratings)
app.use('/', controllers.auth);

// Home Route
app.get('/', (request, response) => response.render('index.ejs'));

// Express Server: initializes the server; app.listen allows your computer to receive requests at http://localhost:4000/ 
app.listen(process.env.PORT || 3000, () => console.log(`Listening on port: ${PORT}`))