var path = require('path');
var webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  mode: "none",
  entry: path.resolve(__dirname, 'src/main.js'),
  output: {
	    path: path.resolve(__dirname, '../../shared/static/dist'),
	    filename: '_build/bundle_map.js'
  },
  plugins: [
        new HtmlWebpackPlugin({
          'template': 'templates/map_core.html',
          'filename': 'maps.html',
          'chunks': ['maps'],
          'inject': false})
      ]
};