const HtmlWebpackPlugin = require('html-webpack-plugin');
const path = require('path')
const VueLoaderPlugin = require('vue-loader/lib/plugin')

module.exports = {
  entry: path.resolve(__dirname, 'src/main.js'),
  module: {
    rules: [{
        test: /\.vue$/,
        use: 'vue-loader'
    },
    {
      test: /\.js?$/,
      exclude: /node_modules/,
      loader: 'babel-loader',
      query: {
        presets: [
          [
            'env',
            {
              targets: {
                browsers: [
                  'ie >= 11'
                ]
              }
            }
          ]
        ]
      }
    },
    {
        test: /\.(png|svg|jpg|gif)$/,
        use: [
            'file-loader'
        ]
    },
    {
        test: /\.(css|scss)$/,
        use: [
          'vue-style-loader',
          {
            loader: 'css-loader',
            options: {
              // enable CSS Modules
              modules: true,
              // customize generated class names
              localIdentName: '[local]'
            }
          },
          'sass-loader'
    ]}]
  },
  output: {
    path: path.resolve(__dirname, '../../shared/static/dist'),
    filename: '_build/bundle_dat.js'
  },
  plugins: [
    new VueLoaderPlugin(),
    new HtmlWebpackPlugin({
      'template': 'public/index.html',
      'filename': 'browse.html',
      'chunks': ['browse'],
      'inject': false})
  ],
};
