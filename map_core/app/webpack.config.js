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


// const HtmlWebpackPlugin = require('html-webpack-plugin');
// const path = require('path')
// // const VueLoaderPlugin = require('vue-loader/lib/plugin')
// const filewatcherPlugin = require("filewatcher-webpack-plugin");

// module.exports = {
//   entry: path.resolve(__dirname, 'src/main.js'),
//   module: {
//     rules: [{
//         test: /\.vue$/,
//         use: 'vue-loader'
//     },
//     {
//         test: /\.(png|svg|jpg|gif)$/,
//         use: [
//             'file-loader'
//         ]
//     },
//     {
//         test: /\.(css|scss)$/,
//         use: [
//           'vue-style-loader',
//           {
//             loader: 'css-loader',
//             options: {
//               // enable CSS Modules
//               modules: true,
//               // customize generated class names
//               localIdentName: '[local]'
//             }
//           },
//           'sass-loader'
//     ]}]
//   },
//   output: {
//     path: path.resolve(__dirname, '../../shared/static/dist'),
//     filename: '_build/bundle_map.js'
//   },
//   plugins: [
//     new VueLoaderPlugin(),
//     new HtmlWebpackPlugin({
//       'template': 'templates/map_core.html',
//       'filename': 'maps.html',
//       'chunks': ['maps'],
//       'inject': false}),
//     new filewatcherPlugin({
//       watchFileRegex: [
//         './src/**/*.js',
//       ],
//       usePolling: true,
//       ignored: '/node_modules/'
//     })
//   ],
// };
