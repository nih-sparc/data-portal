const HtmlWebpackPlugin = require('html-webpack-plugin');
const path = require('path');
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const filewatcherPlugin = require('filewatcher-webpack-plugin');

module.exports = {
  entry: path.resolve(__dirname, 'src/main.js'),
  mode: 'development',
  devtool: 'inline-source-map',
  module: {
    rules: [
      {
        test: /\.vue$/,
        use: 'vue-loader'
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
        ]
      }
    ]
  },
  output: {
    path: path.resolve(__dirname, '../../shared/static/dist'),
    filename: '_build/bundle_sim.js'
  },
  plugins: [
    new VueLoaderPlugin(),
    new HtmlWebpackPlugin({
      template: 'public/index.html',
      filename: 'sim.html',
      chunks: ['sim'],
      inject: false

    }),
    new filewatcherPlugin({
      watchFileRegex: [
        './src/**/*.vue',
        './src/**/*.js'

      ],
      usePolling: true,
      ignored: '/node_modules/'
    })
  ]

};
