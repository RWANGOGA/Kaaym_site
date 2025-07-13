/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,js}",       // Default path
    "./templates/**/*.html",      // Add your template directory
    "./*.html"                    // Root HTML files
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

