import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import Header from 'common/src/components/Header';
import Footer from 'common/src/components/Footer';
import Home from './pages/Home';
import Game from './pages/Game';
import About from './pages/About';

const Stack = createStackNavigator();

const App = () => {
  return (
    <NavigationContainer>
      <Header />
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={Home} />
        <Stack.Screen name="Game" component={Game} />
        <Stack.Screen name="About" component={About} />
      </Stack.Navigator>
      <Footer />
    </NavigationContainer>
  );
};

export default App;
