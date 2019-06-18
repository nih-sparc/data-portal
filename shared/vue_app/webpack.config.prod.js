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
    path: path.resolve(__dirname, '../static/dist'),
    filename: '_build/bundle.js'
  },
  plugins: [
    new VueLoaderPlugin()
      ]
};
