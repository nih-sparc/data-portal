const path = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  mode: "none",
  entry: path.resolve(__dirname, 'src/main.js'),
  output: {
	    path: path.resolve(__dirname, '../../shared/static/dist'),
      filename: '_build/bundle_map.[contenthash].js',
      chunkFilename: '_build/[name].[contenthash].js'
  },
  module: {
    rules: [
      { test: /\.css$/, use: [ 'style-loader', 'css-loader' ] },
      { test: /\.(jpe?g|gif)$/i,
        loader:"file-loader",
        query:{
          
          name:'[name].[ext]',
          outputPath:'images/' }
      },
      { test: /\.(png|woff|woff2|eot|ttf|svg)$/, loader: 'url-loader?limit=100000' }
    ]
  },
  optimization: {
    splitChunks: {
      maxSize: 400000,
      cacheGroups: {
        maps: {
          test: /[\\/]node_modules[\\/]/,
          // cacheGroupKey here is `commons` as the key of the cacheGroup
          name(module, chunks, cacheGroupKey) {
            const moduleFileName = module.identifier().split('/').reduceRight(item => item);
            const allChunksNames = chunks.map((item) => item.name).join('~');
            return `${cacheGroupKey}-${allChunksNames}-${moduleFileName}`;
          },
          chunks: 'async'
        }
      }
    }
  },
  plugins: [
      new HtmlWebpackPlugin({
        'template': 'templates/map_core.html',
         'filename': 'maps.html',
         'chunks': ['maps'],
         'inject': false})
  ]
};