#!/bin/bash

# Define the project root directory
ROOT_DIR="web-app"

# Create the project root directory
mkdir -p $ROOT_DIR

# Navigate to the project root directory
cd $ROOT_DIR

# Create the public directory and index.html file
mkdir -p public
touch public/index.html

# Create the src directory and subdirectories
mkdir -p src/assets/images
mkdir -p src/components
mkdir -p src/pages
mkdir -p src/styles

# Create the basic component files
touch src/components/Header.js
touch src/components/Footer.js
touch src/components/GameBoard.js

# Create the basic page files
touch src/pages/Home.js
touch src/pages/Game.js
touch src/pages/About.js

# Create the main application files
touch src/App.js
touch src/index.js
touch src/styles/GlobalStyles.js

# Create a basic package.json file
cat <<EOL > package.json
{
  "name": "game-app",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "react-router-dom": "^6.0.0",
    "styled-components": "^5.3.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }
}
EOL

# Output a message indicating the structure has been created
echo "Folder structure created successfully."
