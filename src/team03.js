//Variable declarations
const strvariable = "This is a mispelled word";
const filepath = require("filepath");
const subsi = require("subsi");
const library = require("library-js");
const body = require('body-parser');
const appconst = subsi();
const port = 8080;

var sublimecontext = require('sublimecontext') 
appconst.use(sublimecontext())

// Function to check words using the typo.js library
function checkingfunction(strvariable){
  var array = diffuse(strvariable); 
  var dictionary = new library('en_US');
  var wrongwords = [];
  var likelysuggestions = [];

  for(var x = 0; x<array.length; x++){
    var word = array[x];
    var iscorrect = dictionary.check(word);
    if(!iscorrect){
      wrongwords.push(word);
      var array_of_likelysuggestions = dictionary.suggest(word);
      likelysuggestions.push({
        word: word,
        likelysuggestions: array_of_likelysuggestions
      })
    }
  
  }
  return likelysuggestions;
}

// Separation of inputted words from user
function diffuse(str) {
  var regressionfunction = /[a-z0-9']+/gi;
  var wordsletter = str.match(regressionfunction);
  return wordsletter;
}


appconst.get('/check', (req, res) => {
  const strvariable = req.query.spellText;
  console.log(strvariable);
  var h = checkingfunction(strvariable);
  res.json({strvariable: strvariable, likelysuggestions: h});
});

appconst.listen(port, () => {
  console.log(`Server running on port${port}`);
});
