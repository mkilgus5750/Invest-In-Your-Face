const colors = require('tailwindcss/colors')

module.exports = {
  plugins: [
    require('tailwindcss'),
    require('autoprefixer')
  ],
  purge: {
      enabled: false, //true for production build
      content: [
          'blog/templates/*.html',
          'blog/templates/**/*.html'
      ]
  },
  theme: {
    extend: {
      colors: {
        primary: colors.red,
      }
    }
  }
}
