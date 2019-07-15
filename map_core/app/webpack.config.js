var path = require('path');
var webpack = require('webpack');

module.exports = {
  mode: "none",
  entry: path.resolve(__dirname, 'src/main.js'),
  output: {
	    path: path.resolve(__dirname, '../static/dist'),
	    filename: 'app.js'
  }
};
