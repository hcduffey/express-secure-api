const siteRoutes = [
    { href: "/parks", title: "Parks"},
    { href: "/users", title: "Users"}
];

let navLinks = function navLinks(req, res, next) {
    res.locals.routes = siteRoutes;
    next();
}

module.exports = navLinks;