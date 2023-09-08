const about = ("About");
const home = ("Home");
const getAbout = (req, res) => {
    res.json(about);
};

const getHome = (req, res) => {
    res.json(home)
}
module.exports = { getAbout, getHome };